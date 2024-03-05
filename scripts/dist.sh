#!/usr/bin/env bash

pyinstaller scripts/run.py \
	--add-data "src/config.toml:." \
	--add-data "assets:assets" \
	--add-data "maps:maps" \
	--onefile \
	--windowed \
	--name pyjam10
