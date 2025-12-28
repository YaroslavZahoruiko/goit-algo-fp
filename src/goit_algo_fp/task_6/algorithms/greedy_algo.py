def greedy_algorithm(
    items: dict[str, dict[str, int]], budget: int
) -> dict[str, int] | None:
    if budget < 0:
        raise ValueError("Budget must be non-negative")

    if budget == 0 or not items:
        return {}

    item_list = []
    for name, item in items.items():
        cost = item.get("cost", 0)
        calories = item.get("calories", 0)
        if cost > 0 and calories >= 0:
            ratio = calories / cost if cost > 0 else 0
            item_list.append((name, cost, calories, ratio))

    if not item_list:
        return {}

    item_list.sort(key=lambda x: x[3], reverse=True)

    result = {}
    remaining_budget = budget

    for name, cost, calories, ratio in item_list:
        if remaining_budget >= cost:
            result[name] = 1
            remaining_budget -= cost

    return dict(sorted(result.items())) if result else {}
