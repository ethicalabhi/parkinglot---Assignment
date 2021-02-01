API End Points:
a. To park a vehicle : http://localhost:5000/park
b. To unpark a vehicle : http://localhost:5000/unpark
c. To get vehicle/parking info by providing either one : http://localhost:5000/info

Steps to execute the project:
    a. Assuming flask and django environment setup is done
    b. Make sure all packages installed in requirements.txt 
    c. Assuming Database named parkinglot is created
    d. Source/export the required environment variables like parking_lot_size
    e. Start the mongodb service and start the flask server
    f. Finally hit the endpoints 

Steps to run:
 -> Start the mongodb server
 -> start the flask server >> python3 run.py 
 
 
{"info":{"_postman_id":"4d33e702-df30-4e9a-bc4c-e1ffe2e3f1ab","name":"Parking_lot","schema":"https:\/\/schema.getpostman.com\/json\/collection\/v2.0.0\/collection.json"},"item":[{"name":"park a car","id":"fa50317f-66b2-4ce6-8df1-4617a2afd95d","request":{"method":"POST","header":[],"body":{"mode":"raw","raw":"{\n    \"carnumber\":\"AP123456\"\n}","options":{"raw":{"language":"json"}}},"url":"http:\/\/localhost:5000\/park"},"response":[]},{"name":"unpark a car","id":"c6d6d817-a658-4376-86ba-5ab660a61119","request":{"method":"POST","header":[],"body":{"mode":"raw","raw":"{\n    \"carnumber\":\"AP123456\"\n}","options":{"raw":{"language":"json"}}},"url":"http:\/\/localhost:5000\/unpark"},"response":[]},{"name":"vehicle info through car","id":"e414a81a-64fc-47e6-aa83-03858d241c75","request":{"method":"POST","header":[],"body":{"mode":"raw","raw":"{\n    \"carnumber\":\"AP123456\"\n}","options":{"raw":{"language":"json"}}},"url":"http:\/\/localhost:5000\/info"},"response":[]},{"name":"vehicle info through parking no.","id":"adb9a868-7376-4f56-94d9-1b8c9175141c","request":{"method":"POST","header":[],"body":{"mode":"raw","raw":"{\n    \"parkinglot\": 1\n}","options":{"raw":{"language":"json"}}},"url":"http:\/\/localhost:5000\/info"},"response":[]}]}
