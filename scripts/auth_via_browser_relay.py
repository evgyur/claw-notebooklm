#!/usr/bin/env python3
import argparse
import asyncio
import os
import subprocess
import sys
from pathlib import Path

from playwright.async_api import async_playwright


def notebooklm_home() -> Path:
    return Path(os.environ.get("NOTEBOOKLM_HOME", Path.home() / ".notebooklm")).expanduser()


async def export_state(browser_url: str, target_url: str, state_path: Path, wait_ms: int) -> tuple[str, str]:
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(browser_url)
        ctx = browser.contexts[0] if browser.contexts else await browser.new_context()
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()
        await page.goto(target_url, wait_until="domcontentloaded", timeout=60000)
        await page.wait_for_timeout(wait_ms)
        state_path.parent.mkdir(parents=True, exist_ok=True)
        await ctx.storage_state(path=str(state_path))
        final_url = page.url
        title = await page.title()
        await browser.close()
        return final_url, title


def run_auth_check(notebooklm_bin: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [notebooklm_bin, "auth", "check", "--test"],
        capture_output=True,
        text=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Export NotebookLM auth from Browser Relay into ~/.notebooklm/storage_state.json")
    parser.add_argument("--browser-url", default=os.environ.get("OPENCLAW_BROWSER_RELAY_URL", "http://127.0.0.1:18800"))
    parser.add_argument("--target-url", default="https://notebooklm.google.com/")
    parser.add_argument("--wait-ms", type=int, default=4000)
    parser.add_argument("--state-path", default=str(notebooklm_home() / "storage_state.json"))
    parser.add_argument("--notebooklm-bin", default=str(Path(__file__).resolve().parent.parent / ".venv/bin/notebooklm"))
    args = parser.parse_args()

    state_path = Path(args.state_path).expanduser()

    try:
        final_url, title = asyncio.run(export_state(args.browser_url, args.target_url, state_path, args.wait_ms))
    except Exception as exc:
        print(f"Failed to connect to Browser Relay or export state: {exc}", file=sys.stderr)
        return 1

    result = run_auth_check(args.notebooklm_bin)

    print(f"saved_to={state_path}")
    print(f"final_url={final_url}")
    print(f"title={title}")
    print("---")
    if result.stdout:
        print(result.stdout.rstrip())
    if result.stderr:
        print(result.stderr.rstrip(), file=sys.stderr)

    if result.returncode != 0:
        print(
            "Browser Relay export succeeded, but NotebookLM auth check still failed. "
            "Make sure the attached browser session is already logged into the target Google account and can open NotebookLM.",
            file=sys.stderr,
        )
        return result.returncode

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
