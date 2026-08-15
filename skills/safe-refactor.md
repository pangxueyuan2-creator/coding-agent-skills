# Safe Refactor Skill

When asked to do large refactors or renames:

1. First list all files and symbols that will be affected.
2. Prefer small, incremental commits / changes over one giant rewrite.
3. Keep the public API stable unless explicitly told to break it.
4. After each major step, ensure existing tests still pass (or clearly report what is broken).
5. Never delete functionality without confirming it is no longer needed.
6. Document the migration path if behavior changes.

Finish with a short summary of what was changed and what still needs human attention.
