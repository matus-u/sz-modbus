#!/bin/bash

function generate-from-uic {
	rm -rf generated/*
	#for i in ui/*; do pyside2-uic $i -o generated/$(basename $i |cut -f 1 -d .).py; done;
	for i in resources/*qrc; do pyside2-rcc $i -o generated/$(basename $i |cut -f 1 -d .).py; done;
}
