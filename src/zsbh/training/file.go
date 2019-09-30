package training

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

func dupLine(f *os.File, counts map[string]int) {
	input := bufio.NewScanner(f)
	for input.Scan() {
		counts[input.Text()]++
	}
}

func dupLineForData(data string, counts map[string]int) {
	for _, line := range strings.Split(data, "\n") {
		counts[line]++
	}
}

func file() {
	counts := make(map[string]int)
	//input := bufio.NewScanner(os.Stdin)
	files := os.Args[1:]
	for _, arg := range files {
		data, err := ioutil.ReadFile(arg)
		if err != nil {
			fmt.Fprintf(os.Stderr, "dup file: %v\n", err)
		} else {
			dupLineForData(string(data), counts)

			for line, n := range counts {
				if n > 1 {
					fmt.Printf("file:%s  %d\t%s\n", arg, n, line)
				}
			}
		}
	}

}
