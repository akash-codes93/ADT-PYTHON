package main

import (
	"fmt"
	"math/rand"
)

func reservoirSampling(stream []int, k int) []int {
	// return k elements reservoir from stream of elements
	if k > len(stream) {
		return stream
	}

	reservoir := stream[0:k]

	for i := k; i < len(stream); i++ {
		j := rand.Intn(i)
		if j < k {
			reservoir[j] = stream[i]
		}
	}
	return reservoir
}

func main() {
	stream := []int{1, 2, 3, 4, 5, 6, 7}
	fmt.Println(reservoirSampling(stream, 3))

}
