"""
Input:
[
    [17, 2, 17],
    [16, 1, 5],
    [14, 3,  9]
]
"""
import sys


class Solution1:
    """Producing all the cases"""
    n = 3
    no_of_colors = 3

    def paint_houses(self, price_schema, color_order, house_index, cost, min_cost):

        if house_index == self.n:
            print("Color order: ", color_order, cost)
            if cost <= min_cost:
                min_cost = cost

            return min_cost

        for color_index in range(0, self.no_of_colors):

            if (house_index == 0) or color_index != color_order[house_index - 1]:
                cost += price_schema[house_index][color_index]
                color_order.append(color_index)

                min_cost = self.paint_houses(price_schema, color_order, house_index + 1, cost, min_cost)

                cost -= price_schema[house_index][color_index]
                color_order.pop()

        return min_cost


schema = [
    [1, 2, 17],
    [16, 16, 5],
    [14, 3, 9]
]


least_cost = Solution1().paint_houses(schema, [], 0, 0, 999999)
print(least_cost)
