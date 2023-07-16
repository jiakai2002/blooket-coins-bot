# blooket-coins-bot

Bot to automatically earn daily blooket coins.<br>

**How it works:** Bot opens chrome, logs in to blooket, plays cafe game and autoclicks for 6 minutes.<br>

**Disclaimer:** Though the bot uses undetected_chromedriver to avoid bot detection, I will not be liable if your account gets banned.

# Requirements
* **python >= 3.11.3**
* High speed Internet Connection
* Blooket set with 1 question + 2 answers (both correct)
* (For mac users) System preferences > Security & Privacy > Accesibility > Under privacy tab, allow iTerm and VScode control

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
user = "insrt_your_user"
password = "insert_your_password"
```

Insert your blooket account details<br>
e.g.
```
user = "floyd@gmail.com"
password = "password123"
```

## 3. Usage
Go to your terminal and with cwd as blooket-coins-bot folder, run

```
python3 blooket-coins-bot.py
```

