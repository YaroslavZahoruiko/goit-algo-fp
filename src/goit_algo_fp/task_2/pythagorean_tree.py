import turtle
from typing import Any


class PythagoreanTree:
    """A fractal tree visualization using the Pythagorean theorem."""

    def __init__(self) -> None:
        """Initialize the Pythagorean tree with a turtle graphics instance."""
        self.t: Any = turtle.Turtle()  # type: ignore[assignment]

    def show(self, length: float, depth: int, angle: float = 45, ratio: float = 0.8) -> None:
        """
        Display the Pythagorean tree fractal.

        Args:
            length: Initial branch length
            depth: Recursion depth (number of levels)
            angle: Branch angle in degrees (default: 45)
            ratio: Length reduction ratio for child branches (default: 0.8)
        """
        self.t.speed(0)
        self.t.color("darkred")
        self.t.width(2)
        self.t.hideturtle()
        self.t.penup()
        self.t.goto(0, -300)
        self.t.setheading(90)
        self.t.pendown()

        screen = turtle.Screen()
        screen.bgcolor("white")

        self.naked_pythagoras_tree(length, depth, angle, ratio)

    def naked_pythagoras_tree(
        self, length: float, depth: int, angle: float = 45, ratio: float = 0.8
    ) -> None:
        """
        Recursively draw the Pythagorean tree.

        Args:
            length: Current branch length
            depth: Remaining recursion depth
            angle: Branch angle in degrees
            ratio: Length reduction ratio for child branches
        """
        if depth == 0:
            return

        self.t.forward(length)

        self.t.left(angle)
        self.naked_pythagoras_tree(length * ratio, depth - 1, angle, ratio)

        self.t.right(2 * angle)
        self.naked_pythagoras_tree(length * ratio, depth - 1, angle, ratio)

        self.t.left(angle)
        self.t.backward(length)
