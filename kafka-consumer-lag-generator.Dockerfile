FROM python:3.8
WORKDIR /kafka
RUN pip install confluent-kafka
COPY consumer.py .
COPY producer.py .
#CMD [ "/kafka/consumer.py" ]

#CMD [ "/kafka/producer.py" ]