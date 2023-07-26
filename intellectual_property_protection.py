```python
import hashlib
from datetime import datetime

class IntellectualPropertyProtection:

    def __init__(self):
        self.ip_records = {}

    def generate_hash(self, data):
        return hashlib.sha256(data.encode()).hexdigest()

    def record_ip(self, userID, data):
        hash_value = self.generate_hash(data)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.ip_records[hash_value] = {'userID': userID, 'timestamp': timestamp}

    def verify_ip(self, userID, data):
        hash_value = self.generate_hash(data)
        if hash_value in self.ip_records:
            record = self.ip_records[hash_value]
            if record['userID'] == userID:
                return True, record['timestamp']
        return False, None

# Example usage
ip_protection = IntellectualPropertyProtection()
ip_protection.record_ip('user123', 'My unique product idea')
print(ip_protection.verify_ip('user123', 'My unique product idea'))
```