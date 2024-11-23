build:
	poetry install

unittest:
	ENVIRONMENT=testing poetry run pytest tests

run-dev:
	ENVIRONMENT=development poetry run template_project

run-prod:
	ENVIRONMENT=production poetry run template_project