#server
This python program acts a  consumer and subscribe to IoT core cloud on to a topic. When an image is received by the cloud, it is forwarded to the the subscriber, one of which is this program. Once it receives the image, it then adds it to the queue. There is a  asynchronous reader that reads the images from the  queue, create a compelling filename and using  google storage api, upload it to the cloud platform on to the specified bucket. For each device, the image is received from, it creates a folder inside the bucket and store the corresponding image on that folder.

To run this program, first this server must authenticate itself to the core IoT platform. Hence create service account and get the necessary credential as a json file. This a very sensitive file please do  not share it with anybody.

Export this file on the server  environment path to make is globally accesible.
```sh
$ export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/[FILE_NAME].json"
```
I have added other necessary files like google root CA file on the repository itself, so no need to do that.

Now we need to create a subscriber to out topic that we created on the cloud. Create a pull subscriber and remember its name(MY_TOPIC_SUBSCRIPTION).
Furthermore, go to the cloud storge platform and create a bucket and remember its name(BUCKET_NAME)

To run the program, run following script:
```sh
$ python server.py \
    --project_id=PROJECT_ID \
    --pubsub_subscription=MY_TOPIC_SUBSCRIPTION \
    --bk_name=BUCKET_NAME
```
