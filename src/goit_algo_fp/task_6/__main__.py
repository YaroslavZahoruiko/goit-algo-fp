from goit_algo_fp.task_6.algorithms import dynamic_programming, greedy_algorithm


def main() -> None:
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }

    budget = 100

    print("=" * 60)
    print("Knapsack Problem: Maximize Calories within Budget")
    print("=" * 60)
    print(f"\nBudget: {budget}")
    print("\nAvailable items:")
    for name, props in items.items():
        ratio = props["calories"] / props["cost"]
        print(
            f"  {name:12} - Cost: {props['cost']:3}, Calories: {props['calories']:4}, Ratio: {ratio:.2f}"
        )

    print("\n" + "-" * 60)
    print("Dynamic Programming Solution (Optimal):")
    print("-" * 60)
    dp_result = dynamic_programming(items, budget)
    if dp_result:
        total_cost = sum(items[name]["cost"] * qty for name, qty in dp_result.items())
        total_calories = sum(
            items[name]["calories"] * qty for name, qty in dp_result.items()
        )
        print(f"Selected items: {dp_result}")
        print(f"Total cost: {total_cost}")
        print(f"Total calories: {total_calories}")
    else:
        print("No solution found")

    print("\n" + "-" * 60)
    print("Greedy Solution (Approximation):")
    print("-" * 60)
    greedy_result = greedy_algorithm(items, budget)
    if greedy_result:
        total_cost = sum(
            items[name]["cost"] * qty for name, qty in greedy_result.items()
        )
        total_calories = sum(
            items[name]["calories"] * qty for name, qty in greedy_result.items()
        )
        print(f"Selected items: {greedy_result}")
        print(f"Total cost: {total_cost}")
        print(f"Total calories: {total_calories}")
    else:
        print("No solution found")


if __name__ == "__main__":
    main()
