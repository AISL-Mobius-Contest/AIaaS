from kafka import KafkaConsumer, KafkaProducer
from json import loads, dumps


def Producer(topic_name, data):
    producer = KafkaProducer(acks=0, compression_type='gzip', bootstrap_servers=['{Kafka IP & Port}'], value_serializer=lambda x: dumps(x).encode('utf-8')) 
    producer.send(topic_name,value=data)
    producer.flush()


def Consumer(topic_name):
    consumer = KafkaConsumer(
        topic_name,
        bootstrap_servers=['{Kafka IP & Port}'], 
        auto_offset_reset='latest',
        enable_auto_commit=True,
        value_deserializer=lambda x: loads(x.decode('utf-8')),
        consumer_timeout_ms=100000000
    )

    for message in consumer:
        print("Topic: %s, Partition: %d, Offset: %d, Key: %s, Value: %s" % (
            message.topic, message.partition, message.offset, message.key, message.value
        ))
