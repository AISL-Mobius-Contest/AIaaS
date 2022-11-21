from multiprocessing import Process
import subscribe

def multiprocess(source):
    p = Process(target= subscribe.subscribing, args=(source,))
    p.start()
