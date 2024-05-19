test-cov:
	coverage run -m pytest

	coverage html

	coverage report