package main

import (
	"bufio"
	"container/list"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func overlaps(a, b []int) bool {
	return max(a[0], b[0]) <= min(a[3], b[3]) && max(a[1], b[1]) <= min(a[4], b[4])
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func calculateSupport(bricks [][]int) (map[int]map[int]struct{}, map[int]map[int]struct{}) {
	supports := make(map[int]map[int]struct{})
	supportedBy := make(map[int]map[int]struct{})
	for i := range bricks {
		supports[i] = make(map[int]struct{})
		supportedBy[i] = make(map[int]struct{})
	}

	for j, upper := range bricks {
		for i, lower := range bricks[:j] {
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
	for i := range bricks {
		q := list.New()
		falling := make(map[int]struct{})
		for j := range supports[i] {
			if len(supportedBy[j]) == 1 {
				q.PushBack(j)
				falling[j] = struct{}{}
			}
		}
		falling[i] = struct{}{}

		for q.Len() > 0 {
			j := q.Remove(q.Front()).(int)
			for k := range supports[j] {
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

func subset(a, b map[int]struct{}) bool {
	for k := range a {
		if _, ok := b[k]; !ok {
			return false
		}
	}
	return true
}

func day22() {
	file, _ := os.Open("go/2023/inputs.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var bricks [][]int
	for scanner.Scan() {
		line := scanner.Text()
		line = strings.Replace(line, "~", ",", -1)
		parts := strings.Split(line, ",")
		brick := make([]int, len(parts))
		for i, part := range parts {
			brick[i], _ = strconv.Atoi(part)
		}
		bricks = append(bricks, brick)
	}

	sort.Slice(bricks, func(i, j int) bool {
		return bricks[i][2] < bricks[j][2]
	})

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

	sort.Slice(bricks, func(i, j int) bool {
		return bricks[i][2] < bricks[j][2]
	})

	supports, supportedBy := calculateSupport(bricks)
	total := calculateTotal(bricks, supports, supportedBy)

	fmt.Println(total)
}
