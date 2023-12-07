const fs = require('fs');

const adventOfCode = (data) => {  
  const document = data.split("\n");
  
  //--PART 1--
  // const timeDistanceMap = document.map((line) => {
  //   return line.split(" ").filter((entry) => entry >= '0' && entry <= '9999999' && entry);
  // });

  //--PART 2
  const timeDistanceMap = document.map((line) => {
    line = line.split(" ");
    line.shift()
    return [line.filter((entry) => entry != '' && entry).reduce((partial, a) => partial + a, '')];
  });
  
  //--GENERAL--
  let recordMultiplication = 1;
  
  timeDistanceMap[0].forEach((time, index) => {
    let numberOfWinningCombos = 0;

    // 0 and the last is a losing combo
    for(let i=1; i<+time; i++) {
      const remainingTime = time - i;
      if(remainingTime*i > timeDistanceMap[1][index]) {
        numberOfWinningCombos++;
      }
    }
    recordMultiplication *= numberOfWinningCombos;
  })
  console.log(recordMultiplication);
}

const init = async () => {  
  fs.readFile(`src/inputs.txt`, 'utf8', (err, data) => {
    adventOfCode(data);
  });
}

init();
