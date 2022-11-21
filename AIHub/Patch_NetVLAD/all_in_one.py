import time

from AIHub.Patch_NetVLAD import feature_extract
from AIHub.Patch_NetVLAD import feature_match


def main(source, cf):
    while True:

        start = time.time()
        feature_extract.extracting(source)
        feature_match.matching(source, cf)
        end = time.time()
        
        print(" localization delay is")
        print(f"{end - start:.10f} sec")
    