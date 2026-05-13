class DataAnalyser:
def **init**(self, students):
self.students = students
self.result = {}

```
def analyse(self):
    print("Not implemented — use a child class")

def print_results(self):
    for key, value in self.result.items():
        print(f"{key}: {value}")

def __str__(self):
    return f"DataAnalyser: base class, {len(self.students)} students"
```

class CountryAnalyser(DataAnalyser):
def **init**(self, students):
super().**init**(students)

```
def analyse(self):
    valid = list(filter(lambda s: s.get("country", "").strip() != "", self.students))

    country_counts = {}
    for s in valid:
        country = s["country"].strip()
        country_counts[country] = country_counts.get(country, 0) + 1

    sorted_countries = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)
    top_3 = sorted_countries[:3]

    self.result = {
        "total_students": len(self.students),
        "total_countries": len(country_counts),
        "top_3": top_3,
        "all_countries": list(country_counts.keys())
    }

def print_results(self):
    print("=" * 30)
    print("COUNTRY ANALYSIS REPORT")
    print("=" * 30)
    super().print_results()
    print("=" * 30)

def __str__(self):
    return f"CountryAnalyser: Country Analysis, {len(self.students)} students"
```
