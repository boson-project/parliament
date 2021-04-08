ci: lint test

lint:
	flake8 parliament tests

test:
	python -m pytest -s -v --cov parliament tests/*test.py

publish-test:
	python setup.py sdist bdist_wheel
	twine check dist/*
	twine upload --repository-url https://test.pypi.org/legacy/ dist/
	
