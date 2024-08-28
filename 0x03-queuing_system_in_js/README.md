# 0x03-queuing_system_in_js

# Files

## dump.rdb

Contains a dump file of a new database containing only the key-value pair `Holberton="School"

## 0-redis_client.js

Using Babel and ES6, write a script named `0-redis_client.js`. It should connect to the Redis server running on your machine:

- It should log to the console the message `Redis client connected` to the server when the connection to Redis works correctly
- It should log to the console the message `Redis client not connected to the server: ERROR_MESSAGE` when the connection to Redis does not work
- Connect to Redis using the `redis` package from npm

## 1-redis_op.js

In a file 1-redis_op.js, copy the code you previously wrote (0-redis_client.js).

Add two functions:

setNewSchool:
        It accepts two arguments schoolName, and value.
        It should set in Redis the value for the key schoolName
    displaySchoolValue:
        It accepts one argument schoolName.
        It should log to the console the value for the key passed as argument

At the end of the file, call:

    displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    displaySchoolValue('HolbertonSanFrancisco');

## 4-redis_advanced_op.js

Use `HSET` to store a hash value and `HGETALL` to retrieve the object stored.

## 5-subscriber.js, 5-publisher.js

In a file named `5-subscriber.js`, create a redis client:
- On connect, it should log the message `Redis client connected to the server`
- On error, it should log the message `Redis client not connected to the server: ERROR MESSAGE`
- It should subscribe to the channel `holberton school channel`
- When it receives message on the channel holberton school channel, it should log the message to the console
- When the message is `KILL_SERVER`, it should unsubscribe and quit

In a file named `5-publisher.js`, create a redis client:

- On connect, it should log the message `Redis client connected to the server`
- On error, it should log the message `Redis client not connected to the server: ERROR MESSAGE`
- Write a function named `publishMessage`:
  - It will take two arguments: `message` (string), and `time` (integer - in ms)
  - After `time` millisecond:
    - The function should log to the console `About to send MESSAGE`
    - The function should publish to the channel `holberton school channel`, the message passed in argument after the time passed in arguments
- At the end of the file, call:

  ```
publishMessage("Holberton Student #1 starts course", 100);
  publishMessage("Holberton Student #2 starts course", 200);
  publishMessage("KILL_SERVER", 300);
  publishMessage("Holberton Student #3 starts course", 400);
  ```

## 6-job_creator.js

Using `bull`, create a queue called `messages`

Jobs in the queue will have the following format:

```
{
  phoneNumber: string,
  message: string,
}
```
When the job is created without error, log to the console `Notification job created: JOB ID`
When the job is completed, log to the console `Notification job completed`
When the job is failing, log to the console `Notification job failed`

## 6-job_processor.js

Create a job processor that processes jobs from the queue defined in `6-job_creator.js`

Name the job-processing function `sendNotification`. It will log to the console `Sending notification to PHONE_NUMBER, with message: MESSAGE`

## 7-job_creator.js

Add jobs to a queue from an array

## 7-job_processor.js

Track progress of queued jobs
