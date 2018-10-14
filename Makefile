init:
	pip3 install pipenv --upgrade
	pipenv install --dev

run_all:
    # replace this with something less...
	pipenv run ./run.py 1 1
	pipenv run ./run.py 1 2
	pipenv run ./run.py 2 1
	pipenv run ./run.py 2 2
	pipenv run ./run.py 3 1
	pipenv run ./run.py 3 2
	pipenv run ./run.py 4 1
	pipenv run ./run.py 4 2

test_all:
	pipenv run pytest
