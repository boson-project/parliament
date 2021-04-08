ci: lint test

lint:
	flake8 parliament tests

test:
	python -m pytest -s -v --cov parliament tests/*test.py

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