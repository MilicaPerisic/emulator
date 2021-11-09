from kafka import KafkaConsumer
import time
import os
import base64
import logging

logging.basicConfig(level=logging.INFO)

# consumer
consumer = KafkaConsumer(
    'images',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='new-group',
    consumer_timeout_ms=1000)

processing_times_consumer = []

# save images to local directory
for msg in consumer:
    start_time = time.time()
    image_64_decode = base64.decodebytes(msg.value)
    image_result = open(os.path.join("processed_images", "img_decoded"+str(msg.offset)+".bmp"), 'wb')
    image_result.write(image_64_decode)
    processing_time_consumer = time.time() - start_time
    processing_times_consumer.append(processing_time_consumer)

# write processing time
c_file = open("consumer_processing_time.txt", "w")
for element in processing_times_consumer:
    c_file.write(str(element) + "\n")
c_file.close()
