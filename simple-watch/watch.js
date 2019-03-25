const fs = require('fs');
const path = require('path');

const file = `${path.dirname(__filename)}/data.json`;
const dataFile = file => JSON.parse(fs.readFileSync(file, 'utf8'));

fs.openSync(file, 'a');

fs.watchFile(file, (curr, prev) => {
  console.log('Arquivo alterado');
  console.log(dataFile(file));
});
