.PHONY: run
run:
	docker run --rm -i -t -v $(PWD):/home/djustice -u djustice myhaskell /bin/bash

.PHONY: build
build:
	docker build . -t myhaskell

compile: test.hs
	docker run --rm -it -v $(PWD):/home/djustice -u djustice myhaskell stack ghc --dynamic test.hs
