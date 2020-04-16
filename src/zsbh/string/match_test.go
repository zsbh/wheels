package string

import (
	"testing"
)

func TestBF(t *testing.T) {
	res := BFMatch("ADCBAACBDABCD", "CBA")
	if res == 2 {
		t.Log("SUCCESS: prim=ADCBAACBDABCD, mode=CBA")
	} else {
		t.Errorf("FAIL:  prim=ADCBAACBDABCD, mode=CBA, res=%d", res)
	}
	res = BFMatch("ADCBAACBDABCD", "ADC")
	if res == 0 {
		t.Log("SUCCESS: prim=ADCBAACBDABCD, mode=ADC")
	} else {
		t.Errorf("FAIL:  prim=ADCBAACBDABCD, mode=ADC, res=%d", res)
	}

	res = BFMatch("ADCBAACBDABCD", "ABCD")
	if res == 9 {
		t.Log("SUCCESS: prim=ADCBAACBDABCD, mode=ABCD")
	} else {
		t.Errorf("FAIL:  prim=ADCBAACBDABCD, mode=ABCD, res=%d", res)
	}

	res = BFMatch("ADCBAACBDABCD", "ABCCD")
	if res == -1 {
		t.Log("SUCCESS: prim=ADCBAACBDABCD, mode=ABCCD")
	} else {
		t.Errorf("FAIL:  prim=ADCBAACBDABCD, mode=ABCCD, res=%d", res)
	}
}

func TestKMP(t *testing.T) {
	res := KMPMatch("ADCBAACBDABCD", "CBA")
	if res == 2 {
		t.Log("SUCCESS: prim=ADCBAACBDABCD, mode=CBA")
	} else {
		t.Errorf("FAIL:  prim=ADCBAACBDABCD, mode=CBA, res=%d", res)
	}
	res = KMPMatch("ADCBAACBDABCD", "ADC")
	if res == 0 {
		t.Log("SUCCESS: prim=ADCBAACBDABCD, mode=ADC")
	} else {
		t.Errorf("FAIL:  prim=ADCBAACBDABCD, mode=ADC, res=%d", res)
	}

	res = KMPMatch("ADCBAACBDABCD", "ABCD")
	if res == 9 {
		t.Log("SUCCESS: prim=ADCBAACBDABCD, mode=ABCD")
	} else {
		t.Errorf("FAIL:  prim=ADCBAACBDABCD, mode=ABCD, res=%d", res)
	}

	res = KMPMatch("ADCBAACBDABCD", "ABCCD")
	if res == -1 {
		t.Log("SUCCESS: prim=ADCBAACBDABCD, mode=ABCCD")
	} else {
		t.Errorf("FAIL:  prim=ADCBAACBDABCD, mode=ABCCD, res=%d", res)
	}

	res = KMPMatch("ADCBAACBDABCDBAACBDAADCBAACBDABCDBAACBDA", "ACCCCCCCCCCCCCCCCCCCCCCCCCCD")
	if res == -1 {
		t.Log("SUCCESS: prim=ADCBAACBDABCDBAACBDAADCBAACBDABCDBAACBDA, mode=ACCCCCCCCCCCCCCCCCCCCCCCCCCD")
	} else {
		t.Errorf("FAIL:  prim=ADCBAACBDABCDBAACBDAADCBAACBDABCDBAACBDA, mode=ACCCCCCCCCCCCCCCCCCCCCCCCCCD, res=%d", res)
	}

	res = KMPMatch("ADCBAACBDABCDBAACBDAADCBAACBDABCDBAACBDA", "ABCDABD")
	if res == -1 {
		t.Log("SUCCESS: prim=ADCBAACBDABCDBAACBDAADCBAACBDABCDBAACBDA, mode=ABCDABD")
	} else {
		t.Errorf("FAIL:  prim=ADCBAACBDABCDBAACBDAADCBAACBDABCDBAACBDA, mode=, res=%d", res)
	}

	res = KMPMatch("ADCBAACBDABCDBAACBDAADCBAACBDABCDBAACBDA", "BBBBBCABA")
	if res == -1 {
		t.Log("SUCCESS: prim=ADCBAACBDABCDBAACBDAADCBAACBDABCDBAACBDA, mode=BBBBBCABA")
	} else {
		t.Errorf("FAIL:  prim=ADCBAACBDABCDBAACBDAADCBAACBDABCDBAACBDA, mode=BBBBBCABA, res=%d", res)
	}

}

