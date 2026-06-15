# 🌍 Earth System ML: Paleo Biodiversity & Ecosystem Reconstruction

---

## 🧠 Overview

This project applies machine learning techniques to fossil occurrence data from the Paleobiology Database (PBDB) to analyze biodiversity change, reconstruct ancient ecosystems, and model macroevolutionary patterns across geological time.

The goal is to demonstrate how data science and machine learning can be used in Earth system science to understand long-term biodiversity dynamics and extinction patterns.

---

## 📊 Key Results

- 📈 R² Score: 0.77  
- 📉 MAE: ~17 taxa  
- 🌍 Identified distinct paleobiogeographic ecosystem clusters  
- 🧠 Strong predictive signal from fossil occurrence density and spatial distribution  

---

## 🎯 Objectives

- Analyze biodiversity trends across geological intervals  
- Reconstruct paleoenvironments using clustering techniques  
- Model ecosystem evolution through deep geological time  
- Predict biodiversity using supervised machine learning  

---

## 📁 Dataset

**Source:** Paleobiology Database

Includes:
- Fossil occurrence records  
- Taxonomic classifications  
- Geographic coordinates (lat/lng)  
- Geological time intervals  
- Stratigraphic information  

---

## 🧪 Methodology

### 1. Data Processing
- Cleaning fossil occurrence records  
- Handling missing taxonomic and spatial data  
- Filtering geological time intervals  

### 2. Feature Engineering
- Temporal encoding of geological stages  
- Spatial coordinates (latitude, longitude)  
- Taxonomic richness metrics  
- Occurrence density features  

### 3. Machine Learning Models

**K-Means Clustering**
- Identifies paleobiogeographic ecosystem regions  

**Random Forest Regressor**
- Predicts biodiversity (taxonomic richness)  

---

## 🌍 Key Insights

- Fossil occurrence density strongly predicts observed biodiversity  
- Geographic structure influences ecosystem clustering  
- Distinct regional clusters reflect ancient paleoenvironments  
- Biodiversity varies significantly across geological stages  

---

## 📈 Visualizations

The project includes:

- Biodiversity-through-time curves  
- Paleogeographic ecosystem clustering maps  
- Feature importance analysis  
- Machine learning prediction plots  

All figures are stored in:
results/figures/


---

## 🧬 Project Structure


earth-system-ml-paleo-biodiversity/

├── data/
│ ├── raw/
│ │ ├── pbdb/
│ │ ├── gbif/
│ │ ├── macrostrat/
│ │ ├── climate_noaa/
│ │ └── marine_db/
│ └── processed/

├── notebooks/
│ ├── 01_data_exploration.ipynb
│ ├── 02_ecosystem_clustering.ipynb
│ ├── 03_ecosystem_evolution.ipynb
│ └── 04_ecosystem_ml_tracking.ipynb

├── src/
│ ├── data_processing/
│ ├── features/
│ └── models/

├── results/
│ └── figures/

├── README.md
├── requirements.txt
└── LICENSE


---

## ⚙️ Technologies Used

- Python 🐍  
- Pandas, NumPy  
- Matplotlib, Plotly  
- Scikit-learn  
- Machine Learning (Supervised + Unsupervised)  

---

## 🚀 Future Work

- Integration of climate datasets (NOAA)  
- Geological data fusion (Macrostrat)  
- Extinction event classification model  
- Time-series deep learning (LSTM / Transformers)  
- Multi-database Earth system modeling  

---

## 🧠 Interpretation

This study demonstrates that fossil occurrence density and spatial distribution are key drivers of biodiversity patterns. It also highlights the role of sampling bias and geography in paleobiological datasets.

---

## 👤 Author

Dheeraj T

---

## 📜 License

This project is licensed under the MIT License.

---

## 🔥 Summary

An end-to-end Earth system machine learning pipeline combining:

- Paleobiology  
- Data science  
- Machine learning  
- Macroevolutionary analysis  