#
# “How to properly 'make' a latex project?”
# https://tex.stackexchange.com/a/40759
# — @DevSolar
#

SOURCE=Nicolas-Dubois-cv-fr.tex
OUTPUT=Nicolas-Dubois-cv-fr.pdf

.PHONY: ${OUTPUT} all clean

all: ${OUTPUT}

%.tex: %.raw
	./raw2tex $< > $@

%.tex: %.dat
	./dat2tex $< > $@

${OUTPUT}: ${SOURCE}
	latexmk -pdf -pdflatex="pdflatex -interaction=nonstopmode" -use-make ${SOURCE}

view:
	open ${OUTPUT}

clean:
	latexmk -CA
