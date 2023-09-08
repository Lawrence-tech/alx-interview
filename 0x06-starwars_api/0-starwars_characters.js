#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi.dev/api';

if (process.argv.length > 2) {
  request(`${API_URL}/films/${process.argv[2]}/`, (err, response, body) => {
    if (err) {
      console.error(err);
      return;
    }

    if (response.statusCode !== 200) {
      console.error(`Request failed with status code ${response.statusCode}`);
      return;
    }

    const charactersURLs = JSON.parse(body).characters;
    const characterPromises = charactersURLs.map(characterURL => {
      return new Promise((resolve, reject) => {
        request(characterURL, (characterErr, _, characterBody) => {
          if (characterErr) {
            reject(characterErr);
          } else {
            resolve(JSON.parse(characterBody).name);
          }
        });
      });
    });

    Promise.all(characterPromises)
      .then(characterNames => {
        console.log(characterNames.join('\n'));
      })
      .catch(allErr => {
        console.error(allErr);
      });
  });
} else {
  console.log('Please provide a Movie ID as a command-line argument.');
}
