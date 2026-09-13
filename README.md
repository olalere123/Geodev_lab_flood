# Lagos Coastal Corridor: Flood Hazard & Infrastructure Risk Model

A geospatial risk assessment framework evaluating coastal flood exposure (≤ 5 m inundation) on critical social infrastructure and transportation corridors across Eti-Osa, Ibeju-Lekki, and Epe LGAs in Lagos State, Nigeria.

---

## 📌 Project Overview

Coastal Lagos faces escalating threats from sea-level rise, storm surges, and tidal flooding.  
This repository contains the GIS processing workflows, spatial queries, and layer configurations used to model exposure along the newly planned **Lagos–Calabar Coastal Highway corridor**.

### Key Study Area
- **LGAs:** Eti-Osa, Ibeju-Lekki, Epe  
- **Project CRS:** EPSG:32631 (WGS 84 / UTM Zone 31N)  
- **Hazard Threshold:** Elevation ≤ 5 m above mean sea level  

---

## 📊 Data Sources

## 📊 Data Sources

| Layer Category   | Source | Dataset Format | Description |
|------------------|--------|----------------|-------------|
| **Elevation**    | [FABDEM](https://data.bris.ac.uk/data/dataset/s5hqmjcdj8yo2ibzi9b4ew3sn) | Raster GeoTIFF (30m) | Bare-earth DTM with vegetation/building canopy removed |
| **Administrative** | [geoBoundaries](https://www.geoboundaries.org/countryDownloads.html) | Vector Shapefile/GeoPackage | Nigeria ADM2 boundary polygons (LGAs) |
| **Infrastructure (Health)** | [GRID3 Health Facilities](https://data.grid3.org/datasets/GRID3::grid3-nga-health-facilities-v2-0/about) | Vector Points | Geo-referenced health facility locations (2024 release) |
| **Infrastructure (Schools)** | [GRID3 Schools](https://data.grid3.org/datasets/GRID3::grid3-nga-schools/about) | Vector Points | Nigeria school datasets |
| **Population**   | [GRID3 Population](https://data.grid3.org/maps/6966d625aea0488496d01debd3bb80f9/about) | Raster/Vector | Gridded population estimates (2025 release) |
| **Transport**    | OpenStreetMap (OSM) | Vector Line | Major highways, expressways, and coastal bridge alignments |
| **Humanitarian Infrastructure** | [HOTOSM](https://data.humdata.org/) | Vector Points | Additional school and health facility datasets from HOTOSM |

---

## ⚙️ Workflow & Methodology

1. **Data Preprocessing & Mosaic**
   - Download FABDEM tiles `N06E003` and `N06E004`
   - Merge adjacent tiles into a seamless continuous elevation surface
   - Reproject and clip the mosaic to the 3-LGA project boundary in `EPSG:32631`

2. **Flood Hazard Mask Generation**
   - Execute conditional raster math to isolate critical low-elevation terrain:  
     ```
     Flood_Mask = ("FABDEM_Clipped@1" <= 5)
     ```
   - Polygonize the binary raster mask to generate vector hazard zones

3. **Exposure & Proximity Analysis**
   - Filter transport layers using SQL expressions:  
     ```
     "highway" IN ('trunk', 'primary', 'secondary')
     ```
   - Execute spatial joins (`ST_Intersects` / `Select by Location`) between infrastructure points and the 5 m hazard polygon layer
   - Generate multi-ring buffer zones (1 km, 3 km, 5 km) along the coastal highway alignment to measure asset density within the hazard zone

---

## 📂 Project Directory Layout

```text
├── data/
│   ├── raw/              # FABDEM tiles, OSM raw extracts, boundaries
│   └── processed/        # Clipped DEM, reprojected layers, 5m flood mask
├── maps/                 # High-resolution map exports (PNG/PDF)
├── scripts/              # Python / GeoPandas processing scripts
└── qgis/                 # QGIS project file (.qgz) and custom QML styles
