# Agent Self-Check Skill

Before you say a task is finished, run this mental checklist:

1. Did I actually solve the original request, or did I drift?
2. Are there any secrets or sensitive data in the changes?
3. Did I add or update tests for the new behavior?
4. Is the documentation still accurate?
5. Would a human reviewer be able to understand the change without asking me questions?
6. Did I leave any TODO / FIXME / temporary code that should not be merged?

If any answer is "no" or "I'm not sure", fix it before finishing.

## Output
When done, briefly state:

> Self-check passed. Key points verified: ...
