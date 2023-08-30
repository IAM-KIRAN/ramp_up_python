import threading
import random

shared_list = []


def producer():
    added_item = random.randint(1, 1000)
    shared_list.append(added_item)
    print(f"Producer added {added_item} to the list")


def consumer():
    while True:
        if shared_list:
            poped_item = shared_list.pop()
            print(f"Consumer popped {poped_item} from the list")
        else:
            print("List is empty, nothing to pop.")
            break



def main():
    num_producers = int(input("Enter the number of producers: "))
    num_consumers = int(input("Enter the number of consumers: "))

    producer_threads = [threading.Thread(target=producer) for i in range(num_producers)]
    consumer_threads = [threading.Thread(target=consumer) for j in range(num_consumers)]

    for thread in producer_threads:
        thread.start()

    for thread in  consumer_threads:
        thread.start()

    for thread in producer_threads:
        thread.join()

    for thread in consumer_threads:
        thread.join()


main()
