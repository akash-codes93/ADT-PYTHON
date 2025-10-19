package main

import "fmt"

type SparseArray struct {
	data map[int]int
	size int
}

func NewSparseArray(array []int) *SparseArray {

	var spArr SparseArray

	// make an empty map
	spArr.data = make(map[int]int)

	for idx, val := range array {
		if val != 0 {
			spArr.data[idx] = val
		}
	}

	spArr.size = len(array)
	return &spArr

}

func (spArr *SparseArray) Get(index int) (int, error) {

	if index >= spArr.size {
		return 0, fmt.Errorf("index out of range")
	}

	if val, ok := spArr.data[index]; ok {
		return val, nil
	}

	return 0, nil
}

func (spArr *SparseArray) Set(index, value int) {
	spArr.data[index] = value
}

func main() {

	arr := []int{1, 0, 3, 0, 5, 0, 7, 0, 9, 0, 0, 0, 1, 2, 3, 41, 2, 0, 0, 3, 0, 0}

	sparseArr := NewSparseArray(arr)
	val, err := sparseArr.Get(33)
	fmt.Println(val, err)

}
