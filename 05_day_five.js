const fs = require('fs');

const adventOfCode = (data) => {  
  const maps = data.split("\n\n");
  const seeds = maps[0].split(" ");
  seeds.shift();
  maps.shift();
  let currentLocation = 0;
  const seedLocations = {};
  let lowest = 0;

  //--PART 1--

  //for each seed, find the lowest location
  // seeds.forEach((seed, index) => {
  //   currentLocation = +seed;
  //   maps.forEach(map => {
  //     let foundMap = false;
  //     const mapRows = map.split("\n")
  //     mapRows.shift();
  //     mapRows.forEach(row => {
  //       row = row.split(" ");
  //       const destinationRange = +row[0];
  //       const startRange = +row[1];
  //       const rangeLength = +row[2];
  //       if(currentLocation < (startRange+rangeLength) && currentLocation >= startRange && !foundMap) {
  //         currentLocation = destinationRange + (currentLocation - startRange);
  //         foundMap = true;
  //       }
  //     })
  //   });
  //   seedLocations[index] = currentLocation;
  // });
  // lowest = Math.min(...Object.values(seedLocations));
  // console.log(lowest);

  //--PART 2--
  //THIS WAS WAAAAY TOO SLOW
  for(let j=0; j<seeds.length; j+=2) {
    console.log("SEED batch", j+1);
    for(let k=0; k<+seeds[j+1]; k++) {
      currentLocation = (+seeds[j]+k);
      maps.forEach(map => {
        let foundMap = false;
        const mapRows = map.split("\n")
        mapRows.shift();
        mapRows.forEach(row => {
          row = row.split(" ");
          const destinationRange = +row[0];
          const startRange = +row[1];
          const rangeLength = +row[2];
  
          if(currentLocation < (startRange+rangeLength) && currentLocation >= startRange && !foundMap) {
            currentLocation = destinationRange + (currentLocation - startRange);
            foundMap = true;
          }
        })
      });
      if(lowest === 0) {
        lowest = currentLocation;
      } else {
        lowest = Math.min(lowest, currentLocation);
      }
    }
  }
  console.log(lowest)
}

const init = async () => {  
  fs.readFile(`src/inputs.txt`, 'utf8', (err, data) => {
    adventOfCode(data);
  });
}

init();
