init:
	pip3 install pipenv --upgrade
	pipenv install --dev

run_all:
	pipenv run ./run.py 1 1
	pipenv run ./run.py 1 2

test_all:
	pipenv run pytest
