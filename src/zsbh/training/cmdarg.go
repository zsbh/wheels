package training

import (
	"fmt"
	"os"
)

func cmdarg() {
	var args = os.Args
	str, sep := "", ""
	for i := 1; i < len(args); i++ {
		str += sep + args[i]
		sep = " "
	}
	fmt.Println(str)
}
