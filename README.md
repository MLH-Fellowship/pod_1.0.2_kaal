# Kaal  
![](https://img.shields.io/youtube/views/_bkIw7igeJM?label=Views&style=for-the-badge) [Video Link](https://www.youtube.com/watch?v=_bkIw7igeJM)
  
![](https://img.shields.io/badge/commit%20activity-+70-blue) ![](https://github.com/MLH-Fellowship/0.2.1-fellowbook) ![](https://img.shields.io/badge/build-passing-brightgreen) ![](https://img.shields.io/badge/contributors-only%203-orange) ![](https://img.shields.io/badge/version-1.0.0-yellow) ![](https://img.shields.io/badge/learned%20a%20lot-yes-blue)  
  
![Banner](https://github.com/MLH-Fellowship/pod_1.0.2_moropy/blob/master/branding/github_banner.png)  

<p align="center">
    October 12th, 2020 - <a href='https://fellowship.mlh.io/'>MLH Fellowship</a> Orientation Hackathon Project<br>
    by <a href='https://github.com/zerefwayne'>Aayush Joglekar</a>, <a href='https://github.com/pandafy'>Gagan Deep</a> and <a href='https://github.com/rish07'>Rishi Raj Singh</a>.
</p>

## 💁‍♂️ What is the project?

**Kaal is a productivity suite with a beautiful CLI ✨ and Discord Bot 🤖. Kaal shows the fellows' work time and productivity at a glance within Discord and a simple CLI tool to track each fellow's coding routine while working for the fellowship. 💪**

— *Gamify the pod's productivity!*

## 🧑‍🔬 How to use it?

#### Prerequisites:

1. Python3: [Installation Steps](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu)
2. Clone the repository: `https://github.com/MLH-Fellowship/pod_1.0.2_moropy.git`
3. Type `sudo apt-get install xdotool`
4. Head over to the cloned repository's `kaal_cli` folder and type `pip3 install -r requirements.txt`
5. All the dependencies will be installed and the project is good to go! 🎉


#### Instructions:

1. Type `!register` command in the Kaal enabled Discord channel and it'll return your `Secret Code` 🤫 in the DM.
2. Head over to the repository and type `./moropy.py register` and paste the `Secret Code`.
3. When you wish to start the work, type `./moropy.py checkin` and it'll start watching the softwares open. 👀
4. When it's time to stop the work, type `./moropy.py checkout`, the CLI will check you out and stop watching the windows. 😌

## 🙇 Why do we need it?

This project was inspired by [WakaTime](https://wakatime.com/) and the amazing Discord Bots! 

Using this project, the productivity of the pod can be monitored without invading the privacy and can be used to have a healthy competition within the pod. The pod leader (or anyone in the channel) can see the performance of all fellows in that week (or all-time data) in the form of a leaderboard. 🧑🏻‍💻

## 🧑‍💻 Our tech stack!

1. **[Flask](https://flask.palletsprojects.com/en/1.1.x/)** 1️⃣

    Flask is being used as the backend server to listen for updates from CLI, managing database and listening to the discord bot.

2. **[Click](https://pypi.org/project/click/)** 2️⃣

    Click package manages the beautiful CLI and triggers background scripts for listening to window changes.

3. **[discord.py](https://pypi.org/project/discord.py/)**

    `discord.py` helps to provision the REST APIs for the bot-server communication.

4. **[Firestore](https://firebase.google.com/docs/firestore)**

    Firestore is being used as the primary database.

5. **[Heroku](https://www.heroku.com/)**

    Heroku hosts the backend server for the Bot and CLI.

6. **[xdotool](https://www.howtoinstall.me/ubuntu/18-04/xdotool/)**

    xdotool is a linux package to listen to the active window process ID.

## 🙏🏻 Anything else?

Remember the rules!

It's _not_ about:

- how good your code is,
- how novel the idea is, or
- how useful the project is.

It _is_ about:

- **Impressive**: People's wows are on record! Check Discord!
- **Design**: A snappy 24/7 available bot and a beautiful CLI :stars:
- **Completion**: Our hack works completely!
- **Learning**: Discord Bot, Authorization, Bash Scripting and Flask!
- **OSS practices**: Plentiful commits, Code reviews, Kanban boards, issues, branches, PRs!
- **Approved tech**: Flask, Click

In short:

> _Sometimes a pointless project is one of the best hacks!_<br> [—MLH Hackathon Rules](https://github.com/MLH-Fellowship/fellows-0/blob/master/orientation-hackathon/rules.md)
