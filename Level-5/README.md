## Level 5: Space-Crossing

_Almost there! One level to go and complete the mission!_ :heart:

Languages: `python3`

### 📝 Storyline

Space enthusiasts built a public website to share facts about planets, with a search bar for visitors to explore. But in their rush, they overlooked a critical web security issue: user input isn’t handled safely. Attackers can inject malicious code into the site. Can you secure the search feature, protect the community, and complete the mission?

### :keyboard: Setup instructions

- For Level 5, we encourage you to enable code scanning with CodeQL. For more information about CodeQL, see "[About CodeQL](https://codeql.github.com/docs/codeql-overview/about-codeql/)." For instructions on setting up code scanning, see "[Setting up code scanning using starter workflows](https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/setting-up-code-scanning-for-a-repository#setting-up-code-scanning-using-starter-workflows)."

### :keyboard: What's in the repo?

- `code` includes the vulnerable code to be reviewed.
- `hack` exploits the vulnerabilities in `code`. Running `hack` will fail initially and your goal is to get this file to pass 🟢.
- `templates/index.html` host a simple front-end to interact with the back-end.
- `tests` contains the unit tests that should still pass 🟢 after you implement your fix.

### 🚦 Time to start!

1. Review the code in `code.py`. Can you spot the bug(s)?
1. Try to fix the bug. Open a pull request to `main` or push your fix to a branch.
1. You successfully completed this level when you (a) resolve all related code scanning alerts and (b) when both `hack.py` and `tests.py` pass 🟢.
1. If you need more guidance, read the CodeQL scanning alerts.
1. If you get stuck, ask for help.

## Finish

_🎉 Congratulations, you've completed the mission! 🎉_

<footer>



---


</footer>
