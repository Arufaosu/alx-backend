import redis from 'redis';

const client = redis.createClient();

client
  .on('error', (err) => console.log('Redis client not connected to the server:', err.message))
  .on('connect', () => console.log('Redis client connected to the server'));

function displaySchoolValue(schoolName) {
  client.get(schoolName, (error, value) => {
    if (error) throw error;
    console.log(value);
  });
}

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
