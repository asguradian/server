
from google.cloud import storage
from ParserUtility import *
from UploadFileUtility import  *
storage_client= storage.Client() 
def processAsynchronously(workerName,queue,bucketName):
   while(1):
    try: 
     stream= queue.get(block=True)
     imageByte= parseImage(stream.image)
     fileName=buildFileName(stream.date, stream.deviceId)
     bucket= storage_client.get_bucket(bucketName);
     print(fileName)
     uploadFile(storage_client,bucket,fileName,imageByte)
     print("Image successfully uploadded to the cloud storage bucket.")
    except: #// file cannot be upload at this moment
     print("Image cannot be uploaded right now")
    
    
     
