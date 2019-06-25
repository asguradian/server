
from ParserUtility import *
def processAsynchronously(workerName,queue):
   while(1):
     stream= queue.get(block=True)
     imageByte= parseImage(stream.image)
     #fileName=buildFileName(stream.date, stream.deviceId)
     print(stream)
