available_coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(sum: int):
    available_coins_desc = sorted(available_coins, reverse=True)

    coins_count_dict = {}
    for coin in available_coins_desc:
        count = sum // coin
        if count > 0:
            coins_count_dict[coin] = count
            sum -= coin * count

    return coins_count_dict


def find_min_coins(sum: int):
    min_coins_required = [0] + [float("inf")] * sum
    last_coin_used = [0] * (sum + 1)

    for sub_sum in range(1, sum + 1):
        for coin in available_coins:
            if coin > sub_sum:
                continue

            min_coins_required_candidate = min_coins_required[sub_sum - coin] + 1
            if min_coins_required_candidate >= min_coins_required[sub_sum]:
                # the solution is not improved
                continue

            # the solution is improved
            min_coins_required[sub_sum] = min_coins_required_candidate
            last_coin_used[sub_sum] = coin

    return build_solution(last_coin_used, sum)


def build_solution(last_coin_used: list[int], sum: int):
    solution = {}
    while sum > 0:
        coin = last_coin_used[sum]
        solution[coin] = solution.get(coin, 0) + 1
        sum -= last_coin_used[sum]

    return solution


def main():
    sum = 113

    min_coins = find_min_coins(sum)
    greedy_coins = find_coins_greedy(sum)

    print(f"Min coins: {min_coins}")
    print(f"Greedy coins: {greedy_coins}")


if __name__ == "__main__":
    main()
