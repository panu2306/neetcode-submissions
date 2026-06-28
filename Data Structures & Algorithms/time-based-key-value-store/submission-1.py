from collections import defaultdict

class TimeMap:

    def __init__(self):
        # {
        #     key1: [{ts1: 'happpy'}, {ts2: 'sad'}],
        #     key2: [{ts1: 'happpy'}, {ts2: 'sad'}]
        # }
        self.time_map = defaultdict(list)


        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append({timestamp: value})
        
    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.time_map[key]
        l, r = 0, len(timestamps) - 1
        result = ""
        while l <= r: 
            mid = (l + r) // 2 
            ts, val = next(iter(timestamps[mid].items()))
            
            if timestamp == ts: 
                return val  
            elif timestamp > ts:
                result = val  
                l = mid + 1
            else: 
                r = mid - 1 
        
        return result  
        
