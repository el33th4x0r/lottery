all: lottery.png lottery.sorted

lottery.data:	lottery.py
	python lottery.py >lottery.data

lottery.sorted: lottery.data
	head -1000 lottery.data | sort -nr -k +2 >$@

lottery.png: lottery.gnuplot lottery.data
	gnuplot lottery.gnuplot

