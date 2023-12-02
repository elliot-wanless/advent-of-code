const fs = require('fs');

const adventOfCode = (data) => {
//   const array = data.split("\n");
}

const init = async () => {  
  fs.readFile(`src/inputs.txt`, 'utf8', (err, data) => {
    adventOfCode(data);
  });
}

init();
