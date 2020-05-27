.PHONY: run
run:
	docker run --rm -i -t -v $(PWD):/home/ghc -u ghc myhaskell /bin/bash

.PHONY: build
build:
	docker build . -t myhaskell

compile: test.hs
	docker run --rm -it -v $(PWD):/home/ghc -u ghc myhaskell stack ghc --dynamic test.hs
