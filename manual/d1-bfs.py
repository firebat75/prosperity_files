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

all = {}


def bfs(market, val, curr_item, curr_path=["Shell"], all_trades={}):
    # if len(curr_path) == 5 and curr_path[-1] == "Shell":

    # if len(curr_path) > 0 and curr_path[-1] == "Shell":
    #     if val in all_trades.keys():
    #         all_trades[val].append(curr_path)
    #     else:
    #         all_trades[val] = [curr_path]

    #     return all_trades

    if curr_path[-1] == "Shell":
        global all
        if val in all.keys():
            all[val].append(curr_path)
        else:
            all[val] = curr_path

    if len(curr_path) > 5:
        return None

    for item in market[curr_item].keys():
        rate = market[curr_item][item]
        temp_val = val * rate
        temp_path = curr_path + [item]

        bfs(market, temp_val, item, temp_path, all_trades)


output = bfs(market, val, start)

print(all)

print(max(all.keys()))


trades = []
vals = []
for item in all:
    trades.append([round(item), all[item]])
    vals.append(item)
vals.sort()
vals.reverse()
for item in vals:
    print(round(item), all[item])

for item in all:
    if all[item] == ["Shell", "Pizza Slice", "Wasabi Root", "Snowball", "Pizza Slice", "Shell"]:
        print("dsdasfafghjseiofjwef3j0fj390hjfioehjwjofjwef")
        print(item)
# print(output)
