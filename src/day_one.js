const fs = require('fs');
const numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];


const adventOfCode = (data) => {
  const array = data.split("\n");
  let count = 0;

  array.forEach((code) => {
    const codeArray = code.split("");
    let left = 0;
    let right = codeArray.length - 1;

    //was going to go down the twin pointer route but CBA lol
    let foundLeft = false;
    let foundRight = false;

    let leftDigit;
    let rightDigit;

    //approach from left
    while(!foundLeft) {
      numbers.forEach((number, index) => {
        let i = 0;
        while(i < number.length) {
          if(codeArray[left + i] === number[i]) {
            if(i === number.length - 1) {
              foundLeft = true;
              leftDigit = index + 1;
              break;
            }
            i++;
          } else {
            break;
          }
        } 
      });

      if(!foundLeft) {
        if(codeArray[left] >= '0' && codeArray[left] <= '9') {
          leftDigit = +codeArray[left];
          foundLeft = true;
        }
        else {
          left++;
        }
      } 
    }

    while(!foundRight) {
      numbers.forEach((number, index) => {
        let i = number.length - 1;
        while(i >= 0) {
          if(codeArray[right + i] === number[i]) {
            if(i === 0) {
              foundRight = true;
              rightDigit = index + 1;
              break;
            }
            i--;
          } else {
            break;
          }
        } 
      });
  
      if(!foundRight) {
        if(codeArray[right] >= '0' && codeArray[right] <= '9') {
          rightDigit = +codeArray[right];
          foundRight = true;
        } else {
          right--;
        }
      }
    }

    count += +(leftDigit.toString()+rightDigit.toString())
    console.log(count);
})};

const init = async () => {  
  fs.readFile(`src/inputs.txt`, 'utf8', (err, data) => {
    adventOfCode(data);
  });
}

init();
