package app

import (
	"flag"
	"fmt"
	"log"
	"net"
	"net/http"

    "client/internal/helper"
)

var (
	port = flag.Int("port", 3000, "The server port")
)

type App struct {
    helper    *helper.Helper
}

func StartServer() {
	// Start the server
	lis, err := net.Listen("tcp", fmt.Sprintf(":%d", *port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	app := NewApp()

	err = http.Serve(lis, app.Routes())
	if err != nil {
		return
	}
}

func NewApp() *App {
	return &App{
		helper: helper.NewHelper(),
	}
}

func (a *App) Routes() http.Handler {
	mux := http.NewServeMux()
	mux.HandleFunc("/", a.LandingRoute)
	mux.HandleFunc("/mpu6050", a.MPU6050)
	mux.HandleFunc("/hcsr04", a.HCSR04)
	return mux
}
