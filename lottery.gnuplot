set term png
set output "lottery.png"
set style histogram rowstacked gap 0
set style fill solid 0.5 border lt -1
plot "lottery.data" linecolor rgb "green" notitle