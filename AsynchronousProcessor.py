

def processAsynchronously(workerName,queue):
   while(1):
     stream= queue.get(block=True)
     print(stream)
