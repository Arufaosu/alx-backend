import kue from 'kue';

export default function createPushNotificationsJobs(jobs, queue) {
  
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((data) => {

    const job = queue.create('push_notification_code_3', data)
    job.save((err) => {
      if (!err) {
        console.log(`Notification job created: ${job.id}`);
      }
    });

    job.on('progress', (progress) => console.log(`Notification job ${job.id} ${progress}% complete`))
      .on('failure', (error) => console.log(`Notification job ${job.id} failed: ${error.message}`))
      .on('complete', () => console.log(`Notification job ${job.id} completed`));
  });
}
