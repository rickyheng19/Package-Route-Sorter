# code referenced from https://www.youtube.com/watch?v=9HFbhPscPU0&ab_channel=JoeJames

# Hash Map
class HashMap:
    def __init__(self):
        # Initialize the size of the hash map and create an empty array to store data
        self.size = 50
        self.map = [None] * self.size
        
    def _get_hash(self, key):
        # Calculate the hash value for a given key by summing the ASCII values of its characters
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size  # Ensure the hash fits within the size of the map
        
    def add(self, key, value):
        # Add a key-value pair to the hash map
        key_hash = self._get_hash(key)
        key_value = [key, value]
        
        if self.map[key_hash] is None:
            # If the slot at the hash index is empty, create a new list for the key-value pair
            self.map[key_hash] = list([key_value])  # type: ignore
            return True
        else:
            # If the slot is not empty, search for the key and update its value if found,
            # or add a new key-value pair if the key is not already present
            for pair in self.map[key_hash]:  # type: ignore
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)  # type: ignore
            return True
    
    def get(self, key):
        # Retrieve the value associated with a given key from the hash map
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:  # type: ignore
                if pair[0] == key:
                    return pair[1]
        return None
    
    def delete(self, key):
        # Delete a key-value pair from the hash map
        key_hash = self._get_hash(key)
        
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):  # type: ignore
            if self.map[key_hash][i][0] == key:  # type: ignore
                self.map[key_hash].pop(i)  # type: ignore
                return True
        return False
    
    def keys(self):
        # Retrieve a list of all keys present in the hash map
        arr = []
        for i in range(0, len(self.map)):
            if self.map[i]:
                arr.append(self.map[i][0])  # type: ignore
        return arr
    
    def printContents(self):
        # Print the contents of the hash map
        print("All Packages")
        for item in self.map:
            if item is not None:
                print(str(item))
			

			
