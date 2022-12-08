# Love Language - FastAPI

How to run API via Local
1. Open terminal using wsl on your windows at API directory
2. Create venv by
```sh
python3 -m venv venv
```
3. Activate virtual environment by 
```sh
source venv/bin/activate
```
4. Install required module in requirements.txt by
```sh
pip install -r requirements.txt
```
5. Create file .env and state variable with SECRET_KEY and ALGORITHM
```sh
touch .env

#In file .env
SECRET_KEY = "xxxx" #editable
ALGORITM = "HS256" #editable as long as valid
```
6. Run API by
```sh
python3 main.py
```
## Done, Enjoy!
