package main

import (
	"fmt"
	"strings"
)

var opponent, hand, mutated_hand string
var total_score, game_score, hand_score int

type Map struct {
	points int
	win    string
	lose   string
}

var mappings map[string]Map

func day02() {
	//PART 2 MAPPINGS
	mappings = map[string]Map{
		"A": {1, "B", "C"},
		"B": {2, "C", "A"},
		"C": {3, "A", "B"},
	}
	games := ReadFile("go/2022/inputs.txt")

	for _, game := range games {
		formatGame := strings.Split(game, " ")
		opponent = formatGame[0]
		hand = formatGame[1]
		mutated_hand = mutateHand(opponent, hand)
		fmt.Println(opponent, mutated_hand)
		game_score = getScoreForGame(opponent, mutated_hand)
		hand_score = mappings[mutated_hand].points
		total_score += (game_score + hand_score)
	}
	fmt.Println(total_score)

}

func mutateHand(opponent string, hand string) string {
	switch hand {
	case "X":
		return mappings[opponent].lose
	case "Y":
		return opponent
	default:
		return mappings[opponent].win
	}
}

func getScoreForGame(opponent string, shape string) int {
	switch shape {
	case mappings[opponent].win:
		return 6
	case mappings[opponent].lose:
		return 0
	default:
		return 3
	}
}
