import kafka_module
import decoding
import subprocess
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from AIHub.Patch_NetVLAD import all_in_one

def AIHub_main(topic_name, cf):

    print("hello")
    print(cf)

    while True:
        msg = kafka_module.Consumer(topic_name)
        
        if cf == "humanDetection":
            section = msg[0]["section"]
            img = msg[0]["img"]
            
            img_path= decoding.decode(img,section)

            print(section+"connect")
            
            python_path = "python {filepath}/detect.py"
            subprocess.run(python_path + " --source " + img_path + " --device 3"+" --section "+section+" --cf "+cf+" --save-txt", shell=True)
  
        elif cf == "visualLocalization":
            img_path = msg[0]["img_path"]
            print("visualLocalization connect")
            all_in_one.main(img_path, cf)



