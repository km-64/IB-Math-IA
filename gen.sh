#!/bin/bash

# Run script with multiple sampling
# Unbiased:  6,  7
# Lower:    10, 11 
# Center:   14, 15
# Upper:    18, 19

comment() {
    sed -i -E "$1 s/^(\s*)(.*)/\1#\2/" "$2"
}

uncomment() {
    sed -i -E "$1 s/^(\s*)#\s*/\1/" "$2"
}

uncomment 6 src/sampling.py
uncomment 7 src/sampling.py
python src/tables.py 'tables/unbiased'
comment 6 src/sampling.py
comment 7 src/sampling.py

uncomment 10 src/sampling.py
uncomment 11 src/sampling.py
python src/tables.py 'tables/lowerbiased'
comment 10 src/sampling.py
comment 11 src/sampling.py

uncomment 14 src/sampling.py
uncomment 15 src/sampling.py
python src/tables.py 'tables/centrebiased'
comment 14 src/sampling.py
comment 15 src/sampling.py


uncomment 18 src/sampling.py
uncomment 19 src/sampling.py
python src/tables.py 'tables/upperbiased'
comment 18 src/sampling.py
comment 19 src/ampling.py
