class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        ret = self.storage.get(key, [])
        if len(ret) == 0:
            return ""
        l = 0
        r = len(ret)-1
        lastTimestamp = -1
        while l <= r:
            mid = (l + r) // 2
            if ret[mid][1] == timestamp:
                return ret[mid][0]
            elif ret[mid][1] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
                lastTimestamp = mid
        if lastTimestamp == -1:
            return ""
        else:
            return ret[lastTimestamp][0]

        
        
        
