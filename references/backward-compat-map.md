# Backward compatibility map

## Naming

- Public/local OpenClaw skill command: `/claw-notebook-llm`
- Compatibility aliases: `/notebook-llm`, `/notebooklm`
- Upstream project/CLI name: `notebooklm`

## Compatibility rule

When a user says any of the following, route to this skill:
- `/claw-notebook-llm`
- `/notebook-llm`
- `/notebooklm`
- `NotebookLM`
- `notebooklm`
- `notebook lm`

## Command compatibility

- Actual shell command stays `notebooklm`
- Wrapper command is `claw-notebook-llm`
- Upstream docs/examples using `notebooklm ...` remain valid as-is

## Breaking changes

None for existing direct `notebooklm` CLI usage.

## Migration note

This repo renames the skill surface to `claw-notebook-llm` while preserving legacy trigger compatibility.
