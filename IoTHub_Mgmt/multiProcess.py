from multiprocessing import Process
import kafka_module

def multiprocess(topic_name):
    p = Process(target= kafka_module.Consumer, args=(topic_name,))
    p.start()
