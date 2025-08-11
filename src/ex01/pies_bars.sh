#!/bin/bash

echo "2007, 73.32, 70.52" > pies_bars_data.txt
echo "2008, 81.23, 93.00" >> pies_bars_data.txt
echo "2009, 181.43, 135.10" >> pies_bars_data.txt
echo "2010, 110.21, 95.00" >> pies_bars_data.txt
echo "2011, 93.97, 90.45" >> pies_bars_data.txt
echo "Pies (green), Bars (yellow)"
termgraph pies_bars_data.txt --color green yellow --width 50 --delim , --format "{:.2f}"