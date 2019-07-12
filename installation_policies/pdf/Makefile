# Create a PDF of the xSDK community policies.
# Depends on pandoc and the python package panflute:
# --- See https://pandoc.org/installing.html for information on installing pandoc.
# --- Run `pip install panflute` to obtain panflute.
# To generate the pdf just run `make`.
#
# Author: Cody Balos (@balos1)

all:
	pandoc -F fixlinks.py -fmarkdown-implicit_figures *.md -o xsdk-installation-policies.pdf
