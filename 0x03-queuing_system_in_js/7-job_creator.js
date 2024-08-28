#!/usr/bin/node
import Bull from "bull";

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

const messages = new Bull('messages');

// Called when a job is completed
messages.on('completed', (job, result) =>
  console.log(`Notification job completed: (id: ${job.id}), (result: ${result})`)
)

// Called when a job has been added to the queue
messages.on('waiting', (id) =>
  console.log('Notification job created:', id)
)

// Called when a job has failed
messages.on('failed', (job, error) =>
  console.log('Notification job failed:', error)
)

messages.on('progress', (job, progress) =>
  console.log(`Notification job ${progress}% complete`)
)

jobs.forEach(
  (job) => messages.add(job)
);
