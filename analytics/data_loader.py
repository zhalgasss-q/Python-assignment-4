import csv

class DataLoader:
def **init**(self, path):
self.path = path
self.students = []

```
def load(self):
    try:
        with open(self.path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            self.students = [row for row in reader]
        print(f"Loaded {len(self.students)} students")
    except Exception as e:
        print(f"Error loading file: {e}")

def preview(self):
    print("Preview (first 3 rows):")
    for row in self.students[:3]:
        print(row)
```
