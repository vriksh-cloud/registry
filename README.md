# Vriksh Lab Registry

This repository contains the declarative YAML specifications for spinning up interactive, ephemeral lab environments in the Vriksh Engine.

## Schema
Labs are fully agnostic to the backend engine. They define the exact Docker container, port mappings, environment variables, initialization scripts, and checkpoint validation rules.

### Fields
- `id`: Unique identifier (e.g., `git-101`)
- `name`: Display name for the lab catalog.
- `target_port`: The container port to expose to the learner via Traefik.
- `image`: The exact Docker image to run.
- `environment`: List of environment variables (supports `{lab_url}`).
- `volumes`: List of volume mounts (optional).
- `init_script`: A bash script to run securely *after* the container starts (supports `{container_name}`).
- `tasks`: A list of checkpoints. Each contains a `validation` block containing a specific shell `command` to execute via Docker exec to verify completion.

## Verification
You can validate the structure of these YAML files by running:
```bash
python scripts/validate_lab_schema.py
```
