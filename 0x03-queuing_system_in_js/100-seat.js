import express from 'express';
import kue from 'kue';
import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

const getAsync = promisify(client.get).bind(client);

function reserveSeat(number) {
  client.set('available_seats', number);
}

async function getCurrentAvailableSeats() {
  return await getAsync('available_seats');
}

reserveSeat(50);
let reservationEnabled = true;

const queue = kue.createQueue();
  
const app = express();

app.get('/available_seats', async (req, res) => {
  res.json({ 'numberOfAvailableSeats': await getCurrentAvailableSeats() });
});

app.get('/reserve_seat', (req, res) => {

  if (!reservationEnabled) {
    return res.json({ "status": "Reservations are blocked" });
  }

  const job = queue
    .create('reservation')
    .save((error) => {
      if (!error) {
        return res.json({ "status": "Reservation in process" });
      } else {
        return res.json({ "status": "Reservation failed" });
      }
    });

  job.on('complete', () => console.log(`Seat reservation job ${job.id} completed`))
    .on('failure', (error) => console.log(`Seat reservation job ${job.id} failed: ${error.message}`));
});

app.get('/process', (req, res) => {

  queue.process('reservation', async (job, done) => {

    const current_seats = await getCurrentAvailableSeats();

    if (current_seats === 0) {
      console.log('Error');
      return done(new Error('Not enough seats available'));
    }

    const updated_seats = current_seats - 1;
    reserveSeat(updated_seats);

    if (updated_seats === 0) {
      reservationEnabled = false;
    }

    return done();
  });

  return res.json({ "status": "Queue processing" });
});

app.listen(1245)
