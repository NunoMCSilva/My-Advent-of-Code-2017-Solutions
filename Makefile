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
	pipenv run ./run.py 5 1
	pipenv run ./run.py 5 2
	pipenv run ./run.py 6 1
	pipenv run ./run.py 6 2
	pipenv run ./run.py 7 1
	pipenv run ./run.py 8 1
	pipenv run ./run.py 8 2
	pipenv run ./run.py 9 1
	pipenv run ./run.py 9 2
	pipenv run ./run.py 11 1
	pipenv run ./run.py 11 2
	pipenv run ./run.py 15 1
	pipenv run ./run.py 15 2
	pipenv run ./run.py 16 1
	pipenv run ./run.py 16 2
	pipenv run ./run.py 20 1
	pipenv run ./run.py 20 2

test_all:
	pipenv run pytest
