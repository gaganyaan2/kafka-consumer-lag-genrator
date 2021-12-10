# Simple kafka-consumer-lag-genrator

### How it works?

- Once we run the producer.py it creates 100 messages in test1 topic
- When we run consumer.py it reads the message(**enable.auto.commit=true**) one by one with 1 second delay.
- As it's consumes message with **enable.auto.commit=true** every second the offset is changed.
- for example after 10 seconds consumer offset will be 10 and consumer lag will be 90.

### Run

```bash
producer.py --server kafka:9092 --topic topic1 --messages 100 --sleep 0

consumer.py --server kafka:9092 --consumer_group group1 --topic topic1 --messages 100 --sleep 1
```

### How we can fix consumer lag?

- By creating multiple consumer
- increase RAM/CPU of broker instance
- increase the partitions

## Motivation

There was no code available for kafka consumer lag genrator also faced a lot dependencies issues while creating lag.

## Refrences:
- https://stackoverflow.com/questions/52695164/how-to-fix-kafka-consumer-lag-in-0-10-2-1-kafka
- https://stackoverflow.com/questions/55569001/kafka-reduce-lag-for-consumer
- https://docs.confluent.io/clients-confluent-kafka-python/current/overview.html