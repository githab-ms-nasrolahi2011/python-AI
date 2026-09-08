from collections import OrderedDict, defaultdict
class LFUCache:
    def __init__(self, capasity):
        self.capasity = capasity
        self.main_freq = 0
        self.key_val = {}
        self.key_freq = {}
        self.freq_key = defaultdict(OrderedDict)
    def _update_freq(self, key):
        fr = self.key_freq[key]
        del self.freq_key[fr][key]
        if not self.freq_key[fr] and fr == self.main_freq:
            self.main_freq += 1
        self.key_freq[key] = fr + 1
        self.freq_key[fr + 1][key] = None
    def get(self, key):
        if key not in self.key_val:
            return -1
        else:
            value = self.key_val[key]
        self._update_freq(key)
        return value
    def put(self,key, value):
        if self.capasity == 0:
            return 
        if key in self.key_val:
            self.key_val[key] = value
            self._update_freq(key)    
        else:
            if len(self.key_val) >= self.capasity:
                old, _= self.freq_key[self.main_freq].popitem(last=False)
                del self.key_val[old]
                del self.key_freq[old]
            self.key_val[key] = value
            self.key_freq[key] = 1
            self.freq_key[1][key] = None
            self.main_freq= 1
cache = LFUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
print(cache.get(3))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
# THANK YOU TECHNOSHARIF 🧡🧡
# MOHAMMAD SOHEIL NASROLLAHI