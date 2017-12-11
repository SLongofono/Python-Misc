"""
This demonstrates the use of asynchronous pools of workers using the multiprocessing
module.  Due to some unfortunate choices on the back end, anonymous functions and 
closures will not work.  Similar constraints apply to the pool.map() construct.  Things
like logging and shared queues are built in to the module, but trying to use decorators
for timing or tracking is out.  Here, I hack together a workaround to time and track
the PID for some simple worker processes.

Another note of interest is that multiprocessing may create a new process, or not.
Per the documentation, we can't assume a unique process for each.
"""

import multiprocessing
import time
import os

# Costly function for each process to compute
def dowork(num):
  if num < 0:
    raise
  if num <= 1:
    return 1
  return dowork(num-1) + dowork(num-2)
  
# Multiprocessing uses pickling to pass around functions, which
# presents a problem: the built-in pickle module will not support
# anonymous functions (lambda f) or closures (functions bound at
# runtime using decorators or other attributes).  To get extra
# functionality, we need to nest a series of functions which
# do not depend on out of context values
def pidwrapper(num):
print("Process {} starting".format(os.getpid()))
result = dowork(num)
print("Process {} ending".format(os.getpid()))
return result

if __name__ == "__main__":

# Sequential list for generating fibbonacci sequence
myList = range(30)

# Generates a pool of 30 workers
myPool = multiprocessing.Pool(processes=30)

# sets up and automatically starts a worker for each number
#output = pool.map(dowork, myList)

# sets up an automatically starts a worker for each number, returning results
# as they arrive
results = [myPool.apply_async(pidwrapper, (num,)) for num in myList]

# The get will raise an exception if the result is not ready.  We can use
# this to check it and move on if the result is not ready.

done = False

visited = [0 for x in myList]

finalList = [0 for x in myList]

start = time.time()

while not done:
  try:
    for i in range(len(visited)):
      if not visited[i]:
        print("Fibonacci number: {}\n\tfinished in: {} seconds\n\tResult: {}".format(i, time.time()-start, results[i].get(timeout=1)))
      visited[i] = 1
      finalList[i] = results[i].get()
    done = True
  except multiprocessing.TimeoutError:
    pass
    # The result is still being computed, move on to something else.

print(finalList)
