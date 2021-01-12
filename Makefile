all: ja.processed.html en.processed.html
%.processed.html: %.html conv.py
	python conv.py $< $@
