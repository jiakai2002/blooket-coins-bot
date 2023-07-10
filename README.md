# blooket-coins-bot

Bot to automate earning daily blooket coins.<br>

**How it works:** Bot opens chrome, logs in to blooket, plays cafe game and autoclicks for 6 minutes.<br>

**Disclaimer:** Though the bot uses undetected_chromedriver to avoid bot detection, I will not be liable if your account gets banned.

# Requirements
* **python >= 3.11.3**
* High speed Internet Connection
* Blooket set with 1 question + 2 answers (both correct)

# How to get started
## 1. Install the script
Go to your terminal and run<br>

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
python3 -m pip install --upgrade pip wheel
```

```
pip3 install "setuptools<59"
```

```
pip3 install -r requirements.txt
```

## 2. Setup login details in script
Open blooket-coins-bot.py at line 11 to 14

```
# *** EDIT LOGIN DETAILS ****
# don't worry, only you can see this
email = "insert_your_email"
password = "insert_your_password"
```

Insert your Blooket account email and password
## 3. Usage
Go to your terminal and with cwd as blooket-coins-bot folder, run

```
python3 blooket-coins-bot.py
```

