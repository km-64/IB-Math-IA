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

uncomment 6 sampling.py
uncomment 7 sampling.py
python tables.py 'tables/unbiased'
comment 6 sampling.py
comment 7 sampling.py

uncomment 10 sampling.py
uncomment 11 sampling.py
python tables.py 'tables/lowerbiased'
comment 10 sampling.py
comment 11 sampling.py

uncomment 14 sampling.py
uncomment 15 sampling.py
python tables.py 'tables/centrebiased'
comment 14 sampling.py
comment 15 sampling.py


uncomment 18 sampling.py
uncomment 19 sampling.py
python tables.py 'tables/upperbiased'
comment 18 sampling.py
comment 19 sampling.py
