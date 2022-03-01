#!/bin/bash

echo '$1 = ' $1
echo '$2 = ' $2
#echo '$3 = ' $3
#echo '$4 = ' $4

grep '>' -c $1 
grep '>' -c $2 
#grep '>' -c $3 
#grep '>' -c $4 
