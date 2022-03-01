#!/bin/bash

for x in $(cat $1);
do y=$(grep -c $x $2); 
echo "The keyword $x was found $y in the fasta file.";
done
