/*
*
Given a function f, and N return a debounced f of N milliseconds.

That is, as long as the debounced f continues to be invoked, f itself will not be called for N milliseconds.

*
*/
package main

import (
	"fmt"
	"time"

	"github.com/zmwangx/debounce"
)

func main() {
	start := time.Now()

	var count int
	sync, _ := debounce.Debounce(func() {
		fmt.Printf("syncing after %.1fs\n", time.Since(start).Seconds())
		count++ // This is thread-safe.
		// Sync data...
	}, 200*time.Millisecond, debounce.WithMaxWait(500*time.Millisecond))

	for time.Since(start) < 1200*time.Millisecond {
		// Do work that generates data here...
		sync()
	}

	time.Sleep(300 * time.Millisecond)
	fmt.Printf("synced %d times\n", count)
}
