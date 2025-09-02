# Secure Coding Challenge

_Welcome to Secure Coding Challenge!_ :wave:

To get started, please follow the 🛠️ set up guide.

[![start-course](https://user-images.githubusercontent.com/1221423/235727646-4a590299-ffe5-480d-8cd5-8194ea184546.svg)](https://github.com/new?template_owner=nsakjinh-ui&template_name=Biom-rieux----Use-case&owner=%40me&name=skills-secure-code-game&description=My+clone+repository&visibility=public)


1. Right-click **Start course** and open the link in a new tab.
1. In the new tab, most of the prompts will automatically fill in for you.
   - For owner, choose your personal account or an organization to host the repository.
   - We recommend creating a public repository, as private repositories will [use Actions minutes](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions).
   - Scroll down and click the **Create repository** button at the bottom of the form.
1. You can now proceed to the 🛠️ set up section.

## 🛠️ The set up

#### 🖥️ Using codespaces

All levels are configured to run instantly with GitHub Codespaces. If you chose to use codespaces, be aware that this course **will count towards your 60 hours of monthly free allowance**. For more information about GitHub Codespaces, see the "[GitHub Codespaces overview](https://docs.github.com/en/codespaces/overview)." If you prefer to work locally, please follow the local installation guide in the next section.

1. To create a codespace, click the **Code** drop down button in the upper-right of your repository navigation bar.
1. Click **Create codespace on main**.
1. After creating a codespace, relax and wait for VS Code extensions and background installations to complete. This should take less than three minutes.
1. At this point, you can get started with Levels 1, 2, 3, 4, 5, by navigating on the respective folders and reading the `README.md` file.



#### 💻 Local installation

Please note: You don't need a local installation if you are using GitHub Codespaces.

The following local installation guide is adapted to Debian/Ubuntu and CentOS/RHEL, and assumes your goal is to play through all the game's seasons.

1. Open your terminal.
1. Install OpenLDAP headers needed to compile `python-ldap`, depending on your Linux distribution. Check by running:

```bash
uname -a
```
- For Debian/Ubuntu, run:
```bash
sudo apt-get update
sudo apt-get install libldap2-dev libsasl2-dev
```

- For CentOS/RHEL, run:

```bash
sudo yum install python-devel openldap-devel
```

- For Archlinux, run:

```bash
sudo pacman -Sy libldap libsasl
```

- Then, for all of the above Linux distributions install `pyOpenSSL` by running:

```bash
pip3 install pyOpenSSL
```

Once installation has completed, clone your repository to your local machine and install required dependencies.

1. From your repository, click the **Code** drop down button in the upper-right of your repository navigation bar.
1. Select the `Local` tab from the menu.
1. Copy your preferred URL.
1. In your terminal, change the working directory to the location where you want the cloned directory.
1. Type `git clone` and paste the copied URL.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

6. Press **Enter** to create your local clone.
7. Change the working directory to the cloned directory.
8. Install dependencies by running:

```bash
pip3 install -r requirements.txt
```

- Programming Languages

To play, you will need to have `python3` installed.

If you are using VS Code locally, you can install the above programming languages through the editor extensions with these identifiers:

1. `ms-python.python`
1. `ms-python.vscode-pylance`
 
At this point, you can get started with Levels 1, 2, 3, 4, 5, by navigating on the respective folders and reading the `README.md` file.



<footer>



---
