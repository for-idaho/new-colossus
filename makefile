.PHONY=run

run: 
	pipenv shell FLASK_APP=newColossus.py flask run

dev:
	pipenv shell FLASK_APP=newColossus.py SECRET_KEY=abc123 STAGE=DEV flask run

init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock

test:
	coverage run  --source src -m pytest

html-coverage:
	coverage html
	open htmlcov/index.html

