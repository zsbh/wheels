package string

func bmMatch(prim, mode string) int {
	for i := 0; i < len(prim) && len(prim)-i >= len(mode); i++ {
		j := 0
		for j < len(mode) {
			if mode[j] != prim[i+j] {
				break
			}
			j++
		}
		if j == len(mode) {
			return i
		}
	}
	return -1
}

func kmpMatch(prim, mode string) int {
	next := make([]int, len(mode))
	next[0] = -1

	//next数组
	for i := 1; i < len(mode); i++ {
		backIdx := i
		for backIdx > 0 {
			if mode[next[backIdx-1]] == mode[i-1] {
				next[i] = next[backIdx-1] + 1
			} else {
				backIdx = next[backIdx-1]
			}
		}
		next[i] = 0
	}

	//match
	i := 0
	for i < len(prim) {
		j := 0
		for j < len(mode) {
			if prim[i] == mode[j] {
				j++
				i++
			} else {
				if j == 0 {
					break
				} else {
					j = next[j]
				}
			}
		}
		if j == len(mode) {
			return i - j
		}
		i++
	}
	return -1
}
