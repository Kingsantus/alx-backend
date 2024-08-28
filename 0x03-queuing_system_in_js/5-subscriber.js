#!/usr/bin/node
import { createClient } from 'redis';

const subscriber = await createClient()
  .on('error', err => console.log('Redis client not connected to the server:', err))
  .on('connect', () => console.log('Redis client connected to the server'))
  .connect();

async function listener(msg, channel) {
  if (msg === 'KILL_SERVER') {
    await subscriber.unsubscribe('holberton school channel');
    await subscriber.disconnect();
  }
  else {
    console.log(`${channel}: ${msg}`);
  }
}

subscriber.subscribe('holberton school channel', listener);
