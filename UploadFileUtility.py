

def uploadFile(storage_client,bucket,fileName,messageObject):
  blob = bucket.blob(fileName)
  blob.upload_from_string(messageObject,content_type="image/jpg")
