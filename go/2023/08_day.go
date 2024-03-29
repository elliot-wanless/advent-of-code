package main

import (
	"fmt"
	"strings"
)

type position struct {
	current string
	left    string
	right   string
}

var directions []string
var coordinateMap map[string]position
var directionCounter int
var steps int

func day08() {
	input := ReadFile("go/inputs.txt")
	directions = strings.Split(input[0], "")
	coordinateMap = make(map[string]position)
	currentPositions := make(map[string]position)

	currentPosition := position{}
	directionCounter = 0
	steps = 0

	for _, coordinate := range input[1:] {
		splitCoordinate := strings.Split(cleanCoordinate(coordinate), " ")
		key := splitCoordinate[0]
		coordinateMap[key] = position{key, splitCoordinate[1], splitCoordinate[2]}

		// PART 1
		if key == "AAA" {
			currentPosition = coordinateMap[key]
		}

		// PART 2
		if strings.Split(key, "")[2] == "A" {
			currentPositions[key] = coordinateMap[key]
		}
	}

	// PART 1
	for currentPosition.current != "ZZZ" {
		currentPosition = traverse(directions[directionCounter], currentPosition)
	}
	fmt.Println("PART 1:", steps)

	// PART 2
	var stepsList []int
	directionCounter = 0
	steps = 0

	for _, pos := range currentPositions {
		currentPosition = pos
		for strings.Split(currentPosition.current, "")[2] != "Z" {
			currentPosition = traverse(directions[directionCounter], currentPosition)

		}
		stepsList = append(stepsList, steps)
		directionCounter = 0
		steps = 0
	}
	LCM := LCM(stepsList[0], stepsList[1], stepsList[2:]...)
	fmt.Println("PART 2:", LCM)
}

func traverse(direction string, currentPosition position) position {
	directionCounter++
	if directionCounter == len(directions) {
		directionCounter = 0
	}
	steps++

	if direction == "L" {
		return coordinateMap[currentPosition.left]
	} else {
		return coordinateMap[currentPosition.right]
	}

}

func GCD(a, b int) int {
	for b != 0 {
		t := b
		b = a % b
		a = t
	}
	return a
}

func LCM(a, b int, integers ...int) int {
	result := a * b / GCD(a, b)

	for i := 0; i < len(integers); i++ {
		result = LCM(result, integers[i])
	}

	return result
}

func cleanCoordinate(coordinate string) string {
	coordinate = strings.ReplaceAll(coordinate, ",", "")
	coordinate = strings.ReplaceAll(coordinate, "(", "")
	coordinate = strings.ReplaceAll(coordinate, ")", "")
	coordinate = strings.ReplaceAll(coordinate, " =", "")
	return coordinate
}
