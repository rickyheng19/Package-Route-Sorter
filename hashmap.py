#Code referenced from this video: https://www.youtube.com/watch?v=9HFbhPscPU0

class HashMap:
        #Constructor. Creates an array to store data.
        def __init__(self):
                self.size = 64
                self.map = [None] * self.size
		
        #Takes a key, turns it into an index and returns it
        def _get_hash(self, key):
                hash = 0
                for char in str(key):
                        hash += ord(char)
                return hash % self.size
        
		#Gets index from get_hash function. Make list from key and value
        def add(self, key, value):
                key_hash = self._get_hash(key)
                key_value = [key, value]
                #if key_hash list is empty, insert the key and value provided
                if self.map[key_hash] is None:
                        self.map[key_hash] = list([key_value])
                        return True
                #else if key exist, then just update with value provided
                else:
                        for pair in self.map[key_hash]:
                                if pair[0] == key:
                                        pair[1] = value
                                        return True
                        self.map[key_hash].append(key_value)
                        return True
		#get value of key provided	
        def get(self, key):
                key_hash = self._get_hash(key)
                if self.map[key_hash] is not None:
                        for pair in self.map[key_hash]:
                                if pair[0] == key:
                                        return pair[1]
                return None
		#Delete key
        def delete(self, key):
                key_hash = self._get_hash(key)
		
                if self.map[key_hash] is None:
                        return False
                for i in range (0, len(self.map[key_hash])):
                        if self.map[key_hash][i][0] == key:
                                self.map[key_hash].pop(i)
                                return True
                return False
	
        def keys(self):
                arr = []
                for i in range(0, len(self.map)):
                        if self.map[i]:
                                arr.append(self.map[i][0])
                return arr
			
        def print(self):
                print('---PHONEBOOK----')
                for item in self.map:
                        if item is not None:
                                print(str(item))