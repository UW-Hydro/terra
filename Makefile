export SHELL := /bin/bash

test:

	cp testing/matplotlibrc .
	py.test --doctest-modules
	rm matplotlibrc


coverage:

	cp testing/matplotlibrc .
	py.test --cover-erase --with-coverage --cover-html --cover-package terra
	rm matplotlibrc

lint:

	pyflakes -x W terra
	pep8 --exclude external terra

hexstrip:

	make -C examples hexstrip
