def dynamic_programming(
    items: dict[str, dict[str, int]], budget: int
) -> dict[str, int] | None:
    if budget < 0:
        raise ValueError("Budget must be non-negative")

    if budget == 0 or not items:
        return {}

    item_list = [(name, item["cost"], item["calories"]) for name, item in items.items()]

    if not item_list:
        return {}

    n = len(item_list)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, cost, calories = item_list[i - 1]
        for w in range(budget + 1):
            dp[i][w] = dp[i - 1][w]
            if w >= cost:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - cost] + calories)

    result = {}
    w = budget
    max_calories = dp[n][budget]

    if max_calories == 0:
        return {}

    optimal_budget = max(range(budget + 1), key=lambda b: dp[n][b])
    w = optimal_budget

    for i in range(n, 0, -1):
        name, cost, calories = item_list[i - 1]
        if w >= cost and dp[i][w] == dp[i - 1][w - cost] + calories:
            result[name] = 1
            w -= cost

    return dict(sorted(result.items()))
