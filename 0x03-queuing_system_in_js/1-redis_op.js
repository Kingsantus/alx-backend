#!/usr/bin/node
// Connect to the Redis server. Print a message on error or on successful connection

import { createClient } from 'redis';

async function setNewSchool(schoolName, value) {
  await client.set(schoolName, value);
  console.log('success');
}

async function displaySchoolValue(schoolName) {
  const val = await client.get(schoolName);
  console.log(val);
}

const client = await createClient()
  .on('error', err => console.log('Redis client not connected to the server:', err))
  .on('connect', () => console.log('Redis client connected to the server'))
  .connect();

await setNewSchool('HolbertonSanFrancisco', '100');
await displaySchoolValue('HolbertonSanFrancisco');

await client.disconnect();
