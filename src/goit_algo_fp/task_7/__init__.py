"""Task 7: Monte Carlo Dice Simulation."""

from .monte_carlo import (
    monte_carlo_simulation,
    roll_dice,
    get_theoretical_probabilities,
)
from .visualization import print_probability_table, plot_probabilities

__all__ = [
    "monte_carlo_simulation",
    "roll_dice",
    "get_theoretical_probabilities",
    "print_probability_table",
    "plot_probabilities",
]
