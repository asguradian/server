
from google.cloud import storage
from ParserUtility import *
from UploadFileUtility import  *
storage_client= storage.Client() # get the google cloud storge client api 
# This method is  reads the the image from the specified queue, build the file name for the image and using the cloud strorage client api upload the image to the cloud for storage
# for each device, it creetes a separate folder and upload the image to that folder.
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
    
    
     
