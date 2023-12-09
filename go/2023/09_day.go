package main

import (
	"fmt"
	"strings"
)

var seq [][]string
var next_value, first_value int
var part_1_total, part_2_total int

func day09() {
	sequences := ReadFile("go/2023/inputs.txt")
	clean_sequence(sequences)

	for _, sequence := range seq {
		next_value, first_value = find(sequence)
		part_1_total += next_value
		part_2_total += first_value

	}

	fmt.Println("Part 1:", part_1_total)
	fmt.Println("Part 2:", part_2_total)
}

func clean_sequence(sequences []string) {
	for _, sequence := range sequences {
		seq = append(seq, (strings.Split(sequence, " ")))
	}
}

func find(sequence []string) (int, int) {
	var elements [][]int
	var sum, z_index int
	elements = append(elements, []int{})

	//convert them all to ints
	for i := 0; i < len(sequence); i++ {
		elements[0] = append(elements[0], convert_to_int(sequence[i]))
	}

	// build all elements
	for !contains_all_zeroes(elements[z_index]) {
		elements = append(elements, []int{})
		for i := 0; i < len(elements[z_index]); i++ {
			if i+1 < len(elements[z_index]) {
				elements[z_index+1] = append(elements[z_index+1], elements[z_index][i+1]-elements[z_index][i])
			}
		}
		z_index++
	}

	// sum them up for part 1
	for _, element := range elements {
		sum += element[len(element)-1]
	}

	// shove a zero on the bottom of the last element
	z_index = len(elements) - 1
	elements[z_index] = append([]int{0}, elements[z_index]...)
	z_index--

	// calculate first value for part 2
	for z_index > 0 {
		elements[z_index] = append([]int{elements[z_index][0] - elements[z_index+1][0]}, elements[z_index]...)
		z_index--
	}

	first := elements[0][0] - elements[1][0]

	return sum, first
}
