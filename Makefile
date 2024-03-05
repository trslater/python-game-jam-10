# Default: macOS (whould work on Linux as well)
SEP=:

ifeq ($(OS),Windows_NT)
	SEP=;
endif

.PHONY: dist install dev clean

dist:
	pyinstaller scripts/run.py \
		--add-data "src/config.toml$(SEP)." \
		--add-data "assets$(SEP)assets" \
		--add-data "maps$(SEP)maps" \
		--onefile \
		--windowed \
		--name pyjam10

install:
	pip install -e .

dev:
	pip install -e '.[dev]'

clean:
	rm -fr ./build
	rm -fr ./dist
	rm pyjam10.spec
