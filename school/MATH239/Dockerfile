FROM python:3.7-stretch

COPY . /src
WORKDIR /src

RUN pip install poetry==1.0.0 && poetry config virtualenvs.create false && poetry install

CMD jupyter notebook --allow-root --ip=0.0.0.0 --NotebookApp.token=''
