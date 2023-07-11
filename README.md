# blooket-coins-bot

Bot to automatically earn daily blooket coins.<br>

**How it works:** Bot opens chrome, logs in to blooket, plays cafe game and autoclicks for 6 minutes.<br>

**Disclaimer:** Though the bot uses undetected_chromedriver to avoid bot detection, I will not be liable if your account gets banned.

# Requirements
* **python >= 3.11.3**
    * [Install python](https://www.python.org/downloads/)
* Git
    * [Git for Windows](https://gitforwindows.org/)
    * [Git for MacOS](https://sourceforge.net/projects/git-osx-installer/files/git-2.23.0-intel-universal-mavericks.dmg/download?use_mirror=autoselect)
* High speed Internet Connection
* Blooket set with 1 question + 2 answers (both correct)
* (Only for mac users) System preferences > Security & Privacy > Accesibility > Under privacy tab, allow iTerm and VScode control

# How to get started
## 1. Install the script
Make sure you have read the requirements above <br>

Go to your terminal and run
```
git clone https://github.com/jiakai2002/blooket-coins-bot.git
```

```
cd blooket-coins-bot
```

```
python3 -m pip install --upgrade pip wheel
```

```
pip3 install "setuptools<59"
```

```
pip3 install -r requirements.txt
```

## 2. Setup login details in script
Open Python IDLE (search for "IDLE")<br>

Go to File > Open > blooket-coins-bot.py

```
# *** EDIT LOGIN DETAILS ****
# don't worry, only you can see this
email = "insert_your_email"
password = "insert_your_password"
```

Insert your Blooket email and password, for e.g. <br>
```
email = "floyd@gmail.com"
password = "password123"
```

Save blooket-coins-bot.py
## 3. Usage
Subsequently, you can do this to run the bot: <br>

Go to your terminal and run
```
cd blooket-coins-bot
```
```
python3 blooket-coins-bot.py
```

