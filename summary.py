import csv

def read_rows(filename):
    with open(filename, encoding= 'utf-8-sig') as f:
        return(list(csv.DictReader(f)))
    

def clean_values(rows, column):
    values =[]
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
    return(values)


def summarize(values):
    if len(values) == 0:
        return{"count":0, "smallest": None, 'largest': None, "average": None}
    return{
        "smallest": min(values),
        "largest": max(values),
        "count": len(values),
        "average": sum(values) / len(values)
    }

def summarize_all(filename, columns):
    rows = read_rows(filename)
    report = {}
    for column in columns:
        values = clean_values(rows, column)
        report[column] = summarize(values)
    return(report)

report = summarize_all('state_pops.csv', ["population"])

for column, stats in report.items():
    print(column, "->", stats)



rows = read_rows('state_pops.csv')
values = clean_values(rows, "population")
summary = summarize(values)
print(summary)
    