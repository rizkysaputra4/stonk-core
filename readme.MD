# Welcome to Project STONK

requirements:
1. Python 3.9++ installed
2. talib installed, if not follow [this link](https://github.com/mrjbq7/ta-lib/blob/master/README.md) to install.
## How to run stonk-core

1. Clone the project

```
git clone https://github.com/rizkysaputra4/stonk.git
```
2. Open the project folder from terminal
3. Create virtual environment by command:
```
python3 -m venv venv
```
4. Activate venv by:
```commandline
source venv/bin/activate
```

4. Install all dependency

```
pip install -r requirements.txt
```

4. Run the project

```
python main.py
```

5. Test the api

```
open this url from your postman or browser

http://127.0.0.1:8087/
```

## Build the application
To build application into binary executable use this command:
```commandline
pyinstaller --onefile --paths /(path to venv)/venv/lib/python3.9/site-packages --hidden-import talib.stream main.py
```
