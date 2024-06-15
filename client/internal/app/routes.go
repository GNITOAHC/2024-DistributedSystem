package app

import (
	"net/http"
)

func (a *App) LandingRoute(w http.ResponseWriter, r *http.Request) {}
func (a *App) MPU6050(w http.ResponseWriter, r *http.Request)      {}
func (a *App) HCSR04(w http.ResponseWriter, r *http.Request)       {}
