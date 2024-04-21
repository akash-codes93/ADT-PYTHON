package main

import (
	"fmt"
	"slices"

	"github.com/spaolacci/murmur3"
)

type CountMinSketch struct {
	m      uint64  // size of sketch
	k      uint64  // number of hash functions
	sketch [][]int // sketch
}

func NewCountMinSketch(countOfHash int) *CountMinSketch {
	// taking size as 2000
	sketch1 := make([][]int, countOfHash)
	for i := 0; i < countOfHash; i++ {
		sketch1[i] = make([]int, 2000)
		// making all values 0
		for j := 0; j < 2000; j++ {
			sketch1[i][j] = 0
		}
	}

	return &CountMinSketch{
		m:      2000,
		k:      uint64(countOfHash),
		sketch: sketch1,
	}
}

func (csm *CountMinSketch) add(key string) {

	k := csm.k
	m := csm.m // basically use to % over index to keep in range

	for i := 0; i < int(k); i++ {
		digest := getIndex(key, i, m) // i is passed as seed
		csm.sketch[i][digest]++
	}
}

func (csm *CountMinSketch) query(key string) int {
	k := csm.k
	m := csm.m // basically use to % over index to keep in range

	counts := []int{}

	for i := 0; i < int(k); i++ {
		digest := getIndex(key, i, m) // i is passed as seed
		counts = append(counts, csm.sketch[i][digest])
	}

	return slices.Min(counts)
}

func getIndex(item string, i int, m uint64) int {
	hash := murmur3.New32WithSeed(uint32(i))
	hash.Write([]byte(item))
	return int(hash.Sum32()) % int(m)
}

func main() {
	csm := NewCountMinSketch(10)
	csm.add("akash")
	csm.add("akash")
	csm.add("akash")
	csm.add("akash")

	csm.add("Peter")
	csm.add("Peter")
	csm.add("Peter")
	csm.add("Peter")
	csm.add("Peter")
	csm.add("Peter")
	csm.add("Peter")
	csm.add("Peter")
	csm.add("Peter")
	csm.add("Peter")

	fmt.Println(csm.query("akash"))
	fmt.Println(csm.query("akash123"))
	fmt.Println(csm.query("Peter"))
}
