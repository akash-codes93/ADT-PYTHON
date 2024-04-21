package main

import (
	"fmt"
	"math"

	bitarray "github.com/Workiva/go-datastructures/bitarray"
	"github.com/spaolacci/murmur3"
)

type BloomFilter struct {
	bits bitarray.BitArray // bitarray to store the bits
	m    uint64            // size of the bit array
	k    uint64            // number of hash functions
	n    uint64            // number of items you want to store in BF
	p    float64           // false positive probability
}

func createBloomFilters(size uint64, falseProbab float64) *BloomFilter {
	// calculating size of bit array
	_m := -((float64(size) * math.Log(falseProbab)) / (math.Log(2) * math.Log(2)))
	m1 := uint64(_m)

	// calculating number of hash functions
	_k := (_m / float64(size)) * math.Log(2)
	k1 := uint64(_k)

	bitarray := bitarray.NewBitArray(m1)
	return &BloomFilter{
		bits: bitarray,
		m:    m1,
		k:    k1,
		n:    size,
		p:    falseProbab,
	}
}

type Interface interface {
	add(item []byte)
	check(item []byte) bool
}

func (bf *BloomFilter) add(item string) {
	bits := bf.bits
	k := bf.k
	m := bf.m // basically use to % over index to keep in range

	for i := 0; i < int(k); i++ {
		digest := getIndex(item, i, m) // i is passed as seed
		bits.SetBit(digest)
	}
}

func (bf *BloomFilter) check(item string) bool {
	bits := bf.bits
	k := bf.k
	m := bf.m

	for i := 0; i < int(k); i++ {
		digest := getIndex(item, i, m)
		// checking if the digest bit exists in the array or not
		exist, err := bits.GetBit(digest)
		if err != nil {
			panic("Issue while check if bit is set in bitarray")
		}
		if !exist {
			return false
		}
	}
	return true
}

func getIndex(item string, i int, m uint64) uint64 {
	hash := murmur3.New32WithSeed(uint32(i))

	hash.Write([]byte(item))

	return uint64(int(hash.Sum32()) % int(m))
}

func main() {
	bloom_filter := createBloomFilters(40, 0.02)
	bloom_filter.add("akash")
	// bloom_filter.add("")

	fmt.Println(bloom_filter.check("akash"))
	fmt.Println(bloom_filter.check("akas123"))

}
