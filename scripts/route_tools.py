#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROUTES_JSON = ROOT / "routes" / "routes.json"
NOTEBOOKLM = ROOT / ".venv" / "bin" / "notebooklm"


def load_routes():
    data = json.loads(ROUTES_JSON.read_text())
    routes = {r["id"]: r for r in data["routes"]}
    return routes


def ensure_runtime():
    if not NOTEBOOKLM.exists():
        print(f"NotebookLM runtime is not installed here yet. Run: bash {ROOT / 'scripts' / 'install.sh'}", file=sys.stderr)
        raise SystemExit(1)


def run_json(cmd, timeout=300):
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if p.returncode != 0:
        print(p.stdout, end="", file=sys.stderr)
        print(p.stderr, end="", file=sys.stderr)
        raise SystemExit(p.returncode)
    return json.loads(p.stdout)


def list_routes(routes):
    for r in routes.values():
        print(f"{r['id']}: {r['title']} — {r['summary']}")


def show_route(route, as_json=False):
    if as_json:
        print(json.dumps(route, ensure_ascii=False, indent=2))
        return
    print(f"ID: {route['id']}")
    print(f"Title: {route['title']}")
    print(f"Summary: {route['summary']}")
    print("Best for:")
    for item in route.get("best_for", []):
        print(f"- {item}")
    print("Source checklist:")
    for item in route.get("source_checklist", []):
        print(f"- {item}")
    print("Recommended artifacts:")
    for item in route.get("recommended_artifacts", []):
        print(f"- {item}")
    print("Cautions:")
    for item in route.get("cautions", []):
        print(f"- {item}")
    print("Prompts:")
    for key, value in route.get("prompts", {}).items():
        print(f"- {key}: {value}")


def print_prompt(route, phase):
    prompts = route.get("prompts", {})
    if phase not in prompts:
        print(f"Unknown phase '{phase}'. Available: {', '.join(prompts)}", file=sys.stderr)
        raise SystemExit(1)
    print(prompts[phase])


def route_init(route, title, sources, wait, as_json):
    ensure_runtime()
    created = run_json([str(NOTEBOOKLM), "create", title, "--json"], timeout=180)
    notebook = created.get("notebook", created)
    notebook_id = notebook["id"]
    added = []
    waited = []
    for source in sources:
        added_json = run_json([str(NOTEBOOKLM), "source", "add", "-n", notebook_id, source, "--json"], timeout=300)
        src = added_json.get("source", added_json)
        added.append(src)
        if wait:
            wait_json = run_json([str(NOTEBOOKLM), "source", "wait", "-n", notebook_id, src["id"], "--timeout", "600", "--json"], timeout=720)
            waited.append(wait_json)
    result = {
        "route": route["id"],
        "notebook_id": notebook_id,
        "title": notebook.get("title", title),
        "sources_added": added,
        "sources_waited": waited,
        "next_prompts": route.get("prompts", {}),
        "recommended_artifacts": route.get("recommended_artifacts", [])
    }
    if as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return
    print(f"Route: {route['id']}")
    print(f"Notebook: {result['title']}")
    print(f"Notebook ID: {notebook_id}")
    print(f"Sources added: {len(added)}")
    if wait:
        print("Sources waited: yes")
    print("---")
    for phase, prompt in route.get("prompts", {}).items():
        print(f"Next prompt [{phase}]:")
        print(prompt)
        print()
    print("Suggested next commands:")
    for phase in route.get("prompts", {}):
        print(f"claw-notebook-llm route-ask {route['id']} {notebook_id} {phase}")


def route_ask(route, notebook_id, phase, as_json):
    ensure_runtime()
    prompts = route.get("prompts", {})
    if phase not in prompts:
        print(f"Unknown phase '{phase}'. Available: {', '.join(prompts)}", file=sys.stderr)
        raise SystemExit(1)
    answer = run_json([str(NOTEBOOKLM), "ask", "-n", notebook_id, prompts[phase], "--json"], timeout=600)
    if as_json:
        print(json.dumps(answer, ensure_ascii=False, indent=2))
        return
    print(json.dumps(answer, ensure_ascii=False, indent=2))


def main():
    routes = load_routes()

    p = argparse.ArgumentParser(description="Route helpers for claw-notebook-llm")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list")

    show = sub.add_parser("show")
    show.add_argument("route")
    show.add_argument("--json", action="store_true")

    prompt = sub.add_parser("prompt")
    prompt.add_argument("route")
    prompt.add_argument("phase", choices=["map", "summary", "extract"])

    init = sub.add_parser("init")
    init.add_argument("route")
    init.add_argument("title")
    init.add_argument("sources", nargs="*")
    init.add_argument("--no-wait", action="store_true")
    init.add_argument("--json", action="store_true")

    ask = sub.add_parser("ask")
    ask.add_argument("route")
    ask.add_argument("notebook_id")
    ask.add_argument("phase", choices=["map", "summary", "extract"])
    ask.add_argument("--json", action="store_true")

    args = p.parse_args()

    if args.cmd == "list":
        list_routes(routes)
        return

    if args.route not in routes:
        print(f"Unknown route '{args.route}'. Available: {', '.join(routes)}", file=sys.stderr)
        raise SystemExit(1)

    route = routes[args.route]

    if args.cmd == "show":
        show_route(route, as_json=args.json)
    elif args.cmd == "prompt":
        print_prompt(route, args.phase)
    elif args.cmd == "init":
        route_init(route, args.title, args.sources, wait=not args.no_wait, as_json=args.json)
    elif args.cmd == "ask":
        route_ask(route, args.notebook_id, args.phase, as_json=args.json)


if __name__ == "__main__":
    main()
