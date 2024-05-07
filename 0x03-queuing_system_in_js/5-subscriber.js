import redis from 'redis';

const client = redis.createClient();

client
  .on('error', (err) => console.log('Redis client not connected to the server:', err.message))
  .on('connect', () => console.log('Redis client connected to the server'));

const channel_name = 'holberton school channel';
client.subscribe(channel_name);

client.on('message', (channel, message) => {

  if (message === 'KILL_SERVER') {
    client.unsubscribe(channel_name);
    client.quit();
  } else {
    console.log(message);
  }
});
