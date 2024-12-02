FROM ubuntu:latest
LABEL authors="joshu"

ENTRYPOINT ["top", "-b"]

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

#RUN pip install -r requirements.txt

COPY . /app

CMD ["ubuntu", "main.py"]
