# 🚇 Subway Station Analysis - Implementation Guide

## What I've Added to Your Notebook

I've created a complete subway station analysis workflow with **6 new cells** that will:

1. ✅ **Load subway station CSV** (auto-detects lat/long columns)
2. ✅ **Map stations to neighborhoods** (using geospatial join)
3. ✅ **Calculate subway density** per neighborhood
4. ✅ **Merge with heatmap data** for correlation analysis
5. ✅ **Analyze correlations** between subway density and prices/metrics
6. ✅ **Create enhanced heatmap** including subway density

---

## 🗂️ What You Need to Do

### Step 1: Provide the Subway CSV File

The CSV file should contain:
- **Required columns**: Latitude and Longitude (auto-detected)
- **Supported names**:
  - Latitude: `latitude`, `lat`, `Latitude`, `LAT`
  - Longitude: `longitude`, `lon`, `long`, `Longitude`, `LON`
  
- **Optional columns**: Station Name, Line, Borough, etc.

### Step 2: Place the File

Put your subway CSV in this folder:
```
/Users/yishinn/Documents/GitHub/airbnb_nyc/src/
```

Accepted filenames:
- `*subway*.csv` (e.g., `subway_stations.csv`, `nyc_subway.csv`)
- `*station*.csv` (e.g., `station_data.csv`, `transit_stations.csv`)

### Step 3: Run the Cells

The new cells will automatically:
1. Detect and load the file
2. Identify lat/long columns
3. Perform geospatial mapping
4. Calculate correlations
5. Generate the enhanced heatmap

---

## 📊 What the Analysis Will Show

### Cell 1: Load Subway Data
- Displays the file found and its structure
- Shows column names and first few records

### Cell 2: Map to Neighborhoods
- Uses geospatial join to place each subway station in a neighborhood
- Reports mapping success rate
- Flags any unmapped stations (outside NYC boundaries)

### Cell 3: Calculate Density
- Counts subway stations per neighborhood
- Shows top 10 and bottom 10 neighborhoods by station count
- Example:
  ```
  Manhattan Downtown: 45 stations
  Midtown: 38 stations
  Financial District: 28 stations
  ...
  Remote Area: 0 stations
  ```

### Cell 4: Integrate with Heatmap
- Merges subway data with existing analysis
- Shows neighborhoods with/without subway access
- Displays summary statistics

### Cell 5: Correlation Analysis
- Calculates Pearson and Spearman correlations
- Tests subway density vs:
  - Housing prices
  - Airbnb prices
  - Listing density
  - Crime metrics
  - Tree density
- Shows p-values for significance

### Cell 6: Enhanced Heatmap
- Creates 10×10 correlation matrix including subway density
- Shows how subway correlates with all other factors
- Color-coded (red=negative, blue=positive)

---

## 🔍 Key Correlations to Look For

When you run the analysis, look for these patterns:

### Likely Positive Correlations (Subway ↔ Higher Prices)
- **Airbnb Price**: Neighborhoods with subway → higher tourist demand
- **Housing Price**: Transit accessibility → premium property values
- **Listing Density**: Subway corridors → more Airbnb inventory

### Likely Negative Correlations (Subway ↔ Lower Prices)
- **Crime**: Subway corridors often pass through diverse areas (could be neutral)
- **Tree Density**: Urban areas with subway have fewer trees

### Example Expected Findings:
```
Subway Stations vs Airbnb Price:      r = +0.35 to +0.50 (positive)
Subway Stations vs Housing Price:     r = +0.40 to +0.60 (positive)
Subway Stations vs Listing Density:   r = +0.30 to +0.45 (positive)
Subway Stations vs Crime:             r = variable (depends on corridor)
Subway Stations vs Tree Density:      r = -0.20 to -0.30 (negative)
```

---

## 📝 Data Processing Steps

### Geospatial Mapping
```
Subway CSV (lat/lon) → GeoDataFrame
         ↓
Spatial Join with NYC Neighborhoods (from nycgeo.json)
         ↓
Each subway station assigned to neighborhood
```

