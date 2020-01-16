'''import time
import threading


start = time.perf_counter()

def do_somethin(seconds):
    print(f'Sleeping {seconds} second.')
    time.sleep(seconds)
    print('Done Sleeping.')

threads = []
for _ in range(10):
    t = threading.Thread(target=do_somethin, args=[1.5,])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()
print(f'finished in {round(finish - start, 2)} second(s)')
'''
import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f"sleeping {seconds} second(s).")
    time.sleep(seconds)
    return f"done sleeping {seconds}"

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = [executor.submit(do_something, sec) for sec in secs]
    for f in concurrent.futures.as_completed(results):
        print(f.result())


finish = time.perf_counter()
print(f"finished in {finish - start} second(s)")