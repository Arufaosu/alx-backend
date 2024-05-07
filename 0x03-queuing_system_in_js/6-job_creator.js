import kue from 'kue';

const queue = kue.createQueue();

const object = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account'
};

const job = queue
  .create('push_notification_code', object)
  .save((err) => {
    if (!err) {
      console.log('Notification job created:', job.id);
    }
  });

job.on('complete', (result) => console.log('Notification job completed'))
  .on('failed', () => console.log('Notification job failed'));
