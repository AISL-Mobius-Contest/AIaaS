from kafka import KafkaConsumer, KafkaProducer
from json import loads, dumps
import post

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
        msg = message.value
        msg_list = eval(msg)
        print(type(msg_list))
        cf = msg_list[0]["cf"]
        
        if cf == "humanDetection":
            section = msg_list[0]["section"]
            count = msg_list[0]["count"]
            data = {"section":section, "count": int(count)}
        
        elif cf == "visualLocalization":
            location = msg_list[0]["location"]
            data = {"location": int(location)}

        post.posting(cf,data)

