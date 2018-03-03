test:
	coverage run  --source src -m pytest

html-coverage:
	coverage html
	open htmlcov/index.html

