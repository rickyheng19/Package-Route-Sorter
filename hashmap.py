from Package import Package

class HashMap:
    def __init__(self, packageList):
        self.packageList = packageList
        self.buckets = [[] for _ in range(len(self.packageList))]

        for package in packageList:
            key = package.package_id
            value = package
            self.add(key, value)

    # returns a hash code, O(1)
    def _hash(self, key):
        return hash(key) % len(self.packageList)
    
    # adds a key to the hashmap, O(n)
    def add(self, key, value):
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]

        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    # returns a value from a key, O(n)
    def get(self, key):
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]

        for existing_key, value in bucket:
            if existing_key == key:
                return print(value.packageInfo())

        return print("Package not found")

    # deletes a key and value, O(n)
    def delete(self, key):
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]

        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                del bucket[i]
                return

    # returns all keys and values, O(n^2)
    def get_all_Packages(self):
         for bucket in self.buckets:
            for key, package in bucket:
                print(package.packageInfo())
