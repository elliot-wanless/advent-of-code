package main

import (
	"bufio"
	"fmt"
	"os"
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
