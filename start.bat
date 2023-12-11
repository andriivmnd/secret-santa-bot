set dir="C:\Users\admin\Desktop\as"

cd /d %dir%

python -m venv venv
call "venv\Scripts\activate.bat"
pip install -r requirements.txt

python "main.py"

pause