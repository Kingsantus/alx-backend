#!/usr/bin/node
import Bull from "bull";
import sendNotification from "./6-job_processor.js";

class Message {
  constructor (phoneNumber, message) {
    this.phoneNumber = phoneNumber;
    this.message = message;
  }
}

// Create the queue
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

messages.process(sendNotification);

messages.add(new Message('123', 'hey'));
messages.add(new Message('999', 'Bonjour'));
