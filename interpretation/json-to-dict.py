import numpy as np
import matplotlib.pyplot as plt
import json

f = open("state.json")

data = json.load(f)

iterations = []
per_prices = []

for key in data:
    iterations.append(int(key))
    price = max(data[key]["MARKET"]["PEARLS"]["BUY ORDERS"].keys())
    per_prices.append(int(price))

print(data)


# xpoints = np.array(iterations[:100])
# ypoints = np.array(per_prices[:100])

# plt.plot(xpoints, ypoints)
# plt.show()
