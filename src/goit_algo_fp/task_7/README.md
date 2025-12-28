# Task 7: Monte Carlo Simulation - Two Dice Rolls

## Overview

This task implements a Monte Carlo simulation to estimate the probability distribution of the sum of two six-sided dice. The simulation results are compared with analytical (theoretical) calculations to validate the correctness of the implementation.

## Implementation

The simulation performs a large number of random dice rolls (default: 100,000) and calculates the empirical probabilities for each possible sum (ranging from 2 to 12). These results are then compared with the theoretical probabilities derived from combinatorial analysis.

### Theoretical Probabilities

For two six-sided dice, the theoretical probabilities are calculated as follows:

- Sum of 2: 1/36 (only one combination: 1+1)
- Sum of 3: 2/36 (combinations: 1+2, 2+1)
- Sum of 4: 3/36 (combinations: 1+3, 2+2, 3+1)
- Sum of 5: 4/36 (combinations: 1+4, 2+3, 3+2, 4+1)
- Sum of 6: 5/36 (combinations: 1+5, 2+4, 3+3, 4+2, 5+1)
- Sum of 7: 6/36 (combinations: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1)
- Sum of 8: 5/36 (combinations: 2+6, 3+5, 4+4, 5+3, 6+2)
- Sum of 9: 4/36 (combinations: 3+6, 4+5, 5+4, 6+3)
- Sum of 10: 3/36 (combinations: 4+6, 5+5, 6+4)
- Sum of 11: 2/36 (combinations: 5+6, 6+5)
- Sum of 12: 1/36 (only one combination: 6+6)

## Conclusions on Calculation Correctness

### Comparison Results

By comparing the results obtained using the Monte Carlo method with the analytical calculation results, the following conclusions can be drawn:

1. **High Accuracy with Large Sample Sizes**: When running the simulation with 100,000 rolls or more, the Monte Carlo results closely approximate the theoretical probabilities. The differences between simulated and theoretical values are typically within 0.1-0.5 percentage points.

2. **Convergence to Theoretical Values**: As the number of simulation runs increases, the Monte Carlo estimates converge towards the theoretical probabilities, demonstrating the law of large numbers in action.

3. **Symmetry Validation**: The simulation correctly reproduces the symmetric distribution around sum 7 (the most probable sum), with sums equidistant from 7 having equal probabilities (e.g., 2 and 12, 3 and 11, etc.).

4. **Distribution Shape**: The triangular distribution shape (peaking at sum 7) is accurately represented in the Monte Carlo results, confirming that the simulation correctly models the underlying probability distribution.

5. **Statistical Validation**: The comparison shows that the Monte Carlo method provides a reliable approximation of the true probabilities, validating both:
   - The correctness of the simulation implementation
   - The accuracy of the theoretical calculations

### Key Insights
While numerical integration provides higher precision, Monte Carlo simulation offers remarkable flexibility and ease of implementation. The slightly larger error in Monte Carlo is often acceptable given its ability to handle complex domains that would be difficult or impossible to integrate analytically. This makes Monte Carlo particularly valuable for exploring larger problem spaces and more complex geometric configurations.

## Usage

Run the simulation:
```bash
uv run python -m goit_algo_fp.task_7
```

The output includes:
- A probability table comparing Monte Carlo and theoretical results
- A bar chart visualization showing both distributions
- Summary statistics including most/least common sums
- Expected value calculations

