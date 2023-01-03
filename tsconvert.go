package main

import (
	// "bufio"
	"fmt"
	"log"
	"os"
	"os/exec"
	"path/filepath"
)

func fileExists(filename string) bool {
    _, err := os.Stat(filename)
    return err == nil
}

func main() {
	var srcDir = "\\\\hs2500k\\m2ts"
	var dstDir = "d:\\tv"
	var ffmpegExec = ".\\ffmpeg"
	var ffmpegOpts = []string{"-vcodec", "h264_nvenc", "-vsync", "1", "-async", "1"}

	if len(os.Args) >= 2 {
		srcDir = os.Args[1]
	}

	if len(os.Args) >= 3 {
		dstDir = os.Args[2]
	}

	execDir := filepath.Dir(os.Args[0])
	if execDir != "." {
		ffmpegExec = filepath.Join(execDir, "ffmpeg")
	}

	if len(os.Args) >= 4 {
		ffmpegExec = os.Args[3]
	}

	fmt.Printf("* TS File Encode\n")
	fmt.Printf("  Src Directory: %s\n", srcDir)
	fmt.Printf("  Dst Directory: %s\n", dstDir)
	fmt.Printf("  ffmpeg: %s %s\n", ffmpegExec, ffmpegOpts)
	fmt.Println()

	pattern := filepath.Join(srcDir, "*.m2ts")
    files, err := filepath.Glob(pattern)
    if err != nil {
        panic(err)
    }
    for i, file := range files {
		baseFilename := filepath.Base(file)
		dstFilename := filepath.Join(dstDir, baseFilename[:len(baseFilename)-5] + ".mp4")
		if !fileExists(dstFilename) {
			fmt.Printf("%d/%d %s\n", i + 1, len(files), dstFilename)
			var opts = []string{"-i", file}
			for _, v := range ffmpegOpts {
				opts = append(opts, v)
			}
			opts = append(opts, dstFilename)
			cmd := exec.Command(ffmpegExec, opts...)
			cmd.Stdout = os.Stdout
			cmd.Stderr = os.Stderr
			err := cmd.Run()
			if err != nil {
				log.Fatal(err)
			}
		}
    }

}