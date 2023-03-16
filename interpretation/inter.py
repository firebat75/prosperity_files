with open("print-state-v8.log", "r") as f:
    lines = f.readlines()

length = len(lines)

ban_low_sell = []
ban_high_buy = []
per_low_sell = []
per_high_buy = []

state = {}

# for i in range(len(lines)):
for i in range(50):
    lines[i] = lines[i].strip()
    print(lines[i])
    if lines[i] == "===========================================\n":
        ban_low_sell.append(lines[i+3][14:19])
        per_low_sell.append(lines[i+8][14:19])

    print(str(i) + "/" + str(length))

# for i in range(len(ban_low_sell)):
#     if ban_low_sell[i][-1] == ":":
#         ban_low_sell[i] = ban_low_sell[i][:-1]
#     ban_low_sell[i] = int(ban_low_sell[i])
#     if per_low_sell[i][-1] == ":":
#         per_low_sell[i] = per_low_sell[i][:-1]
#     per_low_sell[i] = int(per_low_sell[i])


# def clean_data(arr):
#     for i in range(len(arr)):
#         if arr[i][-1] == ":":
#             arr[i] = arr[i][:-1]
#         arr[i] = int(arr[i])
#     return arr


# ban_low_sell = clean_data(ban_low_sell)
# per_low_sell = clean_data(per_low_sell)


print("ddewdew")
print(ban_low_sell)
print(per_low_sell)
