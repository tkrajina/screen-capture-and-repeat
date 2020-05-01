GIT_PORCELAIN_STATUS=$(shell git status --porcelain)

mypy:
	mypy --strict .

check-all-committed:
	if [ -n "$(GIT_PORCELAIN_STATUS)" ]; \
	then \
	    echo 'YOU HAVE UNCOMMITTED CHANGES'; \
	    git status; \
	    exit 1; \
	fi

pypi-upload: mypy check-all-committed
	rm -Rf dist/*
	python setup.py sdist
	twine upload dist/*