### Density Calculation
```
Subway Stations per Neighborhood = COUNT(stations in each neighborhood)
         ↓
Result: Numerical metric (0-50 stations per neighborhood)
```

### Correlation Analysis
```
For each metric (price, crime, etc.):
  1. Get subway station counts
  2. Get metric values
  3. Calculate Pearson correlation (r)
  4. Calculate p-value (significance)
  5. Calculate Spearman correlation (rank-based)
```

---

## 🎯 Expected Output Format

When you run the cells, you'll see output like:

**Cell 1 Output:**
```
✅ Found subway data file: subway_stations.csv

Subway Station Data Shape: (472, 5)

Column Names: ['station_name', 'latitude', 'longitude', 'line', 'borough']

First few records:
   station_name  latitude  longitude  line      borough
0  Times Square    40.758   -73.986  1,2,3  Manhattan
1  Grand Central   40.753   -73.976  4,5,6  Manhattan
...
```

**Cell 2 Output:**
```
✅ Spatial join complete:
   Total subway stations: 472
   Stations mapped to neighborhoods: 468
   Unmapped stations: 4
```

**Cell 3 Output:**
```
Top 10 neighborhoods by subway station count:
   neighbourhood  subway_stations
   Midtown             45
   Downtown Manhattan  38
   ...
```

**Cell 5 Output:**
```
📊 SUBWAY STATION DENSITY CORRELATIONS:

Metric                  Pearson r  P-value  Significant
────────────────────────────────────────────────────────
Airbnb Price             0.4231   0.0012    ✓ Yes
Housing Avg Price        0.5678   0.0001    ✓ Yes
Listing Density          0.3891   0.0025    ✓ Yes
...
```

**Cell 6 Output:**
- 10×10 heatmap showing all correlations including subway density
- Subway row/column highlighted in the matrix

---

## ✅ Checklist

- [ ] Subway CSV file prepared (with lat/lon columns)
- [ ] File placed in: `/Users/yishinn/Documents/GitHub/airbnb_nyc/src/`
- [ ] File named: `*subway*.csv` or `*station*.csv`
- [ ] New cells are in notebook (6 cells added after cell 65)
- [ ] Ready to run the cells

---

## 🚀 Next Steps

1. **Prepare your subway CSV** with latitude/longitude columns
2. **Save to src folder** with appropriate naming
3. **Run the new cells** sequentially (top to bottom)
4. **Analyze the correlations** - are they significant?
5. **Interpret the heatmap** - which factors matter most?

---

## 💡 Advanced Options (Optional)

Once the basic analysis works, you could also:

1. **Calculate distance-based density**: Stations per square mile
2. **Add line analysis**: Which subway lines correlate with prices?
3. **Temporal analysis**: How subway expansion affects prices over time
4. **Accessibility score**: Weighted by number of lines at each station
5. **Commute time analysis**: If you have station-to-destination data

---

## 🐛 Troubleshooting

### "No subway data file found"
→ Check filename matches `*subway*.csv` or `*station*.csv`
→ Ensure file is in: `/Users/yishinn/Documents/GitHub/airbnb_nyc/src/`

### "Could not auto-identify lat/lon columns"
→ Rename columns to contain: `latitude`/`longitude` OR `lat`/`lon`
→ Or modify the cell to specify exact column names

### "Unmapped stations" warning
→ Normal - some stations may be just outside NYC boundaries
→ Check if they're at the edges (airport, border stations)

### "heatmap_data not found"
→ Run the comprehensive heatmap cell (cell 65) first
→ It creates the heatmap_data variable needed for integration

---

## 📚 Files Modified

- ✅ Notebook: Added 6 new cells at the end
- ✅ Documentation: This guide created

## 📄 Documentation Created

- `SUBWAY_ANALYSIS_GUIDE.md` (this file)

---

**Ready to add subway transit to your analysis! 🚇📊**

Next: Provide the subway CSV file and run the cells!
