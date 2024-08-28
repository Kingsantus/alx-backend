// Connect to the Redis server. Print a message on error or on successful connection

import { createClient } from 'redis';

const client = await createClient()
  .on('error', err => console.log('Redis client not connected to the server:', err))
  .on('connect', () => console.log('Redis client connected to the server'))
  .connect();

await client.disconnect();
