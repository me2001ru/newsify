FROM python:3.10-slim-buster

#ENV PYTHONUNBUFFERED 1
#RUN apt-get update && apt-get install nodejs -y

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install requests
RUN pip3 install BeautifulSoup4
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]
