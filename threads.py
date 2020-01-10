import threading

NTHREADS=20

def my_thread(i):
    print("In thread %s", i)
    print("Thread %s finish", i)

def fac(N):
    if N == 0:
        return 1
    else:
        return N * fac(N-1)

def wrapper(X):
    print("Thread %d" % X)
    print("Result %d... of thread %d" % (fac(X), X))
    return
    

simplethread=[]
for i in range(NTHREADS):
    simplethread.append(threading.Thread(target=wrapper, args=[i+1]))
    simplethread[-1].start()

for i in range(NTHREADS):
    simplethread[i].join()


print("End")
