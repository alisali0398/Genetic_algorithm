# Genetic_algorithm
Genetic_algorithm test case

## Optimization problem 
f(x, y) = cos((x - 1.14)^6) - 100*(y^2 - x)^4

0 <= x <= 2

0 <= y <= 3

x + y >= 1

## Composition of chromosomes

The number of distinct values N = (b - a)/ε

The number of bits n = log<sub>2</sub>N = log<sub>2</sub>(b - a)/ε


# Genetic Algorithm for Optimization Problem 3

## 1. Problem Definition

We aim to **maximize** the following function under given constraints:

\[
f(x,y) = \cos((x - 1.14)^6) - 100 \cdot (y^2 - x)^4
\]

**Domain and constraints:**
- \( 0 \< x \< 2 \)
- \( 0 \<leq> y \leq 3 \)
- \( x + y \geq 1 \)

---

## 2. Chromosome Representation

- Precision: \( \varepsilon = 10^{-4} \) (four decimal places).
- The number of distinct values:

\[
N = \frac{b-a}{\varepsilon}
\]

- Number of bits:

\[
n = \log_2 \left(\frac{b-a}{\varepsilon}\right)
\]

### Encoding
- **For x**:  
  Domain length = 2 (0 to 2)  
  \( n_x = \log_2 \frac{2-0}{10^{-4}} \approx 14.28 \approx 15 \) bits  

- **For y**:  
  Domain length = 3 (0 to 3)  
  \( n_y = \log_2 \frac{3-0}{10^{-4}} \approx 14.87 \approx 16 \) bits  

Since \( 2^{15} = 32768 \) just covers the required range for \( y \), we round up to **16 bits** to ensure full coverage.

### Total Chromosome Length
- **31 bits**:  
  - first 15 bits → encode \( x \)  
  - last 16 bits → encode \( y \)

---

## 3. Algorithm Parameters

- **Population size**: 100 chromosomes  
- **Number of generations**: 1000  

---

## 4. Implementation Notes

- Selection method: roulette wheel (with safe handling for invalid probabilities).  
- Crossover: two-point crossover.  
- Mutation: bit-flip mutation.  
- Constraint handling: penalty function applied if \( x + y < 1 \).  

---

