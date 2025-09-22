## Level 4: Locanda


Languages: `python3`


### 📝 Storyline

Locanda attracts travelers who prefer long passphrases. But the backend team rushed deployment and implemented password handling incorrectly. Some accounts may be vulnerable to dictionary attacks or hash guessing. Your mission: inspect the authentication code (storage & comparison), find the fatal mistake, and secure Locanda’s passwords so guests stay safe.


### :keyboard: What's in the repo?

For each level, you will find the same file structure:

- `code` includes the vulnerable code to be reviewed.
- `hack` exploits the vulnerabilities in `code`. In this level, this file is inactive.
- `tests` contains the unit tests that should still pass 🟢 after you have implemented your fix.

### 🚦 Time to start!

1. Review the code in `code.py`. Can you spot the bug(s)?
1. Try to fix the bug. Open a pull request to `main` or push your fix to a branch.
1. You successfully completed this level when you (a) resolve all related code scanning alerts and (b) `tests.py` pass 🟢. Notice that `hack.py` in this level is inactive.
1. If you need more guidance, read the CodeQL scanning alerts.
