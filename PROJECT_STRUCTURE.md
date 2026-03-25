# Project Structure & Setup Guide

## Directory Organization

```
Multi-omic-project/
│
├── 01_LITERATURE_REVIEW.md              # Comprehensive literature synthesis
├── 02_DATASETS_GUIDE.md                 # Data sourcing & validation
├── 03_METHODOLOGY_OVERVIEW.md           # Why, what, how project design
├── PROJECT_STRUCTURE.md                 # This file
│
├── notebooks/                           # Main analysis notebooks
│   ├── 01_Data_Preparation.ipynb        # QC, preprocessing, normalization
│   ├── 02_MultiOmic_Integration.ipynb   # MOFA+, cross-omic correlation
│   ├── 03_Patient_Stratification.ipynb  # Clustering, differential analysis
│   ├── 04_Mechanistic_Discovery.ipynb   # Pathways, networks, drugs
│   └── 05_ML_Prediction.ipynb           # Supervised models, interpretability
│
├── src/                                 # Reusable Python modules
│   ├── __init__.py
│   ├── data_loader.py                   # Functions to load/validate data
│   ├── preprocessing.py                 # QC, normalization, scaling
│   ├── integration.py                   # Multi-omic integration methods
│   ├── clustering.py                    # Stratification algorithms
│   ├── pathway_analysis.py              # Enrichment, networks
│   ├── ml_pipeline.py                   # Classification, interpretation
│   └── utils.py                         # Plotting, logging, helpers
│
├── data/                                # Data storage
│   ├── raw/                             # Original files (never edit)
│   │   ├── genomics/
│   │   ├── transcriptomics/
│   │   ├── proteomics/
│   │   ├── metabolomics/
│   │   └── clinical/
│   │
│   ├── processed/                       # QC & cleaned files
│   │   ├── genomics_qc.csv
│   │   ├── expression_normalized.csv
│   │   ├── metabolites_processed.csv
│   │   └── clinical_validated.csv
│   │
│   └── integrated/                      # Multi-omic integrated matrices
│       ├── mofa_factors.csv
│       ├── integrated_features.csv
│       └── patient_metadata.csv
│
├── results/                             # Analysis outputs
│   ├── qc_reports/                      # Quality control visualizations
│   ├── integration/                     # Integration analysis results
│   ├── clustering/                      # Stratification results
│   ├── enrichment/                      # Pathway, network results
│   ├── models/                          # Trained ML models
│   └── figures/                         # Publication-quality plots
│
├── dashboard/                           # Streamlit app (future)
│   ├── app.py
│   └── requirements.txt
│
├── README.md                            # Getting started guide
├── environment.yml                      # Conda environment specification
└── requirements.txt                     # Python package versions

```

---

## Setup Instructions

### 1. Create Conda Environment

```bash
# Create environment with core dependencies
conda create -n multiomics_hd python=3.10 \
  jupyter numpy pandas scipy scikit-learn \
  matplotlib seaborn plotly \
  -y

# Activate environment
conda activate multiomics_hd

# Install additional packages
pip install xgboost shap rpy2 mofa
```

### 2. Install R for Bioconductor (Optional but Recommended)

```R
# In R console
install.packages('BiocManager')
BiocManager::install(c(
  'DESeq2',
  'limma',
  'mixOmics',
  'igraph',
  'reactomePA',
  'clusterProfiler'
))
```

### 3. Verify Installation

```bash
python -c "import pandas, sklearn, xgboost; print('Python packages OK')"
```

---

## Notebook Execution Order

**Required Order (Dependencies Between Notebooks)**:

1. **01_Data_Preparation.ipynb**
   - Input: Raw multi-omic data files
   - Output: `/data/processed/` directory with QC'd data
   - Runtime: 30-45 minutes
   - Key Outputs: Data quality assessment plots, normalized matrices

2. **02_MultiOmic_Integration.ipynb**
   - Input: Processed data from notebook 1
   - Output: `/data/integrated/` with MOFA factors, cross-omic correlations
   - Runtime: 45-60 minutes
   - Key Outputs: MOFA factor loadings, cross-omic heatmaps

3. **03_Patient_Stratification.ipynb**
   - Input: Integrated data from notebook 2
   - Output: `/results/clustering/` with cluster assignments and biomarkers
   - Runtime: 30-40 minutes
   - Key Outputs: Biomarker tables, survival curves, cluster definitions

4. **04_Mechanistic_Discovery.ipynb**
   - Input: Stratification results from notebook 3 + gene lists
   - Output: `/results/enrichment/` with pathway and network analysis
   - Runtime: 45-60 minutes
   - Key Outputs: Pathway enrichment tables, network visualizations, drug targets

5. **05_ML_Prediction.ipynb**
   - Input: All processed data + subtype assignments
   - Output: `/results/models/` with trained classifiers and predictions
   - Runtime: 40-50 minutes
   - Key Outputs: Model performance metrics, SHAP explanations, risk scores

