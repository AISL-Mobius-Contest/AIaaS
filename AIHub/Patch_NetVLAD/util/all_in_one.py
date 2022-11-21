from feature_extract import extracting
from feature_match import matching
import time

if __name__ == "__main__":
    while True:
        start = time.time()
        extracting()
        matching()
        end = time.time()
        print(" localization delay is")
        print(f"{end - start:.10f} sec")