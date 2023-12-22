package main

import (
	"container/list"
	"fmt"
	"sort"
	"strconv"
	"strings"
)

// Check if any of the points overlap
func overlaps(a, b []int) bool {
	return max(a[0], b[0]) <= min(a[3], b[3]) && max(a[1], b[1]) <= min(a[4], b[4])
}

// Find the max of two numbers
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// Find the min of two numbers
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func calculateSupport(bricks [][]int) (map[int]map[int]struct{}, map[int]map[int]struct{}) {
	supports := make(map[int]map[int]struct{})
	supportedBy := make(map[int]map[int]struct{})

	// Initialize the maps
	for i := range bricks {
		supports[i] = make(map[int]struct{})
		supportedBy[i] = make(map[int]struct{})
	}

	// Calculate the support and supportedBy maps
	for j, upper := range bricks {
		for i, lower := range bricks[:j] {
			// Check the bottom z-index against the top z-index
			if overlaps(lower, upper) && upper[2] == lower[5]+1 {
				supports[i][j] = struct{}{}
				supportedBy[j][i] = struct{}{}
			}
		}
	}
	return supports, supportedBy
}

func calculateTotal(bricks [][]int, supports map[int]map[int]struct{}, supportedBy map[int]map[int]struct{}) int {
	total := 0

	// Find the bricks that are falling
	for i := range bricks {
		q := list.New()
		falling := make(map[int]struct{})

		// Find the bricks that are supported by only one brick
		for j := range supports[i] {
			if len(supportedBy[j]) == 1 {
				q.PushBack(j)
				falling[j] = struct{}{}
			}
		}
		falling[i] = struct{}{}

		// Find the bricks that are supported by the falling bricks
		for q.Len() > 0 {
			j := q.Remove(q.Front()).(int)
			for k := range supports[j] {
				// If the brick is not already falling and is supported by the falling bricks
				if _, ok := falling[k]; !ok {
					if subset(supportedBy[k], falling) {
						q.PushBack(k)
						falling[k] = struct{}{}
					}
				}
			}
		}

		total += len(falling) - 1
	}
	return total
}

// Check if a is a subset of b
func subset(a, b map[int]struct{}) bool {
	for i := range a {
		if _, ok := b[i]; !ok {
			return false
		}
	}
	return true
}

func day22() {
	var bricks [][]int

	lines := ReadFile("go/2023/inputs.txt")

	// Format the bricks
	for _, line := range lines {
		line = strings.Replace(line, "~", ",", -1)
		parts := strings.Split(line, ",")
		brick := make([]int, len(parts))
		for i, part := range parts {
			brick[i], _ = strconv.Atoi(part)
		}
		bricks = append(bricks, brick)
	}

	// Sort the bricks by the z-index
	sort.Slice(bricks, func(i, j int) bool {
		return bricks[i][2] < bricks[j][2]
	})

	// Calculate the max z-index for each brick
	for index, brick := range bricks {
		maxZ := 1
		for _, check := range bricks[:index] {
			if overlaps(brick, check) {
				maxZ = max(maxZ, check[5]+1)
			}
		}
		brick[5] -= brick[2] - maxZ
		brick[2] = maxZ
	}

	// Sort the again bricks but by the max z-index
	sort.Slice(bricks, func(i, j int) bool {
		return bricks[i][2] < bricks[j][2]
	})

	supports, supportedBy := calculateSupport(bricks)
	total := calculateTotal(bricks, supports, supportedBy)

	fmt.Println(total)
}
