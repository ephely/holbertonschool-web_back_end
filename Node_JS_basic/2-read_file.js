const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n');
    const CheckLines = lines.filter((line) => line.trim() !== '');

    const header = CheckLines[0].split(',');
    const students = CheckLines.slice(1);

    const fields = {};

    students.forEach((line) => {
      const parts = line.split(',');
      if (parts.length === header.length) {
        const firstname = parts[0].trim();
        const field = parts[parts.length - 1].trim();
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      }
    });

    const totalStudents = students.length;
    console.log(`Number of students: ${totalStudents}`);

    for (const field in fields) {
      console.log(
        `Number of students in ${field}: ${
          fields[field].length
        }. List: ${fields[field].join(', ')}`,
      );
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
