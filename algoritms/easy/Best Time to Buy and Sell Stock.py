def maxProfit(prices: list) -> int:
    buy_index = 0
    sell_index = 1
    max_profit = 0
    while sell_index < len(prices):
        current_profit = prices[sell_index] - prices[buy_index]
        if prices[buy_index] < prices[sell_index]:
            max_profit = max(current_profit, max_profit)
        else:
            buy_index = sell_index
        sell_index += 1
    return max_profit
