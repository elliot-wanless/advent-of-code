const fs = require('fs');

const adventOfCode = (data) => {
  //make engine matrix into 3D array
  const engineMatrix = data.split("\n").map(row => row.split(""));
  let total = 0;
  let matrixLength = engineMatrix.length;
  let rowLength = engineMatrix[0].length;
  let gearTotal = 0;
  //for every row in the matrix
  for(let i = 0; i < engineMatrix.length; i++) {
    //for every char in the matrix row
    let currentNumber = "";
    let partNumber = false;

    /** PART ONE */
    for(let j = 0; j < engineMatrix[i].length; j++) {
      while(j<rowLength && engineMatrix[i][j] >= '0' && engineMatrix[i][j] <= '9') {
        currentNumber += engineMatrix[i][j];
        //check above
        if((i > 0 && j > 0 && engineMatrix[i-1][j-1] != ".") ||
          (i > 0 && engineMatrix[i-1][j] != ".") ||
          (i > 0 && j < rowLength - 1 && engineMatrix[i-1][j+1] != ".") ||
        //check same row
          (j > 0 && engineMatrix[i][j-1] != "." && !(engineMatrix[i][j-1] >= '0' && engineMatrix[i][j-1] <= '9')) ||
          (j > 0 && j < matrixLength -1 && engineMatrix[i][j+1] != "." && !(engineMatrix[i][j+1] >= '0' && engineMatrix[i][j+1] <= '9')) ||
        //check below
          (i < matrixLength - 1 && j > 0 && engineMatrix[i+1][j-1] != ".") ||
          (i < matrixLength - 1 && engineMatrix[i+1][j] != ".") ||
          (i < matrixLength - 1 && j < rowLength - 1 && engineMatrix[i+1][j+1] != ".")
        ) {
          partNumber = true;
        }
        j++;
      }

      const searchAndDestroy = (i, j) => {
        let newI = i;
        let newJ = j+1;
        let number = "";

        //add initial number
        number += engineMatrix[i][j];
        
        //remove the number from the matrix
        engineMatrix[i][j] = ".";
        //search right
        while(newJ<rowLength && engineMatrix[newI][newJ] >= '0' && engineMatrix[newI][newJ] <= '9') {
          number += engineMatrix[newI][newJ];
          engineMatrix[newI][newJ] = ".";
          newJ++;
        }

        //reset coordinates
        newJ = j-1;
        newI = i;
        //search left
        while(newJ>=0 && engineMatrix[newI][newJ] >= '0' && engineMatrix[newI][newJ] <= '9') {
          number = engineMatrix[newI][newJ] + number;
          engineMatrix[newI][newJ] = ".";
          newJ--;
        }

        return +number;
      }

      let gearRatio = 1;
      let count = 0;

      //get the gear ratio when we find a gear
      if(engineMatrix[i][j] === "*") { //search and destroy, baby!
        engineMatrix[i][j] = "."; //remove the gearing to it's not re-processed afterwards

        //check all directions
        if(i > 0 && j > 0 && engineMatrix[i-1][j-1] != ".") {
          gearRatio *= searchAndDestroy(i-1, j-1);
          count++;
        }
        if(i > 0 && engineMatrix[i-1][j] != ".") {
          gearRatio *= searchAndDestroy(i-1, j);
          count++;
        }
        if(i > 0 && j < rowLength - 1 && engineMatrix[i-1][j+1] != ".") {
          gearRatio *= searchAndDestroy(i-1, j+1);
          count++;
        }
        if(j > 0 && engineMatrix[i][j-1] != ".") {
          gearRatio *= searchAndDestroy(i, j-1);
          count++;
        }
        if(j > 0 && j < rowLength -1 && engineMatrix[i][j+1] != ".") {
          gearRatio *= searchAndDestroy(i, j+1);
          count++;
        }
        if(i < matrixLength - 1 && j > 0 && engineMatrix[i+1][j-1] != ".") {
          gearRatio *= searchAndDestroy(i+1, j-1);
          count++;
        }
        if(i < matrixLength - 1 && engineMatrix[i+1][j] != ".") {
          gearRatio *= searchAndDestroy(i+1, j);
          count++;
        }
        if(i < matrixLength - 1 && j < rowLength - 1 && engineMatrix[i+1][j+1] != ".") {
          gearRatio *= searchAndDestroy(i+1, j+1);
          count++;
        }

        //if the gear has more than one number connected, add it
        if(count > 1) {
          gearTotal += gearRatio; 
        }

        //reset the gearing and count
        gearRatio = 1;
        count = 0;
      }
      console.log(gearTotal);

      //for part one
      if(partNumber){
        total += +currentNumber;
      }
      currentNumber = "";
      partNumber = false;
    }
  }
}

const init = async () => {  
  fs.readFile(`src/inputs.txt`, 'utf8', (err, data) => {
    adventOfCode(data);
  });
}

init();
