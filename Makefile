all: nlognGO nlognCPP

nlognGO: nlogn.go
	go build -o nlogngo nlogn.go

nlognCPP: nlogn.cc
	g++ -o nlogncpp nlogn.cc

clean_data: nlogncpp-* nlogngo-*
	rm -f nlogncpp-* nlogngo-*

clean:
	rm -f nlogncpp nlogngo
