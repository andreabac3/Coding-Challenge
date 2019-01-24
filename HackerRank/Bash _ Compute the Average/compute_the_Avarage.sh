#!/bin/bash 
read nLines
sum=0
for (( c=0; c<nLines; c++ ))
do
    read val
    sum=$(($sum + $val)) 
done

printf "%.3f\n" "$(bc -l <<< "($sum / $nLines)")"

exit
