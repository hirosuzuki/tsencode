tsconvert.exe: tsconvert.go
	GOOS=windows GOARCH=amd64 go build tsconvert.go
