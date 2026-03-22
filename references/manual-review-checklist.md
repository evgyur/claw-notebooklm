# Manual review checklist

- [ ] `SKILL.md` stays short and routes to first-level references.
- [ ] The public command name is `/claw-notebook-llm`.
- [ ] `/notebook-llm` and `/notebooklm` are documented as compatibility aliases.
- [ ] Auth path and shared-context risk are documented.
- [ ] Browser Relay auth flow does not depend on a custom relay skill.
- [ ] No local secrets, auth files, or browser profiles are committed.
- [ ] Long-running generation/download actions are treated as confirm-first in the main conversation.
- [ ] Route helpers (`routes`, `route-info`, `route-prompt`, `route-init`, `route-ask`) work and match documented presets.
- [ ] Public usage routes are discoverable from the README and references.
- [ ] Upstream repo remains pinned as `references/notebooklm-py` submodule.
- [ ] Wrapper/install scripts stay transparent and do not hide the underlying `notebooklm` behavior.
