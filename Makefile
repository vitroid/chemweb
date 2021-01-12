all: ja.processed.html en.processed.html
%.processed.html: %.html
	python conv.py $< $@
