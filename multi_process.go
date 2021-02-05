package main

import (
	"fmt"
	"sync"
	"time"
)

var wg sync.WaitGroup

func DoWork(cc chan int) {
	for {
		a, ok := <-cc
		if !ok {
			break
		}
		fmt.Println("wwwwwww", a)
		time.Sleep(time.Second)
	}
	wg.Done()
}

func main() {
	cc := make(chan int, 10)

	for i := 0; i < 3; i++ {
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
