import threading
import queue

shared_queue = queue.Queue()

def producer():
    while True:
        item = threading.current_thread().getName()
        shared_queue.put(item)
        print(f"Produced by {item}")
        shared_queue.task_done()

def consumer():
    while True:
        item = shared_queue.get()
        if item is None:
            break
        print(f"Consumed by {threading.current_thread().getName()}")
        shared_queue.task_done()

def main():
    num_producers = int(input("Enter the number of producers: "))
    num_consumers = int(input("Enter the number of consumers: "))

    producer_threads = [threading.Thread(target=producer) for _ in range(num_producers)]
    consumer_threads = [threading.Thread(target=consumer) for _ in range(num_consumers)]

    for thread in producer_threads:
        thread.start()

    for thread in consumer_threads:
        thread.start()

    for thread in producer_threads:
        thread.join()

    for _ in range(num_consumers):
        shared_queue.put(None)

    for thread in consumer_threads:
        thread.join()

if __name__ == "__main__":
    main()
