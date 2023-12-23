package main

import (
	"fmt"
	"strings"
)

type Point struct {
	r, c int
}

// Map the directions to their respective points
var dirs = map[rune]Point{'^': {-1, 0}, 'v': {1, 0}, '<': {0, -1}, '>': {0, 1}}
var grid []string
var maxLength int

func day23() {
	grid = ReadFile("go/2023/inputs.txt")

	// Find the start and end points
	start := Point{0, strings.Index(grid[0], ".")}
	end := Point{len(grid) - 1, strings.Index(grid[len(grid)-1], ".")}
	visited := make([][]bool, len(grid))

	for i := range visited {
		visited[i] = make([]bool, len(grid[0]))
	}

	// Run DFS from the first point
	dfs(start, end, 0, visited)

	fmt.Println(maxLength)
}

func dfs(current, end Point, length int, visited [][]bool) {
	// If we are at the end point, check the length
	if current == end {
		if length > maxLength {
			maxLength = length
			// Prints part 2 answer after 20 seconds or so
			fmt.Println(maxLength)
		}
		return
	}

	// Set current to true
	visited[current.r][current.c] = true

	// For each direction, check if we can move there
	for _, dir := range dirs {
		// Find the new point
		newR, newC := current.r+dir.r, current.c+dir.c
		if newR >= 0 && newR < len(grid) && newC >= 0 && newC < len(grid[0]) && !visited[newR][newC] && grid[newR][newC] != '#' {
			// Uncomment this for Part 1 solution
			// if slope, ok := dirs[rune(grid[current.r][current.c])]; ok {
			// 	if slope != dir {
			// 		continue
			// 	}
			// }

			// Add one to the length and run DFS again
			dfs(Point{newR, newC}, end, length+1, visited)
		}
	}

	// Reset for the next path
	visited[current.r][current.c] = false
}
