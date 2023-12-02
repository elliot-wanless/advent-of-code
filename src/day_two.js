const fs = require('fs');
const colours = {red: 12, green: 13, blue: 14};
let total = 0;
let numbersPerColour = {};
let roundMinimum = {red: 0, green: 0, blue: 0};
let power = 0;


const adventOfCode = (data) => {
  const array = data.split("\n");

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

    //split game into rounds
    const rounds = gameSplit[1].split(";");
    let possible = true;

    console.log("GAME NUMBER: ", gameNumber)
    for (let i = 0; i < rounds.length; i++) {
        //split round into array
        const roundArray = rounds[i].replace(/,/g, "").split(" ");
        roundArray.shift();

        roundArray.forEach((round, i) => {
            //if it's a number, add it to the array and check if it's the POWERRRRRRR
            if(round >= "0" && round <= "9") {
                let num = roundArray[i];
                let colour = roundArray[i + 1];
                numbersPerColour[colour] = num;

                if(+roundMinimum[colour] < +roundArray[i]) {
                    roundMinimum[colour] = +num;
                }
            }
        })

        for(const [key] of Object.entries(numbersPerColour)) {
            if(numbersPerColour[key] > colours[key]) {
                possible = false;
            }
        }
        
    }

    //set up the total power for part 2
    let runningTotal = 1;
    const {red, green, blue} = roundMinimum;
    if(red > 0) {
        runningTotal *= red;
    }
    if(green > 0) {
        runningTotal *= green;
    }
    if(blue > 0) {
        runningTotal *= blue;
    }
    power += runningTotal;

    //this is the total for part 1
    if(possible) {
        total += gameNumber;
    }

    //reset for the next round
    roundMinimum = {red: 0, green: 0, blue: 0};
    possible = true;
    numbersPerColour = {};
  })
  console.log(power);
}

const init = async () => {  
  fs.readFile(`src/inputs.txt`, 'utf8', (err, data) => {
    adventOfCode(data);
  });
}

init();
