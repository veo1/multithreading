import threading
import queue
import random
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

shared_queue = queue.Queue(maxsize=10)
lock = threading.Lock()
running_time = 10  # Program runtime in seconds

def producer():
    start_time = time.time()
    num = None  # Initialize num outside the loop, this allows us to keep the number if the queue is full and try again
    while time.time() - start_time < running_time:
        try:
            with lock:
                if not shared_queue.full():
                    if num is None:  # Generate a new number if num is None
                        num = random.randint(1, 100)
                    shared_queue.put(num)
                    logging.info(f"Produced: {num}")
                    num = None  # Reset num after putting it in the queue
                else:
                    logging.warning("Queue is full. Producer is waiting.")
        except Exception as e:
            logging.error(f"Error in producer: {e}")
        time.sleep(0.1)  # Producer delay

def consumer():
    start_time = time.time()
    while time.time() - start_time < running_time:
        try:
            with lock:
                if not shared_queue.empty():
                    num = shared_queue.get()
                    logging.info(f"Consumed: {num}")
                else:
                    logging.warning("Queue is empty. Consumer is waiting.")
        except Exception as e:
            logging.error(f"Error in consumer: {e}")
        time.sleep(0.15)  # Consumer delay

# Create producer and consumer threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

# Wait for both threads to complete
producer_thread.join()
consumer_thread.join()

print("Program finished.")
