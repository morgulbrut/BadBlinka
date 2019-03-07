package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	template "text/template"

	"github.com/fatih/color"
)

func main() {
	var payload []string
	if len(os.Args) <= 1 {
		color.Red("ERROR: Exepted DuckyScript file")
		os.Exit(1)
	}

	color.Green("Compiling DuckyScript")

	file, err := os.Open(os.Args[1])
	if err != nil {
		color.Red("ERROR: File not found")
		os.Exit(1)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		payload = append(payload, processLine(scanner.Text()))
	}

	if err := scanner.Err(); err != nil {
		color.Red("ERROR: Could not read file")
		os.Exit(1)
	}

	executeTemplate(strings.Join(payload, "\n"))

}

func processLine(s string) string {
	params := strings.Split(s, " ")
	cmd, params := params[0], params[1:]
	cmd = strings.ToUpper(cmd)
	switch cmd {
	case "REM":
		return "    # " + strings.Join(params, " ")
	case "STRING":
		return "    keyboard_layout.write(\"" + strings.Join(params, " ") + "\")"
	case "DELAY":
		t, err := strconv.ParseFloat(params[0], 64)
		if err != nil {
			color.Red("ERROR: DELAY: Missing param")
			os.Exit(1)
		}
		return fmt.Sprintf("    time.sleep(%0.1f)", t/1000)
	case "GUI", "SHIFT", "ALT", "CTRL":
		key := strings.ToUpper(params[0])
		switch key {
		case "SHIFT", "ALT", "CTRL":
			key2 := strings.ToUpper(params[1])
			return "    keyboard.press(Keycode." + cmd + ", Keycode." + key + ", Keycode." + key2 + ")\n    keyboard.release_all()"
		default:
			return "    keyboard.press(Keycode." + cmd + ", Keycode." + key + ")\n    keyboard.release_all()"
		}
	case "DELETE", "HOME", "INSERT", "PAGE_UP", "PAGE_DOWN", "UP_ARROW", "DOWN_ARROW", "LEFT_ARROW", "RIGHT_ARROW", "TAB",
		"END", "ESCAPE":
		return "    keyboard.press(Keycode." + cmd + ")\n    keyboard.release_all()"
	default:
		return "    # UNDEFINED: " + s
	}
}

func executeTemplate(s string) {
	color.Yellow(s)

	f, err := os.Create("code.py")
	if err != nil {
		color.Red("ERROR: template parsing fail")
		os.Exit(1)
	}

	//w := bufio.NewWriter(f)

	t, err := template.ParseFiles("code_template.py")
	if err != nil {
		color.Red("ERROR: template parsing fail")
		os.Exit(1)
	}
	t.Execute(f, s)
}
