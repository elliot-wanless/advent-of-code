const fs = require('fs');

const adventOfCode = (data) => {
  const array = data.split("\n");
  let total = 0;
  const copies = {}; 

  array.map((game) => {
    //get game number
    let gameNumber = 0;
    const gameSplit = game.split(":");
    gameSplit[0].split("").map(char => {
        if(char >= '0' && char <= '9') {
            gameNumber += char;
        }
    });
    gameNumber = +gameNumber;
    console.log("CARD NUMBER: ", gameNumber)


    //split game into rounds
    let gameTotal = 0;
    let count = 0;
    const numbers = gameSplit[1].split("|");
    const winningNumbers = numbers[0].split(" ").filter(number => number != "");
    const myNumbers = numbers[1].split(" ").filter(number => number != "");

    //add the initial card
    if(!copies[gameNumber]) {
      copies[gameNumber] = 1;
    }
    winningNumbers.forEach(number => {
      if(myNumbers.includes(number)) {
        count++;
        //if not initalised, set to 1, otherwise double
        if(gameTotal === 0) {
          gameTotal += 1;
        } else {
          gameTotal *= 2;
        }
      }
      })
      for(let i = 1; i <= count; i++) {
        if(copies[gameNumber + i]) {
          //add a card for each copy of the previous card
          copies[gameNumber + i] += (1*copies[gameNumber]);
        } else {
          //if not initalised, set add the correct number of copies (minus the original)
          copies[gameNumber + i] = 1 + (1*copies[gameNumber]);
        }
      }
    total += gameTotal;
    const sumValues = Object.values(copies).reduce((a, b) => a + b, 0);
    
    //part 2 answer
    console.log(sumValues);
    //part 1 answer
    console.log(total);
  })

}

const init = async () => {  
  fs.readFile(`src/inputs.txt`, 'utf8', (err, data) => {
    adventOfCode(data);
  });
}

init();
