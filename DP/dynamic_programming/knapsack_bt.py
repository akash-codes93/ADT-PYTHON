"""

"""


def knapsack(items, wt):

    max_bag_value = [0]

    def looper(i, bag_wt, bag_value):

        if bag_wt > wt:
            return

        if i == len(items):
            if bag_value > max_bag_value[0]:
                max_bag_value[0] = bag_value
            return


        bag_wt += items[i][0]
        bag_value += items[i][1]
        looper(i+1, bag_wt, bag_value)
        bag_wt -= items[i][0]
        bag_value -= items[i][1]
        looper(i + 1, bag_wt, bag_value)

    looper(0,0,0)
    return max_bag_value[0]


value = knapsack([[3,30],[4,40],[5,60]], 8)
print(value)