from collections import deque


class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.cache = {}
        self.deque = deque([])

    def get(self, key: int) -> int:
        # print(self.deque)
        # print(self.cache)

        value = self.cache.get(key, None)

        if value is None:
            return -1
        else:
            self.deque.remove(key)
            self.deque.append(key)

            return value

    def put(self, key: int, value: int) -> None:

        if self.cache.get(key, None) is None:

            if len(self.deque) == self.capacity:
                oldest = self.deque.popleft()
                self.cache.pop(oldest)
        else:
            self.deque.remove(key)

        #         if self.size < self.capacity:
        #             self.size += 1

        #             if self.cache.get(key, None):
        #                 self.deque.remove(key)
        #         else:
        #             if self.cache.get(key, None) is None:
        #                 old_key = self.deque.popleft()
        #                 # print("old_key", old_key)
        #                 self.cache.pop(old_key)
        #                 # print("Sem, ", self.cache)
        #             else:
        #                 self.deque.remove(key)

        self.cache[key] = value
        self.deque.append(key)


if __name__ == '__main__':
    cache = LRUCache(2)
    # ["LRUCache", "put", "put", "put", "put", "get", "get"]
    # [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]]

    # ["LRUCache", "get", "put", "get", "put", "put", "get", "get"]
    # [[2], [2], [2, 6], [1], [1, 5], [1, 2], [1], [2]]

    cache.put(2, 6)
    print("cache- ", cache.cache)
    print("deque- ", cache.deque)
    print("#"*20)
    cache.get(1)
    print("cache- ", cache.cache)
    print("deque- ", cache.deque)
    print("#" * 20)
    cache.put(1, 5)
    print("cache- ", cache.cache)
    print("deque- ", cache.deque)
    print("#" * 20)
    cache.put(1, 2)
    print("cache- ", cache.cache)
    print("deque- ", cache.deque)
    print("#" * 20)

# ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
# [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]