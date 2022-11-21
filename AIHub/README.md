# AIHub
AIHub is a hub with an artificial intelligence model. 

An external AI Enablers or an internal AI Enablers can upload the model.

## Visual Localization(Patch_NetVLAD)
1. If you run all_in_one.py for Visual localization, you will see if you want to download the pretrained model. At this time, select yes and download the model.  

2. After you run all_in_one.py, when the image file sent by the device changes the query image in the patchnetvlad directory, it continuously compares the features extracted from images in the database and transmits the indoor coordinate value of the highest similarity to Mobius

## HumanDetection(yolov5-crowdhuman)
If you will use only the Human Detection model separately, please check the README.md file inside the human detection folder.

When using AIHub Mgmt, you can set the paths in the detect.py code in the human Detection file and use them.
