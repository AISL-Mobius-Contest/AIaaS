from kafka import KafkaConsumer, KafkaProducer
from json import loads, dumps
import time
import os

def Producer(topic_name, data):
    producer = KafkaProducer(acks=0, compression_type='gzip', bootstrap_servers=['{Kafka IP & Port}'], value_serializer=lambda x: dumps(x).encode('utf-8'))
    producer.send(topic_name,value=data)
    producer.flush()


def Consumer(topic_name):
    print('Started. , pid : ',os.getpid(),' ppid : ',os.getppid())

    consumer = KafkaConsumer(
        topic_name,
        bootstrap_servers=['{Kafka IP & Port}'],
        auto_offset_reset='latest',
        enable_auto_commit=True,
        value_deserializer=lambda x: loads(x.decode('utf-8')),
        consumer_timeout_ms=100000000
    )


    for message in consumer:

        msg = message.value
        msg_list = eval(msg)
        
        return msg_list
