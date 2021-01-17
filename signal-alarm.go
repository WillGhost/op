package main
import (
	"fmt"
	"time"
	"sync"
	"os"
	"os/signal"
	"syscall"
)

func someThing() {
	for i:=1; i<10000; i++ {
		fmt.Println("http_request-----------", i)
		time.Sleep(time.Second)
	}
}

func doMessage(c int) {
	fmt.Println("---start", c)
	time.Sleep(time.Second * 5)
	fmt.Println("---end", c  )
}

func runWorker(chq chan int, done chan bool) {
	for {
		select {
		case <-done:
			fmt.Println("bye~~")
			return
		case c := <-chq:
		priority:
			for {
				select {
				case <-done:
					fmt.Println("bye~~")
					return
				default:
					break priority
				}
			}
			doMessage(c)
		default:
			fmt.Println("dddd====")
			time.Sleep(time.Second)
		}
	}
}


func listenSignal(cs chan os.Signal, curr int, done chan bool) {
	<-cs
	for i:=0; i<curr; i++ {
		done<-true
	}
	for {
		if len(done) == 0 {
			break
		}
		time.Sleep(time.Second)
	}
	signal.Stop(cs)
	syscall.Kill(syscall.Getpid(), syscall.SIGINT)
}



var wg sync.WaitGroup
func test() {
	chq := make(chan int, 100)
	for i:=1; i< 50; i++ {
		chq <- i
	}
	//close(chq)

	curr := 3
	done := make(chan bool, curr)

	cs := make(chan os.Signal)
	signal.Notify(cs, syscall.SIGINT, syscall.SIGTERM)
	go listenSignal(cs, curr, done)

	for i:=0; i<curr; i++ {
		wg.Add(1)
		go runWorker(chq, done)
	}

	someThing()
	wg.Wait()
}


func main() {
	test()
}



