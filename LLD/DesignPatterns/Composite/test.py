from collections import Iterable


class Test(Iterable):

    def __iter__(self):
        yield self


# test = Test()
# for i in test:
#     print(i)

from datetime import timedelta, date


class DateIterable(Iterable):

    def __init__(self, start_date, end_date):
        # initilizing the start and end dates
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        # returning __iter__ object
        return self

    def __next__(self):
        # comparing present_day with end_date,
        # if present_day greater then end_date stoping the iteration
        if self._present_day >= self.end_date:
            raise StopIteration
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today


if __name__ == '__main__':
    for day in DateIterable(date(2020, 1, 1), date(2020, 1, 6)):
        print(day)