---

## Data File Specifications

### Input Data Format

**Genomics** (VCF or CSV):
```
variant_id,chr,pos,ref,alt,patient_id,genotype,effect_size
rs123456,1,1000000,A,G,patient_001,0/1,0.25
rs234567,1,1000010,C,T,patient_001,1/1,0.50
```

**Transcriptomics** (CSV with genes as rows, patients as columns):
```
gene_id,gene_name,patient_001,patient_002,patient_003
ENSG00000000003,TNNC1,100.5,95.2,110.3
ENSG00000000005,DDREAMIG,50.2,48.1,52.9
```

**Proteomics** (CSV with proteins as rows, patients as columns):
```
protein_id,protein_name,patient_001,patient_002,patient_003
PROT_001,TNNT2,2.5,2.3,2.8
PROT_002,ACTC1,3.1,2.9,3.4
```

**Metabolomics** (CSV with metabolites as rows, patients as columns):
```
metabolite_id,metabolite_name,patient_001,patient_002,patient_003
MET_001,L-Alanine,0.85,0.92,0.78
MET_002,Acetylcarnitine,0.34,0.29,0.41
```

**Clinical Data** (CSV with patient-level phenotypes):
```
patient_id,age,sex,ejection_fraction,bnp,nyha_class,outcome_status,outcome_time_days
patient_001,65,M,35,450,3,1,365
patient_002,72,F,28,820,4,1,180
patient_003,58,M,42,150,2,0,1000
```

---

## Execution Checklist

Before running notebooks, ensure:

- [ ] Conda environment created and activated
- [ ] Raw data files placed in `/data/raw/` directories
- [ ] All Python packages installed (`pip list | grep xgboost`)
- [ ] R packages installed (for Bioconductor functions)
- [ ] `/results/` subdirectories exist (or create automatically)
- [ ] Sufficient disk space: ~50 GB for intermediate files

---

## Expected Outputs Per Notebook

| Notebook | Output Files | Output Plots |
|----------|--------------|--------------|
| 01 | `*_qc.csv`, `*_normalized.csv` | QC plots, distribution plots |
| 02 | `mofa_factors.csv`, `cross_omic_corr.csv` | Factor heatmaps, integration plots |
| 03 | `cluster_assignments.csv`, biomarker tables | Heatmaps, cluster plots, volcano plots |
| 04 | Pathway enrichment tables, drug target lists | Network plots, enrichment plots |
| 05 | Trained models (.pkl), prediction matrices | ROC curves, SHAP plots, feature importance |

---

## Reproducibility Guidelines

### Version Control & Reproducibility
1. Pin all package versions in `environment.yml`
2. Set random seeds in all notebooks (line 1)
3. Document data processing decisions (comments in code)
4. Track changes with git: `git add . && git commit -m "description"`

### Random Seed Setting (Add to Every Notebook Header)
```python
import numpy as np
import random
import os

SEED = 42
np.random.seed(SEED)
random.seed(SEED)
os.environ['PYTHONHASHSEED'] = str(SEED)
```

### Documentation Standards
- **Every function**: Docstring with inputs, outputs, example
- **Every step**: Brief comment explaining what & why
- **Every output**: Interpretation in markdown cell

### Git Workflow
```bash
# Before starting work
git pull origin main

# During development (commit frequently)
git add notebooks/ src/ results/
git commit -m "Descriptive message about changes"

# After completion
git push origin main
```

---

## Package Dependencies & Versions

### Core Data Science
- numpy==1.24.0
- pandas==1.5.0
- scipy==1.9.0
- scikit-learn==1.2.0

### Machine Learning
- xgboost==1.7.0
- shap==0.41.0

### Visualization
- matplotlib==3.6.0
- seaborn==0.12.0
- plotly==5.10.0

### Bioinformatics (Optional)
- rpy2==3.13.0 (for R integration)
- mofa==1.0+ (via pip)

### Jupyter & Terminals
- jupyter==1.0.0
- jupyterlab==3.5.0
- ipykernel==6.17.0

---

## Troubleshooting

### Issue: Kernel crashes on large matrices
**Solution**: Increase available RAM, reduce N samples for initial testing

### Issue: "Module not found" errors
**Solution**: Ensure environment activated: `conda activate multiomics_hd`

### Issue: Different results across runs
**Solution**: Check random seed set at notebook top; reproducibility requires SEED=42

### Issue: Data import errors (encoding, delimiters)
**Solution**: Check file format in `01_Data_Preparation.ipynb`, use `pd.read_csv(..., sep=',', encoding='utf-8')`

---

## Contact & Support

For questions on datasets, methods, or code:
1. Check relevant documentation file (01-03_*.md)
2. Review notebook comments & markdown explanations
3. Consult references in Literature Review (01_LITERATURE_REVIEW.md)

---

**Document Version**: 1.0  
**Last Updated**: March 2026  
**Status**: Complete - Ready for Execution
