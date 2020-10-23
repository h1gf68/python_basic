with open("task3_workers", "r") as workers:
    n = 0
    sum = 0
    for worker in workers.readlines():
        n += 1
        if int(worker.split()[1]) >= 20000:
            print(worker.split()[0] + " has an income of more than 20000")
        sum += int(worker.split()[1])
    print("-" * 40)
    print(f"Average income of the employees: {sum / n}")
