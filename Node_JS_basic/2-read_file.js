const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n');
    const CheckLines = lines.filter((line) => line.trim() !== '');

    const students = CheckLines.slice(1);

    const fields = {};

    students.forEach(line => {
        const student = line.split(',');
        if (student.length === header.length) {
          const firstname = student[0].trim();
          const field = student[student.length - 1].trim();
          if (!fields[field]) {
            fields[field] = [];
          }
          fields[field].push(firstname);
        }
      });
    
      const totalStudents = students.length;
      console.log(`Number of students: ${totalStudents}`);
    
      for (const field in fields) {
        console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
      }
    }
    
    module.exports = countStudents;