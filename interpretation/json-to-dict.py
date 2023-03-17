import numpy as np
import matplotlib.pyplot as plt
import json

f = open("interpretation/state.json")

data = json.load(f)

iterations = []
per_prices = []

for key in data:
    iterations.append(int(key))
    price = max(data[key]["MARKET"]["PEARLS"]["BUY ORDERS"].keys())
    per_prices.append(int(price))


xpoints = np.array(iterations[:16])
ypoints = np.array(per_prices[:16])

plt.plot(xpoints, ypoints)
plt.show()
