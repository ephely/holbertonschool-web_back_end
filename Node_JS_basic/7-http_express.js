const express = require('express');
const fs = require('fs');
const app = express();

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const header = lines[0].split(',');
      const students = lines.slice(1);
      const fields = {};

      students.forEach((line) => {
        const parts = line.split(',');
        const firstname = parts[0];
        const field = parts[4];
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      });

      let output = `Number of students: ${students.length}\n`;
      for (const field in fields) {
        output += `Number of students in ${field}: ${
          fields[field].length
        }. List: ${fields[field].join(', ')}\n`;
      }

      resolve(output.trim());
    });
  });
}

// Serveur Express
app.get('/', (req, res) => {
  res.set('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  res.write('This is the list of our students\n');
  countStudents(process.argv[2])
    .then((data) => res.end(data))
    .catch((err) => res.end(err.message));
});

app.listen(1245);

module.exports = app;
