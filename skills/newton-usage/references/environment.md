# Select an existing Python environment

- Confirm which interpreter the task uses before probing. A project `.venv`
  and an activated environment can point to different installations. If the
  task requires a wrapper for variables or project context, keep using it.
- For an existing uv project environment, use
  `uv run --project <project> --no-sync --frozen python ...`. Use
  `uv run --active --no-sync --frozen python ...` when the active environment
  is the intended one. Check that the target exists first. These commands
  assume the project directory and any environment-selection settings are known.
- If no non-mutating route is available, report the blocker. If selection is
  ambiguous, ask for the interpreter or launch command. Installing or syncing
  dependencies requires authorization.
