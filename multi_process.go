package main

import (
	"fmt"
	"sync"
	"time"
)

var wg sync.WaitGroup

func DoWork(cc chan int) {
	for v := range cc {
		fmt.Println("wwwwwww", v)
		time.Sleep(time.Second)
	}
	wg.Done()
}

func main() {
	Concurrent := 3
	cc := make(chan int)

	for i := 0; i < Concurrent; i++ {
		wg.Add(1)
		go DoWork(cc)
	}

	for i := 0; i < 20; i++ {
		cc <- i
	}
	close(cc)

	wg.Wait()
	fmt.Println("oooooover")
}
