#!/usr/bin/node
import Bull from "bull";
const blacklisted = ['4153518780', '4153518781'];

async function sendNotification(job, done) {
  job.progress(0);

  if (blacklisted.includes(job.data.phoneNumber)) {
    await done(new Error(`Phone number ${job.data.phoneNumber} is blacklisted`));
    return;
  }

  job.progress(50);
  console.log(
    `Sending notification to ${job.data.phoneNumber}, with message: ${job.data.message}`
  );
  done(null, 'ok');
}

const messages = new Bull('messages');

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
messages.process(2, sendNotification);
