package app

import (
	"encoding/json"
	"log"
	"net/http"
	"text/template"
)

func (a *App) LandingRoute(w http.ResponseWriter, r *http.Request) {
	tmpl := template.Must(template.ParseFiles("templates/base.html", "templates/landing.html"))
	err := tmpl.Execute(w, nil)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
}

func (a *App) MPU6050(w http.ResponseWriter, r *http.Request) {
	tmpl := template.Must(template.ParseFiles("templates/base.html", "templates/mpu6050.html"))
	err := tmpl.Execute(w, nil)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}

}

func (a *App) HCSR04(w http.ResponseWriter, r *http.Request) {
	startTime := r.URL.Query().Get("start")
	endTime := r.URL.Query().Get("end")
	if startTime == "" || endTime == "" {
		log.Println("No start or end time provided")
		a.tmplExecute(w, []string{"templates/base.html", "templates/hcsr04.html"}, nil)
		return
	}
	data, err := a.helper.GetHCSR04(startTime, endTime)

	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	err = json.NewEncoder(w).Encode(data)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
	return
}
