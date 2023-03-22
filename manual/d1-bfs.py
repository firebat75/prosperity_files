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


def bfs(market, val, curr_item, curr_path=[], all_trades={}):
    # if len(curr_path) == 5 and curr_path[-1] == "Shell":
    print(all_trades)
    if curr_path[-1] == "Shell":
        if val in all_trades.keys():
            all_trades[val].append(curr_path)
        else:
            all_trades[val] = [curr_path]

        return all_trades

    else:
        for item in market[curr_item].keys():
            rate = market[curr_item][item]
            temp_val = val * rate
            temp_path = curr_path + item

            return bfs(market, temp_val, item, temp_path, all_trades)


output = bfs(market, val)

# print(output)
