import base64

def decode(imgstring,section):
    imgdata = base64.b64decode(imgstring)
    filename = '{filepath}'+'/'+section+'.jpg' 
    with open(filename, 'wb') as f:
        f.write(imgdata)

    return filename