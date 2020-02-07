.PHONY: run
run:
	xhost +
	docker run --rm -it -v $(PWD):/src -w /src -v /tmp/.X11-unix:/tmp/.X11-unix:ro -e DISPLAY=$DISPLAY -p 8888:8888 pcap

.PHONY: build
build:
	docker build . -t pcap
