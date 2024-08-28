#!/usr/bin/node
import { createClient } from 'redis';

const publisher = await createClient()
  .on('error', err => console.log('Redis client not connected to the server:', err))
  .on('connect', () => console.log('Redis client connected to the server'))
  .connect();

function publishMessage(message, time) {
  setTimeout(
    () => {
      console.log('About to send:',  message);
      publisher.publish('holberton school channel', message);
    }, time
  )
}

publishMessage("Holberton Student #1 starts course", 1000);
publishMessage("Holberton Student #2 starts course", 2000);
publishMessage("KILL_SERVER", 3000);
publishMessage("Holberton Student #3 starts course", 4000);

// await publisher.disconnect();
