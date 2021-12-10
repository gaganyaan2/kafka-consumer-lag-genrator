from confluent_kafka import Producer, KafkaError, KafkaException
from confluent_kafka.admin import AdminClient, NewTopic
import socket
import argparse
import time

# commnad
# producer.py --server kafka:9092 --topic topic1 --messages 100 --sleep 1

parser = argparse.ArgumentParser(description='kafka producer parameters')
parser.add_argument('--server', type=str,
                    help='kafka server with port eg. kafka:9092.')

parser.add_argument('--topic', type=str,
                    help='kafka topic name')

parser.add_argument('--messages', type=int,
                    help='number of messages needs to be produced.')

parser.add_argument('--sleep', type=float,
                    help='sleep between messages produced.')

args = parser.parse_args()

kafka_server = args.server
kafka_topic = args.topic
kafka_messages= args.messages
kafka_sleep = args.sleep

#need to write code for creating new kafka topic if not exsits

conf = {'bootstrap.servers': kafka_server,
        'client.id': socket.gethostname()}

producer = Producer(conf)
def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

for i in range(kafka_messages):
    producer.produce(kafka_topic, key="key", value="message"+str(i), callback=acked)
    producer.poll(1)
    print("messages sent:",i)
    time.sleep(kafka_sleep)

print(str(kafka_messages)+" messages has been sent to topic : "+kafka_topic)

while True:
    print("infinite sleep...")
    time.sleep(60)