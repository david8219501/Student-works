def get_max_profit(value_list):
    buy_p = value_list[0]
    max_p = 0
    profit = -1
    loss = float("-inf")
    for i in range(1, len(value_list)):
        max_p = max(max_p, value_list[i])
        profit = max(profit, max_p - buy_p)
        if value_list[i] < buy_p:
            if profit > -1:
                buy_p = value_list[i]
            else:
                loss = max(loss, max_p - buy_p)
                buy_p = value_list[i]
            max_p = 0
    if profit > -1:
        return profit
    else:
        return loss


max_profit = get_max_profit([21,18,16,6,3,3])
print(max_profit)