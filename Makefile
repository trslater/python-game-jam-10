.PHONY: dist install dev clean

dist:
	pyinstaller scripts/run.py \
		--onefile \
		--windowed \
		--name pyjam7

install:
	pip install -e .

dev:
	pip install -e '.[dev]'

clean:
	rm -fr ./build
	rm -fr ./dist
	rm pyjam7.spec
