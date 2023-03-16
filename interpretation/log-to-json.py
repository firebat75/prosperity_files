import json
import ast

with open("print-state-v9.log", "r") as f:
    lines = f.readlines()

LENGTH = len(lines)
STATE = {}

NUM_ITEMS = 2

count = 0
for i in range(LENGTH):

    if lines[i][-2:-12:-1] == "++++++++++":

        temp = {"POSITION": ast.literal_eval(lines[i+1][:-1])}
        market = {}
        for item in range(NUM_ITEMS):
            market[lines[i+4+(item*5)][0:-1]] = {
                "SELL ORDERS": ast.literal_eval(lines[i+5+(item*5)][lines[i+5+(item*5)].find("{"):lines[i+5+(item*5)].find("}")+1]),
                "BUY ORDERS": ast.literal_eval(lines[i+6+(item*5)][lines[i+6+(item*5)].find("{"):lines[i+6+(item*5)].find("}")+1])
            }
        temp["MARKET"] = market
        STATE[count] = temp

        count += 1


with open("state.json", "w") as outfile:
    outfile.write(json.dumps(STATE))