func TestBM(t *testing.T) {
	res := BM("ADCBAACBDABCD", "CBA")
	if res == 2 {
		t.Log("SUCCESS: prim=ADCBAACBDABCD, mode=CBA")
	} else {
		t.Errorf("FAIL:  prim=ADCBAACBDABCD, mode=CBA, res=%d", res)
	}

	res = BM("HICHYAT_THAT", "AT_THAT")
	if res == 5 {
		t.Log("SUCCESS: prim=HICHYAT_THAT, mode=AT_THAT")
	} else {
		t.Errorf("FAIL:  prim=HICHYAT_THAT, mode=AT_THAT, res=%d", res)
	}

	res = BM("ADCBAACBDABCD", "ADC")
	if res == 0 {
		t.Log("SUCCESS: prim=ADCBAACBDABCD, mode=ADC")
	} else {
		t.Errorf("FAIL:  prim=ADCBAACBDABCD, mode=ADC, res=%d", res)
	}

	res = BM("ADCBAACBDABCD", "ABCD")
	if res == 9 {
		t.Log("SUCCESS: prim=ADCBAACBDABCD, mode=ABCD")
	} else {
		t.Errorf("FAIL:  prim=ADCBAACBDABCD, mode=ABCD, res=%d", res)
	}

	res = BM("ADCBAACBDABCD", "ABCCD")
	if res == -1 {
		t.Log("SUCCESS: prim=ADCBAACBDABCD, mode=ABCCD")
	} else {
		t.Errorf("FAIL:  prim=ADCBAACBDABCD, mode=ABCCD, res=%d", res)
	}

	res = BM("ADCBAACBDABCDBAACBDAADCBAACBDABCDBAACBDA", "BCABABAB")
	if res == -1 {
		t.Log("SUCCESS: prim=ADCBAACBDABCDBAACBDAADCBAACBDABCDBAACBDA, mode=BCABABAB")
	} else {
		t.Errorf("FAIL:  prim=ADCBAACBDABCDBAACBDAADCBAACBDABCDBAACBDA, mode=BCABABAB, res=%d", res)
	}
}

func TestBMMatch(t *testing.T) {
	res := BMMatch("ADCBAACBDABCD", "CBA")
	if res == 2 {
		t.Log("SUCCESS: prim=ADCBAACBDABCD, mode=CBA")
	} else {
		t.Errorf("FAIL:  prim=ADCBAACBDABCD, mode=CBA, res=%d", res)
	}

	res = BMMatch("HICHYAT_THAT", "AT_THAT")
	if res == 5 {
		t.Log("SUCCESS: prim=HICHYAT_THAT, mode=AT_THAT")
	} else {
		t.Errorf("FAIL:  prim=HICHYAT_THAT, mode=AT_THAT, res=%d", res)
	}

	res = BMMatch("ADCBAACBDABCD", "ADC")
	if res == 0 {
		t.Log("SUCCESS: prim=ADCBAACBDABCD, mode=ADC")
	} else {
		t.Errorf("FAIL:  prim=ADCBAACBDABCD, mode=ADC, res=%d", res)
	}

	res = BMMatch("ADCBAACBDABCD", "ABCD")
	if res == 9 {
		t.Log("SUCCESS: prim=ADCBAACBDABCD, mode=ABCD")
	} else {
		t.Errorf("FAIL:  prim=ADCBAACBDABCD, mode=ABCD, res=%d", res)
	}

	res = BMMatch("ADCBAACBDABCD", "ABCCD")
	if res == -1 {
		t.Log("SUCCESS: prim=ADCBAACBDABCD, mode=ABCCD")
	} else {
		t.Errorf("FAIL:  prim=ADCBAACBDABCD, mode=ABCCD, res=%d", res)
	}

	res = BMMatch("ADCBAACBDABCDBAACBDAADCBAACBDABCDBAACBDA", "BCABABAB")
	if res == -1 {
		t.Log("SUCCESS: prim=ADCBAACBDABCDBAACBDAADCBAACBDABCDBAACBDA, mode=BCABABAB")
	} else {
		t.Errorf("FAIL:  prim=ADCBAACBDABCDBAACBDAADCBAACBDABCDBAACBDA, mode=BCABABAB, res=%d", res)
	}
}
