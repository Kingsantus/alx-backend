#!/usr/bin/node

export default async function sendNotification(job, done) {
  console.log(
    `Sending notification to ${job.data.phoneNumber}, with message: ${job.data.message}`
  );
  done(null, 'ok');
}
