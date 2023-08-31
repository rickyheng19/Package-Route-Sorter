from Package import Package

class HashMap:
    def __init__(self, packageList):
        self.packageList = packageList
        self.buckets = [[] for _ in range(len(self.packageList))]

        for package in packageList:
            key = package.package_id
            value = package
            self.add(key, value)

    def _hash(self, key):
        return hash(key) % len(self.packageList)

    def add(self, key, value):
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]

        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key):
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]

        for existing_key, value in bucket:
            if existing_key == key:
                return value.packageInfo()

        return "Package not found"

    def delete(self, key):
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]

        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                del bucket[i]
                return

    def get_all_Packages(self):
         for bucket in self.buckets:
            for key, package in bucket:
                package.packageInfo()
