import json

class ResultSaver:
def **init**(self, result, path):
self.result = result
self.path = path

```
def save_json(self):
    try:
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(self.result, f, indent=4)
        print(f"Result saved to {self.path}")
    except Exception as e:
        print(f"Error saving file: {e}")
```
