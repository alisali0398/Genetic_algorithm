# Genetic_algorithm
Genetic_algorithm test case

## Optimization problem - maximize
f(x, y) = cos((x - 1.14)<sup>6</sup>) - 100 * (y<sup>2</sup> - x)<sup>4</sup>

0 &le; x &le; 2

0 &le; y &le; 3

x + y &ge; 1

## The composition of chromosomes: 

The number of distinct values N = (b - a) / ε

The number of bits n = log<sub>2</sub>N = log<sub>2</sub>(b - a) / ε

Precision ε = 10<sup>-4</sup> means four places after the decimal point

The domain length for x is 2 (0 ~ 2)

n<sub>x</sub> = 14.28 ~ 15 bits

The domain length for y is 2 (0 ~ 3)

n<sub>y</sub> = 14.87 ~ 16 bits

For n<sub>y</sub>, the number of bits is rounded up to 16 to ensure there are enough binary 
combinations to represent all possible values. Using the domain length equal to 
15 gives us 2<sup>15</sup>=32768 values, which is just above 30000, so from safety 
reasons the domain length equal to 16 will be used (2<sup>16</sup>= 65536 values). 

Total chromosome length is 31 bits – first 15 bits to encode x, last 16 bits to 
encode y.

## Number of chromosomes and number of generations: 
Size of the **population** is **200 chromosomes** 

Number of **generations** is **5000**

## Mechanisms of selection, crossover and mutation: 
Selection mechanism – roulette wheel 

Crossover mechanism – two-point crossover 

Mutation mechanism – mutation of one random bit (bit flipping)

## Constraint handling:  
The constraint x + y &ge; 1 is used as a penalty method. If the solution violates the 
constraint, a large negative fitness value is applied to decrease the possibility of 
survival to the next generation.  

## Setting of tuning parameters: 
Crossover rate – 0.9 

Mutation rate – 0.1 

Penalty rate – 10<sup>6</sup> 
