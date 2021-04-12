ci: lint test

lint:
	flake8 parliament tests

test:
	coverage run --source parliament -m pytest -s tests/*test.py
	coverage run --source parliament -a -m pytest -s tests/http/*test.py
	coverage run --source parliament -a -m pytest -s tests/event/*test.py
	coverage report -m

publish-test:
	python setup.py sdist bdist_wheel
	twine check dist/*
	twine upload --repository testpypi dist/*
	@echo
	@echo -e "\033[1;32mPublished to testpypi repository. To install the test package run:\033[0m"
	@echo "python3 -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple parliament-functions"
	@echo
	@echo -e "\033[1;32mTo publish the package run:\033[0m"
	@echo twine upload dist/\*