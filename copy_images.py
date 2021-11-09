import shutil
import os
from time import sleep
import time
source_dir = "sample_imgs"
target_dir = 'new_imgs'

file_names = os.listdir(source_dir)

for file_name in file_names:
    start_time = time.time()
    shutil.copy(os.path.join(source_dir, file_name), target_dir)
    processing_time_producer = time.time() - start_time
    print(processing_time_producer)
    sleep(0.00001-processing_time_producer)
