package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

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

func convert_to_int(value string) int {
	num, err := strconv.Atoi(value)
	if err != nil {
		fmt.Println(err)
	}
	return num
}

func contains_all_zeroes(arr []int) bool {
	for _, value := range arr {
		if value != 0 {
			return false
		}
	}
	return true
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
