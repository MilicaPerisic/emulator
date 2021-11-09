import time
from time import sleep
import os
import base64
from kafka import KafkaProducer
import logging

logging.basicConfig(level=logging.INFO)


def load_images_from_folder(folder):
    read_images = []
    for filename in os.listdir(folder):
        image = open(os.path.join(folder, filename), "rb")
        image_read = image.read()
        read_images.append(image_read)
    return read_images

# load images from local directory
images = load_images_from_folder("sample_images")
producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])
processing_times_producer = []
topic = 'images'

# producer
for img in images:
    start_time = time.time()
    img_64_encode = base64.encodebytes(img)
    producer.send(topic, img_64_encode).get(timeout=30)
    processing_time_producer = time.time() - start_time
    processing_times_producer.append(processing_time_producer)
    # sleep(0.00001-processing_time)

# write processing time
p_file = open("producer_processing_time.txt", "w")
for element in processing_times_producer:
    p_file.write(str(element) + "\n")
p_file.close()

