build:
	PYTHONPATH=$PYTHONPATH:$(pwd) jb build .

all:
	PYTHONPATH=$PYTHONPATH:$(pwd) jb build . --all

clean:
	rm -r ./_static/plot

