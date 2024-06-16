package helper

import (
	"encoding/json"
	"io"
	"log"
	"net/http"
)

var (
	apiURL = "http://localhost:8000/"
)

type Helper struct {
	client *http.Client
}

func NewHelper() *Helper {
	return &Helper{
		client: &http.Client{},
	}
}

func (h *Helper) GetHCSR04(start, end string) (map[string]interface{}, error) {
	requestString := apiURL + "HCSR04?start=" + start + "&end=" + end

	req, err := http.NewRequest("GET", requestString, nil)
	if err != nil {
		log.Println(err)
		return nil, err
	}
	res, err := h.client.Do(req)
	if err != nil {
		log.Println(err)
		return nil, err
	}

	body, err := io.ReadAll(res.Body)
	log.Println(string(body))
	if err != nil {
		log.Println(err)
		return nil, err
	}
	var data map[string]interface{}
	json.Unmarshal(body, &data)

	return data, nil
}
