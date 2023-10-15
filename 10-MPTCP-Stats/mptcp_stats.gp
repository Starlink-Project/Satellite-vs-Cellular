reset
set terminal pdfcairo enhanced color font "Helvetica,27" lw 2 size 9.3,4.8
set output 'mptcp_stats.pdf'

set xlabel "Network Provider" offset 0,0.6 font "Helvetica,31"
set ylabel 'Throughput (Mbps)' offset 1.85 font "Helvetica,31"

set xrange [0.6:7.4]
set yrange [0:400]
set xtics offset -0.1,0.2 center
set ytics offset 0.6

set key left top Left reverse at screen 0.16,0.95 samplen 2

set lmargin 5.65
set rmargin 0.7
set tmargin 0.55
set bmargin 2.4

set grid lc rgb "gray" lw 2
set style line 12 lc rgb 'black' lt 12 lw 1
set grid xtics,mxtics,ytics,mytics
set grid lw 3,lw 1,lw 3,lw 1
set grid lt 1,dt 2,lt 1,dt 2
set grid lc rgb "gray90",lc rgb "gray90",lc rgb "gray90",lc rgb "gray90"

set boxwidth 0.4
set style fill solid 1 border -1
set style data boxplot
set style boxplot outliers pointtype 7
set style boxplot fraction 0.95
set style boxplot nooutliers

set arrow from 5.5,0 to 5.5,400 nohead lc rgb "gray30" lw 4 dt (9,9)
set label 1 "Tuned" at screen 0.170,0.865 textcolor rgb "gray30" font "Helvetica,32"
set label 2 "Untuned" at screen 0.770,0.865 textcolor rgb "gray30" font "Helvetica,32"

plot 'mptcp_stats.txt' using ($2):($5):($4):($8):($7):xtic(1) with candlesticks lc rgb "purple" lw 3 ti col whiskerbars, \
     '' using ($2):($6):($6):($6):($6) with candlesticks lw 3 lt 1 lc rgb "black" notitle
