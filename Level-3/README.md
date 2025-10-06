## Level 3: Data Bank

_Nicely done! Level 2: Social Network is complete. It's time for Level 3: Database_ :partying_face:

Languages: `python3`, `sql`


### 📝 Storyline

The data backbone of our platform holds stock prices and historical records. A single rogue query could alter prices or delete tables — and an attacker is already probing endpoints. Can you harden the database layer so users can’t inject SQL and rewrite history? Secure it, keep the tests green, and progress to Level 4.


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

2. > Heads up, you need to erase the created database in order to start testing again.
