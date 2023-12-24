package main

import (
	"fmt"
	"strconv"
	"strings"
)

type Hailstone struct {
	sx, sy, sz, vx, vy, vz float64
}

// Create a new hailstone with the given position and velocity.
func NewHailstone(sx, sy, sz, vx, vy, vz float64) Hailstone {
	return Hailstone{
		sx: sx, sy: sy, sz: sz, vx: vx, vy: vy, vz: vz,
	}
}

// Get the hailstones and format them
func parseHailstones(input []string) []Hailstone {
	var hailstones []Hailstone
	for _, line := range input {
		// Convert each position and velocity to a float
		parts := strings.Split(strings.ReplaceAll(strings.ReplaceAll(line, "@", ","), " ", ""), ",")
		sx, _ := strconv.ParseFloat(parts[0], 64)
		sy, _ := strconv.ParseFloat(parts[1], 64)
		sz, _ := strconv.ParseFloat(parts[2], 64)
		vx, _ := strconv.ParseFloat(parts[3], 64)
		vy, _ := strconv.ParseFloat(parts[4], 64)
		vz, _ := strconv.ParseFloat(parts[5], 64)
		
		// Add it to the hailstones
		hailstones = append(hailstones, NewHailstone(sx, sy, sz, vx, vy, vz))
	}
	return hailstones
}

func calculateIntersections(hailstones []Hailstone) int {
	total := 0
	// For each pair of hailstones, find the intersection and check if it's valid
	for i, hs1 := range hailstones {
		for _, hs2 := range hailstones[i+1:] {
			x, y := findIntersection(hs1, hs2)
			if isValidIntersection(x, y, hs1, hs2) {
				total++
			}
		}
	}
	return total
}

// Find the intersection of two hailstones
func findIntersection(hs1, hs2 Hailstone) (float64, float64) {
	a1, b1, c1 := hs1.vy, -hs1.vx, hs1.vy*hs1.sx-hs1.vx*hs1.sy
	a2, b2, c2 := hs2.vy, -hs2.vx, hs2.vy*hs2.sx-hs2.vx*hs2.sy
	x := (c1*b2 - c2*b1) / (a1*b2 - a2*b1)
	y := (c2*a1 - c1*a2) / (a1*b2 - a2*b1)
	return x, y
}

// Check if the intersection is valid
func isValidIntersection(x, y float64, hs1, hs2 Hailstone) bool {
	// Check if the intersection is within the bounds of the hailstones
	return 200000000000000 <= x && x <= 400000000000000 && 200000000000000 <= y && y <= 400000000000000 &&
		(x-hs1.sx)*hs1.vx >= 0 && (y-hs1.sy)*hs1.vy >= 0 && (x-hs2.sx)*hs2.vx >= 0 && (y-hs2.sy)*hs2.vy >= 0
}

func day24() {
	input := ReadFile("go/2023/inputs.txt")
	hailstones := parseHailstones(input)
	total := calculateIntersections(hailstones)
	fmt.Println(total)
}
