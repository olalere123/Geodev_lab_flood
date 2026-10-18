with open('ward.csv') as f:
    lines = f.readlines()
    
for line in lines:
    print(line.strip())
    
for line in lines[1:]:
    parts = line.strip().split(",")
    ward = parts[0]
    area_km2 = float(parts[1])
    area_in_hectares = area_km2 * 100
    print(ward, "has an area of ", round(area_in_hectares, 1), "hecatres" )
    
for line in lines[1:]:
    parts = line.strip().split(",")
    ward = parts[0]
    area_km2 = float(parts[1])
    if area_km2 > 9:
        print(ward, "is large")
    else:
        print(ward, "is small")
     
for line in lines:
    parts = line.strip().split(",")
    ward = parts[0]
    area = parts[1]
    print(ward, 'has area', area)  
print('the number of lines', len(lines))