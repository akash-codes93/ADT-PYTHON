# cook your dish here
withdraw, total = map(float, input().strip().split())

withdraw = int(withdraw)
# total = float(total)


def output():
    if withdraw >= total:
        print(total)
        return None

    if withdraw % 5 != 0:
        print(total)
        return None

    remaining = total - withdraw
    remaining = remaining - 0.5

    if remaining < 0:
        print(total)
        return None
    else:
        print(remaining)
        return None

output()