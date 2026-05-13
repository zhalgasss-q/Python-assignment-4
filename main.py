from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import CountryAnalyser, DataAnalyser

fm = FileManager(‘students.csv’)
fm.check_file()
fm.create_output_folder()

dl = DataLoader(‘students.csv’)
dl.load()
dl.preview()

small_sample = [
{“GPA”: “3.8”, “sleep_hours”: “7”, “country”: “USA”, “final_exam_score”: “95”, “study_hours_per_day”: “4”},
{“GPA”: “2.5”, “sleep_hours”: “5”, “country”: “India”, “final_exam_score”: “72”, “study_hours_per_day”: “2”},
{“GPA”: “3.9”, “sleep_hours”: “8”, “country”: “USA”, “final_exam_score”: “98”, “study_hours_per_day”: “5”},
{“GPA”: “1.8”, “sleep_hours”: “4”, “country”: “Canada”, “final_exam_score”: “55”, “study_hours_per_day”: “1”},
{“GPA”: “3.5”, “sleep_hours”: “6”, “country”: “India”, “final_exam_score”: “88”, “study_hours_per_day”: “3”},
]

analysers = [CountryAnalyser(dl.students), DataAnalyser(small_sample)]

print(”-” * 30)
print(“Running all analysers:”)
print(”-” * 30)

for a in analysers:
print(a)
a.analyse()
a.print_results()

saver = ResultSaver(analysers[0].result, ‘output/result.json’)
report = Report(analysers[0], saver)
report.generate()
