all: nlognGO nlognCPP

nlognGO: nlogn.go 
	go build -o nlogngo nlogn.go

nlognCPP: nlogn.cc
	g++ -o nlogncpp nlogn.cc
	
clean:
	rm -f nlogncpp nlogngo