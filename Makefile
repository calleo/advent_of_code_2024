test:
	pipenv run pytest -s

format:
	pipenv run black .

lint:
	pipenv run black . --check && pipenv run flake8
