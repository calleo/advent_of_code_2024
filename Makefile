test:
	pipenv run pytest

format:
	pipenv run black .

lint:
	pipenv run black . --check && pipenv run flake8
