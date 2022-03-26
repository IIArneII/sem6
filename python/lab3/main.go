package main

import "unicode"

func main() {
	alphanumeric("123adwfw sq")
}

func alphanumeric(str string) bool {
	for i := 0; i < len(str); i++ {
		if unicode.IsSpace(str[i]) || str[i] == rune('_') {return false}
	}
	return true
}
