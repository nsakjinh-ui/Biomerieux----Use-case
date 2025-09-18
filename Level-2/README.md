## Level 2: Social Network

_Nice work finishing Level 1: Cyber Monday! It's now time for Level 2: Social Network_ :sparkles:

Languages: `python3`

### 📝 Storyline

In the mid-2030s, governments launch social networks to fight crime and assist citizens. Users can upload tax forms, set profile pictures, and share public tips. But the rush to digitize has left the platform exposed. Hackers may access files far beyond what was intended. Can you secure the system and unlock Level 3?

### :keyboard: Setup instructions

- For Level 2, we encourage you to enable code scanning with CodeQL. For more information about CodeQL, see "[About CodeQL](https://codeql.github.com/docs/codeql-overview/about-codeql/)." For instructions setting up code scanning, see "[Setting up code scanning using starter workflows](https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/setting-up-code-scanning-for-a-repository#setting-up-code-scanning-using-starter-workflows)."

### :keyboard: What's in the repo?

For each level, you will find the same file structure:

- `code` includes the vulnerable code to be reviewed.
- `hack` exploits the vulnerabilities in `code`. Running `hack.py` will fail initially, your goal is to get this file to pass 🟢.
- `tests` contains the unit tests that should still pass 🟢 after you have implemented your fix.

### 🚦 Time to start!

1. Review the code in `code.py`. Can you spot the bug(s)?
1. Try to fix the bug. Open a pull request to `main` or push your fix to a branch.
1. You successfully completed this level when you (a) resolve all related code scanning alerts and (b) when both `hack.py` and `tests.py` pass 🟢.
1. If you need more guidance, read the CodeQL scanning alerts.