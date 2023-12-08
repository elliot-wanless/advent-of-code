package main

import (
	"fmt"
	"sort"
	"strconv"
)

var total_calories int
var elf_calories int
var top_three []int

func main() {
	inputs := ReadFile("go/inputs.txt")
	for _, input := range inputs {
		if input != "" {
			num, err := strconv.Atoi(input)
			if err != nil {
				fmt.Println(err)
				continue
			}
			elf_calories += num
		} else {
			total_calories = max(total_calories, elf_calories)
			updateTopThree(elf_calories)
			elf_calories = 0
		}
	}
	fmt.Println(total_calories)
	fmt.Println(sum(top_three))

}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func updateTopThree(num int) {
	// Check if num is already in top_three
	for _, value := range top_three {
		if value == num {
			return
		}
	}

	// Add num to top_three and sort it
	top_three = append(top_three, num)
	sort.Sort(sort.Reverse(sort.IntSlice(top_three)))

	// If top_three has more than 3 elements, remove the smallest one
	if len(top_three) > 3 {
		top_three = top_three[:3]
	}
}

func sum(arr []int) int {
	total := 0
	for _, value := range arr {
		total += value
	}
	return total
}
