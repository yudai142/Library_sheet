開発環境でflaskを起動する
FLASK_APP=books.py FLASK_ENV=development pipenv run flask run

データベースの追加方法
export FLASK_APP=books.py
export FLASK_ENV=development
flask db init
flask db migrate -m"first setup"
flask db upgrade


requirementsテキストにpipenvのライブラリを書き込む
pipenv lock -r > requirements.txt

requirementsテキストからpipenvにライブラリを書き込む
pipenv install -r ./requirements.txt