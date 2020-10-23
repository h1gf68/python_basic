# строго не судите за нечитабельный код, время было ограничено

firms_list = [{}, {}]
all_profit = 0
num_profit = 0
with open("task7_firms", "r") as firms:
    for line in firms:
        tmp_list = line.split()
        profit = float(tmp_list[2]) - float(tmp_list[3])
        firms_list[0][tmp_list[0]] = profit
        if profit > 0:
            num_profit += 1
            all_profit += profit
        else:
            firms_list[1][tmp_list[0]] = profit
    firms_list[1]["average_profit"] = all_profit / num_profit

print(firms_list)
