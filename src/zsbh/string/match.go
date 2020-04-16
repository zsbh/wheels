package string

func BFMatch(text, pattern string) int {
	//控制主串移动
	for i := 0; i < len(text); i++ {
		j := 0
		//控制模式串移动
		for j < len(pattern) {
			//失配则跳出
			if pattern[j] != text[i+j] {
				break
			}
			j++
		}
		//匹配成功则返回
		if j == len(pattern) {
			return i
		}
	}
	return -1
}

func KMPMatch(text, pattern string) int {
	// 预处理阶段，构造next数组

	next := make([]int, len(pattern))
	next[0] = -1
	for i := 0; i < len(pattern)-1; i++ {
		backIdx := i
		for backIdx >= 0 {
			if next[backIdx] == -1 || pattern[i] == pattern[next[backIdx]] {
				next[i+1] = next[backIdx] + 1
				//next数组通过添加第二个条件进行优化，将aaaaaa这种情况的回溯次数又进行优化。
				if i != 0 && pattern[i] == pattern[next[i]] {
					next[i] = next[next[i]]
				}
				break
			} else {
				backIdx = next[backIdx]
			}
		}
	}

	i := 0 //P的下标
	// Other
	pLen := len(pattern)
	j := -1 //相同前后缀的长度
	nextval := make([]int, pLen)
	nextval[0] = -1

	for i < pLen {
		if j == -1 || pattern[i] == pattern[j] {
			i++
			j++
			if i >= pLen {
				break
			}
			if pattern[i] != pattern[j] {
				nextval[i] = j
			} else {
				nextval[i] = nextval[j] //既然相同就继续往前找前缀
			}
		} else {
			j = nextval[j]
		}
	}

	//匹配阶段
	i = 0
	for i < len(text) {
		j := 0
		for len(text)-i >= len(pattern)-j && j >= 0 && j < len(pattern) {
			if text[i] == pattern[j] {
				j++
				i++
			} else {
				j = next[j]
			}
		}
		if j == len(pattern) {
			return i - j
		}
		i++
	}
	return -1
}

func PreBmGs() {

	//BCABABAB
	var i, j int
	var m int = 8
	var suff = []
	var bmGs [8]int

	// 先全部赋值为m，包含Case3
	for i = 0; i < m; i++ {
		bmGs[i] = m
	}

	// Case2
	j = 0
	for i = m - 1; i >= 0; i-- {
		if suff[i] == i+1 {
			for ; j < m-1-i; j++ {
				if bmGs[j] == m {
					bmGs[j] = m - i - 1
				}
			}
		}
	}
	//7 7 7 7 7 7 7 8

	// Case1
	for i = 0; i <= m-2; i++ {
		bmGs[m-1-suff[i]] = m - 1 - i
	}
	//7 7 7 2 7 4 7 1

}


func MAX(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func suffixes(x string) []int {
	var f, g, i int
	m := len(x)
	suff := make([]int, m)
	suff[m-1] = m
	g = m - 1
	for i = m - 2; i >= 0; i-- {
		if i > g && suff[i+m-1-f] < i-g {
			suff[i] = suff[i+m-1-f]
		} else {
			if i < g {
				g = i
			}
			f = i
			for g >= 0 && x[g] == x[g+m-1-f] {
				g--
			}
			suff[i] = f - g
		}
	}
	return suff
}

func preBmBc(x string, bmBc map[uint8]int) {
	var i int

	m := len(x)
	for i = 0; i < m-1; i++ {
		bmBc[x[i]] = m - i - 1
	}
}

func preBmGs(x string, bmGs []int) {
	var i, j int

	m := len(x)
	suff := suffixes(x)

	for i = 0; i < m; i++ {
		bmGs[i] = m
	}
	j = 0
	for i = m - 1; i >= 0; i-- {
		if suff[i] == i+1 {
			for ; j < m-1-i; j++ {
				if bmGs[j] == m {
					bmGs[j] = m - 1 - i
				}
			}
		}
	}

	for i = 0; i <= m-2; i++ {
		bmGs[m-1-suff[i]] = m - 1 - i
	}
}

func BM(y, x string) int {
	var i, j int
	bmGs := make([]int, len(x))
	bmBc := make(map[uint8]int)

	/* Preprocessing */
	preBmGs(x, bmGs)
	preBmBc(x, bmBc)

	m := len(x)
	n := len(y)
	/* Searching */
	getBc := func(c uint8) int {
		pos, ok := bmBc[c]
		if ok {
			return pos - m + 1 + i
		}
		return 1 + i
	}
	j = 0
	for j <= n-m {
		i = m - 1
		for i >= 0 && x[i] == y[i+j] {
			i--
		}
		if i < 0 {
			return j
		}
		j += MAX(bmGs[i], getBc(y[i+j]))
	}
	return -1
}

func maxSuffix(x string) []int {
	suff := make([]int, len(x))
	suff[len(x)-1] = len(x)
	for i := len(x) - 1; i >= 0; i-- {
		j := i
		for j >= 0 && x[j] == x[len(x)-1-(i-j)] {
			j--
		}
		suff[i] = i - j
	}
	return suff
} /*待优化*/

func preBc(x string) func(byte) int {
	bcMap := make(map[byte]int, len(x))
	for i := 0; i < len(x)-1; i++ {
		bcMap[x[i]] = len(x) - 1 - i
	}

	return func(c byte) int {
		v, ok := bcMap[c]
		if ok {
			return v
		}
		return len(x)
	}
}

func preGs(pattern string) []int {
	m := len(pattern)
	arr := make([]int, m)
	suff := maxSuffix(pattern)
	for i := 0; i < m; i++ {
		arr[i] = m
	}

	i := 0
	for j := m - 1; j >= 0 && suff[j] == j+1; j-- {
		for ; i < m-1-j && arr[i] == m; i++ {
			arr[i] = m - 1 - i
		}
	}

	for i = 0; i < m-1; i++ {
		arr[m-1-suff[i]] = m - 1 - i
	}

	return arr
}

func BMMatch(text, pattern string) int {
	bmBc := preBc(pattern)
	bmGs := preGs(pattern)
	m := len(pattern)
	n := len(text)

	i := 0
	for i <= n-m {
		j := m - 1
		for j >= 0 && pattern[j] == text[i+j] {
			j--
		}

		if j >= 0 {
			i += MAX(bmBc(text[i+j])-(m-1-j), bmGs[j])
		} else {
			return i
		}
	}
	return -1
}
