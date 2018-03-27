from datetime import  datetime
import time


class PartialDict(dict):

    # default initialization
    def __init__(self):

        # to maintain the time stamp
        self.timestamp = {}

        # to main the records
        self.val = {}

        super().__init__(self)

    # to get the historical read
    def hist_read(self, key, timestamp):

        __length = len(self.timestamp.get(key, []))

        for __counter, __time in enumerate(self.timestamp.get(key, [])):

            if __time < timestamp:
                continue
            else:

                return self.val.get(key,[])[__counter]

        return self.val.get(key, [])[__length-1]

    # to update the value of the dictionary
    def update(self, __m, **kwargs):

        for key, values in __m.items():
            # self.timestamp.get(key, []).append(localtime)
            # self.val.get(key, []).append(values)
            if key in self.timestamp.keys():
                self.timestamp[key].append(datetime.now())
                self.val[key].append(values)
            else:
                self.timestamp[key], self.val[key] = [], []
                self.timestamp[key].append(datetime.now())
                self.val[key].append(values)


        super().update(__m, **kwargs)


if __name__ == '__main__':

    _dict = PartialDict()

    _dict.update({
        'a': 1
    })

    time.sleep(10)

    _dict.update({
        'a' : 2
    })

    time.sleep(10)

    _dict.update({
        'a': 15
    })

    time.sleep(10)

    print(_dict.hist_read('a' , datetime.now()))

    print(_dict.timestamp)
    print(_dict.val)