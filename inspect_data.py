# import csv

# with open('states_pop.csv', encoding='utf-8-sig') as f:
#     reader = csv.DictReader(f)
#     rows = list(reader)
 
# values = []
# for row in rows:
#     raw = row["population"].strip()
#     if raw == "":
#         continue
#     values.append(float(raw))
    
# print(values)

import csv

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    values =[]
    for row in rows :
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
        
    return{
        "smallest": min(values),
        "largest": max(values),
        "count": len(values)
    }
    
result = inspect_column("states_pop.csv", "population")

print(result)       
