FROM python:3.9.1-buster

WORKDIR /root/LovelyRobot

COPY . .

RUN pip install -r requirements.txt

CMD ["python3","-m","LovelyRobot"]
