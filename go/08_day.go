package main

import (
	"bufio"
	"fmt"
	"os"
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

func main() {
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

		//PART 2
		if strings.Split(key, "")[2] == "A" {
			currentPositions[key] = coordinateMap[key]
		}
	}

	//PART 1
	for currentPosition.current != "ZZZ" {
		currentPosition = traverse(directions[directionCounter], currentPosition)
	}
	fmt.Println("PART 1:", steps)

	directionCounter = 0
	steps = 0
	//PART 2
	var stepsList []int

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

// https://siongui.github.io/2017/06/03/go-find-lcm-by-gcd/
func GCD(a, b int) int {
	for b != 0 {
		t := b
		b = a % b
		a = t
	}
	return a
}

// https://siongui.github.io/2017/06/03/go-find-lcm-by-gcd/
func LCM(a, b int, integers ...int) int {
	result := a * b / GCD(a, b)

	for i := 0; i < len(integers); i++ {
		result = LCM(result, integers[i])
	}

	return result
}

func ReadFile(filename string) (file_array []string) {
	file, err := os.Open(filename)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		file_array = append(file_array, scanner.Text())
	}

	return
}

func cleanCoordinate(coordinate string) string {
	coordinate = strings.ReplaceAll(coordinate, ",", "")
	coordinate = strings.ReplaceAll(coordinate, "(", "")
	coordinate = strings.ReplaceAll(coordinate, ")", "")
	coordinate = strings.ReplaceAll(coordinate, " =", "")
	return coordinate
}
