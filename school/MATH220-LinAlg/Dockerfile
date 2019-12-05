FROM python:3.7-slim-stretch

RUN apt-get update && apt-get install -y python3-tk && apt-get clean && pip install --upgrade pip setuptools
RUN pip install sympy numpy ipython matplotlib

CMD ["bash"]

# docker build . -f Dockerfile-school -t pyschool
# xhost +
# docker run --rm -it -v ${PWD}:/src -v /tmp/.X11-unix:/tmp/.X11-unix:ro -w /src -e DISPLAY=$DISPLAY pyschool
