from multiprocessing import Process
import main 

def multiprocess(topic_name, cf):
    p = Process(target= main.AIHub_main, args=(topic_name, cf))
    p.start()
