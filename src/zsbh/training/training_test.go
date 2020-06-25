package training

import (
	"fmt"
	"testing"
)

func TestTraining(t *testing.T) {
	var a = 23
	var b, c = a, 4
	var b1, b2 int = b, c
	// var c1 float64, d1 int = 23.3, 45 // syntax error
	// c1 float64, d1 int := 23.3, 45 // syntax error
	fmt.Println(b1, b2)
	genImage()
}