market = {
    "Pizza Slice": {
        "Wasabi Root": 0.5,
        "Snowball": 1.45,
        "Shell": 0.75
    },

    "Wasabi Root": {
        "Pizza Slice": 1.95,
        "Snowball": 3.1,
        "Shell": 1.49,
    },

    "Snowball": {
        "Pizza Slice": 0.67,
        "Wasabi Root": 0.31,
        "Shell": 0.48
    },

    "Shell": {
        "Pizza Slice": 1.34,
        "Wasabi Root": 0.64,
        "Snowball": 1.98
    }
}

val = 2000.0
start = "Shell"


def bfs(market, val, curr_trades=[], all_trades={}, curr="Shell"):

    if len(curr_trades) == 5:
        if val in all_trades.keys():
            all_trades[val].append(curr_trades)
        else:
            all_trades[val] = [curr_trades]
        return all_trades

    if len(curr_trades) == 4 and curr != "Shell":

        temp_val = val * market[curr]["Shell"]

        return bfs(market, val, temp_trades, all_trades, "Shell")

    elif len(curr_trades) == 4 and curr == "Shell":
        return all_trades

    for rate in market[curr].keys():

        item = market[curr][rate]

        temp_val = val * rate
        temp_trades = curr_trades + [market[curr][rate]]

        if temp_val in all_trades.keys():
            all_trades[temp_val].append(temp_trades)
        else:
            all_trades[temp_val] = [temp_trades]

        print(all_trades)

        return bfs(market, val, temp_trades, all_trades, item)

        # if len(temp_trades) == 5:
        #     return all_trades
        # elif len(temp_trades) == 4 and curr != "Shell":
        #     bfs(exchange, val, temp_trades, all_trades, "Shell")
        # else:
        #     bfs(exchange, val, temp_trades, all_trades, item)


output = bfs(market, val)

# print(output)
