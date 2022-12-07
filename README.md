# Love-FastAPI

Cara Run API Secara Lokal
1. Buka terminal (gunakan wsl pada windows) pada folder API
2. Buat venv dengan
```sh
python3 -m venv venv
```
3. Aktifkan venv dengan
```sh
source venv/bin/activate
```
4. Install module yang ada di requirements.txt dengan
```sh
cd src
pip install -r requirements.txt
```
5. Buat file .env dan tetapkan variabel SECRET_KEY dan ALGORITM
```sh
touch .env

#Didalam file .env
SECRET_KEY = "BEBASAJAINI" #Dapat diubah
ALGORITM = "HS256" #Dapat diubah selama valid
```
6. Run API dengan
```sh
python3 main.py
```
## Selesai!