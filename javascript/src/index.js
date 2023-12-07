const fs = require('fs');

//PART 1 Ordering
// const order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'].reverse();

//PART 2 Ordering
const order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'].reverse();

const combos = {
  FIVE_OF_A_KIND: [],
  FOUR_OF_A_KIND: [],
  FULL_HOUSE: [],
  THREE_OF_A_KIND: [],
  TWO_PAIR: [],
  PAIR: [],
  HIGH_CARD: [],
}

const jokerCountCombo = (jokerCount, currentValue, i) => {
  let newValue = 0;
  //Add the joker amount to make it the highest possible combo
  switch(jokerCount) {
    case 5:
      //make it a five of a kind if 5 jokers present
      combos.FIVE_OF_A_KIND.push(i);
      return true;
    case 4:
      //make it a five of a kind if 4 jokers present (4 + remining)
      combos.FIVE_OF_A_KIND.push(i);
      return true;
    case 3:
      //make it four of a kind or a five of a kind
      newValue = currentValue+jokerCount;
      newValue === 5 ? combos.FIVE_OF_A_KIND.push(i) : combos.FOUR_OF_A_KIND.push(i);
      return true;
    case 2:
      //make it three of a kind or a four of a kind or five of a kind
      newValue = currentValue+jokerCount;
      if(newValue === 5) {
        combos.FIVE_OF_A_KIND.push(i);
      } else if(newValue === 4) {
        combos.FOUR_OF_A_KIND.push(i);
      } else {
        combos.THREE_OF_A_KIND.push(i);
      }
      return true;
    case 1:
      //make it two of a kind or a three of a kind or a four of a kind or five of a kind
      newValue = currentValue+jokerCount;
      if(newValue === 5) {
        combos.FIVE_OF_A_KIND.push(i);
      } else if(newValue === 4) {
        combos.FOUR_OF_A_KIND.push(i);
      } else if(newValue === 3) {
        combos.THREE_OF_A_KIND.push(i);
      } else {
        combos.PAIR.push(i);
      }
      return true;
    default:
      //do nothing for zero jokers or full house
      return false;
  }
}

const getHighestCombos = (map, i, jokerCount) => {
  let values = Object.values(map);
  //values = the amount of each card. Look at all of them for the highest combo.
  //jokerCountCombo will add the joker amount to make it the highest possible combo, otherwise return normal combo.
  if(values.includes(5)) {
    !jokerCountCombo(jokerCount, 5, i) && combos.FIVE_OF_A_KIND.push(i);
  } else if(values.includes(4)) {
    !jokerCountCombo(jokerCount, 4, i) && combos.FOUR_OF_A_KIND.push(i);
  } else if(values.includes(3) && values.includes(2)) {
    //J wont be included, so this makes it a real full house
    combos.FULL_HOUSE.push(i);
  } else if(values.includes(3)) {
    !jokerCountCombo(jokerCount, 3, i) && combos.THREE_OF_A_KIND.push(i);
  } else if(values.includes(2)) {
    const pairs = values.filter((value) => value === 2);
    if(pairs.length === 2) {
      //in this case, J can only be 1 or 0
      if(jokerCount === 1) {
        //with 1 joker, we can make it a full house
        combos.FULL_HOUSE.push(i);
      } else {
        //with no joker, it's just two pairs
        combos.TWO_PAIR.push(i);
      }
    } else {
      //it's just a pair or more with joker combos
      !jokerCountCombo(jokerCount, 2, i) && combos.PAIR.push(i);
    }
  } else {
    //high card is default, but joker combo can make it higher combo.
    !jokerCountCombo(jokerCount, 0, i) && combos.HIGH_CARD.push(i);
  }
}

const mapHand = (hand) => {
  const map = {};
  let jokerCount = 0;
  hand = hand.split("");
  hand.forEach((card) => {
    //don't count the Js (part 2), otherwise count each instance of the card
    if(card === "J") {
      jokerCount++;
    } else {
      map[card] ? map[card]++ : map[card] = 1;
    }
  })
  return { map, jokerCount };

}

const adventOfCode = (data) => {  
  const hands = data.split("\n").map((line) => {
    return line.split(" ");
  })

  //get highest combo for each hand
  hands.forEach((hand, i) => {
    const { map, jokerCount } = mapHand(hand[0], i);
    getHighestCombos(map, i, jokerCount);
  })

  //order combo by highest card
  const orderedHands =  Object.entries(combos).map(([,array]) => {
    const sorted = array.sort((a, b) => {
      let i = 0;
      const handA = hands[a][0];
      const handB = hands[b][0];

      //while the cards are the same, keep iterating
      while(order.indexOf(handA[i]) === order.indexOf(handB[i])) {
        i++;
      }
      return order.indexOf(handB[i]) - order.indexOf(handA[i]);
    })

    return sorted;
  });

  let count = 0;
  let totalWinnings = 0;

  //rank the hands (highest to lowest) and count winnings
  orderedHands.forEach((hand) => {
    if(hand.length > 0) {
      hand.forEach(index => {
        totalWinnings = totalWinnings + (hands[index][1] * (hands.length-count));
        count++;
      })
    }
  })
  console.log(totalWinnings);
}

const init = async () => {  
  fs.readFile(`src/inputs.txt`, 'utf8', (err, data) => {
    adventOfCode(data);
  });
}

init();
