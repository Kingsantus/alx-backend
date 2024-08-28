#!/usr/bin/node
import { createClient } from "redis";

const client = await createClient()
.on('error', err => console.log('Redis client not connected to the server:', err))
.on('connect', () => console.log('Redis client connected to the server'))
.connect();

client.hSet('HolbertonSchools', 'Portland', '50');
client.hSet('HolbertonSchools', 'Seattle', '80');
client.hSet('HolbertonSchools', 'New York', '20');
client.hSet('HolbertonSchools', 'Bogota', '20');
client.hSet('HolbertonSchools', 'Cali', '40');
client.hSet('HolbertonSchools', 'Paris', '2');

await client.hGetAll('HolbertonSchools').then(
  (result) => console.log(result)
).catch(
  (error) => console.log('Error occured during HGETALL:', error)
);

await client.disconnect();
