from confluent_kafka import Consumer, KafkaError, KafkaException
import sys
import time
import argparse

# commnad
# consumer.py --server kafka:9092 --consumer_group group1 --topic topic1 --messages 100 --sleep 1

parser = argparse.ArgumentParser(description='kafka consumer parameters')
parser.add_argument('--server', type=str,
                    help='kafka server with port eg. kafka:9092.')

parser.add_argument('--consumer_group', type=str,
                    help='consumer_group name.')

parser.add_argument('--topic', type=str,
                    help='kafka topic name.')

parser.add_argument('--messages', type=int,
                    help='number of messages needs to be consumed.')

parser.add_argument('--sleep', type=float,
                    help='sleep between messages consumed.')

args = parser.parse_args()

kafka_server = args.server
kafka_consumer_group = args.consumer_group
kafka_topic = args.topic
kafka_messages= args.messages
kafka_sleep = args.sleep

conf = {'bootstrap.servers': kafka_server,
        'group.id': kafka_consumer_group,
        'enable.auto.commit': True,
        'auto.offset.reset': 'earliest'}

consumer = Consumer(conf)

def msg_process(msg):
    print(f"key: {msg.key()}, value: {msg.value()}")

running = True

def kafka_consumer(consumer, kafka_topic):
    try:
        print("Consuming from kafka_topic: ",str(kafka_topic))
        consumer.subscribe([kafka_topic])
        count = 0
        while running:
            msg = consumer.poll(timeout=1.0)
            if msg is None: continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                print("message processing:")
                msg_process(msg)
                time.sleep(kafka_sleep)
                
                count = count + 1
                print("count :",count)
                if count == kafka_messages:
                    while True:
                        print("infinite sleep...")
                        time.sleep(60)

    finally:
        print("finally block")
        consumer.close()

#call kafka_consumer function
kafka_consumer(consumer,kafka_topic)