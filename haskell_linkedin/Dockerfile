FROM haskell:latest

RUN apt-get update
RUN apt-get install git libgmp-dev xz-utils
RUN apt-get install -y libssl-dev ca-certificates libtinfo-dev authbind
RUN cabal update && cabal install stackage-update stackage-install && stackage-update
RUN useradd ghc
RUN adduser ghc sudo
USER ghc
WORKDIR /home/ghc

RUN stack setup
