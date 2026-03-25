# Multi-Omic Stratification for Heart Disease: Methodology & Overview

## Executive Summary

This project develops a **multi-omic machine learning system** to stratify heart disease patients into molecularly-defined subtypes and predict patient-specific treatment responses. Rather than treating all heart disease as a single entity, we integrate genomics, transcriptomics, proteomics, and metabolomics to identify distinct disease pathway signatures that guide precision therapeutics.

---

## PART 1: WHY THIS PROJECT?

### 1.1 The Problem: One-Size-Fits-All Approach Fails

**Current Clinical Reality:**
- Heart disease affects 17.9 million people globally (WHO, 2021)
- Standard treatment: ACE inhibitors, beta-blockers, diuretics for all HF patients
- Problem: Only 40-60% respond favorably to these "standard" therapies
- Result: Progressive disease, hospitalizations, reduced quality of life

**Why One-Size-Fails:**
Heart disease is **clinically and molecularly heterogeneous**:
- Different etiologies (ischemic, inflammatory, genetic, metabolic, toxic)
- Different phenotypes (systolic vs diastolic dysfunction, acute vs chronic)
- Different underlying pathway dysregulation
- → **Same treatment doesn't work for everyone**

**Example**: Two patients with identical EF of 35% may have:
- Patient A: Defective mitochondrial energy metabolism → needs CoQ10, alpha-lipoic acid
- Patient B: Excessive inflammatory signaling → needs IL-6 inhibitor, TNF-alpha antagonist
- Patient C: Genetic channelopathy → needs specific channel blocker + genetic counseling

**Clinical Impact of Better Stratification:**
- Studies show molecular subtyping improves treatment response prediction by 25-40%
- Prevents inappropriate therapy escalation (e.g., inotropes for certain subtypes worsen outcomes)
- Enables early detection of high-risk progression

---

### 1.2 Why Multi-Omics?

**Historical Limitation: Single-Omic Approaches**
| Approach | Shows | Misses |
|----------|-------|--------|
| Genetics alone | Disease susceptibility (30% heritable) | Actual disease mechanism, environmental triggers |
| Genomics | Which genes are mutated | Are mutations actually expressed? Functional consequence? |
| Transcriptomics | Which genes are dysregulated | Are proteins actually translated? Post-translational modifications? |
| Proteomics | Protein abundance changes | Source? Metabolic basis? Drug-target interactions? |
| Metabolomics | Biochemical dysfunction | What genes/proteins cause it? |

**Multi-Omics Advantage:**
Integrating all layers creates a **molecular systems view**:
- Genetic predisposition → gene expression changes → protein alterations → metabolic dysfunction → clinical phenotype
- Identify causality (not just correlation)
- Discover bottleneck nodes amenable to therapeutic intervention
- More predictive than any single omic layer

**Quantified Benefit:**
- Single-omic ML model AUC: 0.75-0.80
- Multi-omic integrated model AUC: 0.88-0.93
- **~10-15% absolute improvement in discrimination**

---

### 1.3 Why Now?

**Enabling Technologies & Data Abundance:**
- RNA-seq and whole exome sequencing now cost-effective ($500-2000/sample)
- High-throughput proteomics (mass spec, aptamer assays) scale to thousands
- Metabolomics platforms mature and standardized (NMR, LC-MS)
- Large public omics datasets available: GTEx, UK Biobank, TCGA
- ML methods for heterogeneous data integration established (MOFA, iCluster, mixOmics)

**Regulatory Momentum:**
- FDA guidance on Precision Medicine (2013, updated 2021)
- CMS reimbursement for genetic testing and biomarker-guided therapy increasing
- Clinical trials increasingly use molecular subtypes for stratification

---

### 1.4 Personal Motivation

In your previous heart disease project, you established:
✓ Understanding of cardiovascular biology and clinical phenotyping  
✓ Feature engineering and ML model development  
✓ Domain knowledge to communicate findings to clinicians  
✓ Foundation in epidemiological/clinical prediction modeling  

**This project represents a major upgrade by:**
- Adding **multi-omics integration** (single-omic → 4-layer molecular systems view)
- Shifting from **association to mechanism** (which pathways drive phenotypes? why?)
- Building **production-grade pipeline** (reproducible, scalable, interpretable)
- Creating **precision medicine actionability** (not just risk prediction)

---

## PART 2: WHAT THIS PROJECT DOES

### 2.1 Project Scope

**Input**: Multi-omic data from heart disease patients
```
Patient 1:
  ├─ Genomics: 20,000 SNVs, 50 rare variants, 5 copy number variants
  ├─ Transcriptomics: 20,000 mRNA expression levels
  ├─ Proteomics: 5,000 protein expression + phosphorylation
  ├─ Metabolomics: 250 metabolite concentrations
  └─ Clinical: EF, BNP, NYHA class, outcomes, medications
```

**Processing & Analysis**:
1. Quality control and harmonization across omics layers
2. Data integration (coordinate omics dimensions to same patient-feature space)
3. Unsupervised discovery (identify natural patient clusters)
4. Supervised classification (map clusters to clinical outcomes & phenotypes)
5. Mechanistic interpretation (identify causal drivers per subtype)
6. Drug target prioritization (which genes to target per subtype)

**Output**: Patient stratification + treatment predictions
```
Patient A → Subtype_Metabolic (80% confidence)
  ├─ Key biomarkers: ↓ NAD+, ↑ lactate, ↑ BCAA, ↓ carnitines
  ├─ Dysregulated pathway: Mitochondrial oxidative phosphorylation
  ├─ Treatment recommendation: CoQ10, beta-blocker, beta-3 agonist
  └─ Risk score: High (82nd percentile)

Patient B → Subtype_Inflammatory (92% confidence)
  ├─ Key biomarkers: ↑ IL-6, ↑ TNF-alpha, ↑ CRP, activated immune cells
  ├─ Dysregulated pathway: NF-kB inflammatory signaling
  ├─ Treatment recommendation: IL-6 antagonist, immunosuppression
  └─ Risk score: Very High (95th percentile)
```

### 2.2 Subtypes We'll Identify

Based on literature and preliminary analysis, we expect 3-5 major subtypes:

#### Subtype 1: Ischemic-Driven
- **Signature**: Hypoxia-responsive genes, mitochondrial dysfunction
- **Key Pathways**: HIF-1 signaling, glycolytic switch, energy starvation
- **Biomarkers**: Troponin, myoglobin, lactate, ↓ ATP
- **Treatment**: Revascularization, reperfusion therapy, energetic support

#### Subtype 2: Inflammatory-Driven
- **Signature**: Immune activation, cytokine upregulation
- **Key Pathways**: NF-kB, NLRP3 inflammasome, Th17 differentiation
- **Biomarkers**: IL-6, TNF-alpha, CRP, neutrophil/lymphocyte ratio
- **Treatment**: Anti-inflammatory (IL-6i, TNFi), immunosuppression

#### Subtype 3: Metabolic-Lipotoxic
- **Signature**: Altered lipid metabolism, mitochondrial lipid accumulation
- **Key Pathways**: PPARα/γ signaling, steatosis, oxidative stress
- **Biomarkers**: ↑ Triglycerides, ↓ HDL, ceramides, lipid peroxides
- **Treatment**: PPAR agonists, lipid lowering, antioxidants

#### Subtype 4: Fibrotic-Structural
- **Signature**: Excessive collagen deposition, TGF-β signaling
- **Key Pathways**: TGF-β/SMAD, fibroblast activation, epithelial-mesenchymal transition
- **Biomarkers**: Soluble ST2, galectin-3, collagen I/III ratio, procollagen peptides
- **Treatment**: SGLT2i, aldosterone antagonists, antifibrotic agents

#### Subtype 5: Genetic (Optional, Disease-Specific)
- **Signature**: Monogenic cardiomyopathy variants
- **Key Pathways**: Sarcomeric dysfunction, calcium handling
- **Biomarkers**: Specific truncating mutations, genetic score
- **Treatment**: Gene therapy (future), specific channel blockers, family screening

### 2.3 Clinical Outputs

**Per Individual Patient:**
1. **Subtype Classification** + confidence score
2. **Prognostic Risk Stratification** (risk score for 1, 3, 5-year outcomes)
3. **Recommended Treatments** (ranked by evidence & mechanism match)
4. **Key Biomarkers** (what's driving their disease?)
5. **Mechanistic Explanation** (why they have this subtype)

**Population-Level:**
1. **Subtype Prevalence** across cohorts
2. **Demographic/Ancestry Distribution**
3. **Outcome Disparities** (disparities between groups)
4. **Drug Response Patterns** (which subtypes benefit from which drugs)

---

## PART 3: HOW WE'LL BUILD IT

### 3.1 Technical Architecture

```
┌─────────────────────────────────────────────────────────────┐
│ DATA LAYER (Multi-Omics Integration)                        │
├─────────────────────────────────────────────────────────────┤
│ Genomics (Python: PyVCF, plink)                            │
│ Transcriptomics (R: DESeq2, limma)                         │
│ Proteomics (Python: scikit)                                 │
│ Metabolomics (R: metaboAnalyst)                            │
│ Clinical Data (Pandas, SQL)                                │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│ PREPROCESSING LAYER (QC & Harmonization)                    │
├─────────────────────────────────────────────────────────────┤
│ Feature quality assessment                                  │
│ Batch effect correction (ComBat, Harmony)                  │
│ Missing data imputation                                     │
│ Normalization & scaling                                     │
│ Feature selection & dimensionality reduction               │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│ INTEGRATION LAYER (Multi-Omic Fusion)                       │
├─────────────────────────────────────────────────────────────┤
│ Methods: MOFA+, iCluster, mixOmics, netZooPy               │
│ Output: Integrated latent factor space                      │
│         Cross-omic correlation networks                     │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│ DISCOVERY LAYER (Unsupervised Learning)                     │
├─────────────────────────────────────────────────────────────┤
│ Clustering (K-means, hierarchical, consensus clustering)   │
│ Visualization (PCA, t-SNE, UMAP)                           │
│ Output: Patient clusters / putative subtypes               │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│ VALIDATION LAYER (Supervised Classification)                │
├─────────────────────────────────────────────────────────────┤
│ Supervised ML: Random Forest, XGBoost, SVM                 │
│ Outcome prediction: mortality, hospitalization, HF class   │
│ Feature importance: SHAP, permutation importance           │
│ Cross-validation: 5-fold stratified CV                     │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│ INTERPRETATION LAYER (Mechanistic Understanding)            │
├─────────────────────────────────────────────────────────────┤
│ Pathway enrichment (GSEA, Reactome)                        │
│ Network analysis (igraph, Cytoscape)                       │
│ Causal inference (MR, instrumental variables)             │
│ Drug target mapping (DrugBank, ChEMBL)                    │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│ DEPLOYMENT LAYER (Clinical Tool)                           │
├─────────────────────────────────────────────────────────────┤
│ Streamlit dashboard for single-patient predictions         │
│ Django REST API for EHR integration                        │
│ Output: Subtype + treatment recommendations               │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Technology Stack

#### Data Processing & Analysis
- **Python 3.10+**: pandas, numpy, scipy, scikit-learn
- **R 4.2+**: Bioconductor packages (DESeq2, limma, mixOmics, igraph)
- **Jupyter Notebooks**: Reproducible analysis & documentation

#### Multi-Omics Integration
- **MOFA+** (Multi-Omics Factor Analysis): Identify shared/unique factors across omics
- **mixOmics**: Partial least squares (PLS) integration
- **Harmony**: Batch effect correction across omics
- **PyMCA** or **Python-igraph**: Network integration

#### Machine Learning
- **scikit-learn**: Unsupervised (clustering), supervised (classification)
- **XGBoost**: Gradient boosting for feature importance
- **SHAP**: Model interpretability (Shapley values)

#### Visualization & Dashboard
- **Streamlit**: Interactive web app for single-patient predictions
- **Plotly/ggplot2**: Publication-grade plots
- **Cytoscape** or **igraph**: Network visualization

#### Statistical Methods
- **Statsmodels**: Statistical testing, effect size
- **rpy2**: Call R functions from Python (Bioconductor integration)

---

### 3.3 Project Workflow (Step-by-Step)

#### **Phase 1: Data Preparation (Week 1-2)**
```
Step 1.1: Download & organize multi-omic data
  - GTEx heart tissue (genomics + transcriptomics)
  - Metabolomic data (via literature download)
  - Clinical phenotypes (curated)
  Output: /data/raw/ directory with organized files

Step 1.2: Data quality control
  - Genomics: Call rates, HWE, MAF filtering
  - Transcriptomics: Alignment quality, expression level cutoffs
  - Metabolomics: Detection rates, outlier removal
  - Clinical: Missing data assessment, phenotype validation
  Output: /data/qc_reports/ with figures

Step 1.3: Data preprocessing & normalization
  - Genomics: PCA (population stratification), Hardy-Weinberg QC
  - Transcriptomics: TMM normalization, log2 transformation
  - Metabolomics: Pareto scaling, log transformation
  - Clinical: StandardScaler for continuous, LabelEncoder for categorical
  Output: /data/processed/ with normalized matrices
```

#### **Phase 2: Multi-Omic Integration (Week 3-4)**
```
Step 2.1: Feature selection per omic layer
  - Genomics: Polygenic risk score (PRS) calculation, rare variant aggregation
  - Transcriptomics: Highest variance genes (top 5K), pathway-level aggregation
  - Metabolomics: All metabolites + pathway scores
  - Clinical: Relevant cardiac phenotypes
  Output: Feature matrices for each omic in common patient space

Step 2.2: Multi-omic integration
  - Run MOFA+: Identify shared factors across omics
  - Output: Latent factor scores per patient
  - Output: Cross-omic loadings (which features load on each factor)
  Output: /results/integration/ with factor plots

Step 2.3: Integration validation
  - Do integrated factors correlate with outcomes?
  - Cross-validation of factor stability
  Output: Validation metrics, robustness assessment
```

#### **Phase 3: Patient Stratification (Week 5-6)**
```
Step 3.1: Unsupervised clustering
  - Apply K-means to integrated factor space (K = 3, 4, 5)
  - Consensus clustering to determine optimal K
  - Hierarchical clustering for structure
  Output: Patient cluster assignments + dendrogram

Step 3.2: Cluster characterization
  - Differential expression per cluster (edgeR, limma)
  - Differential abundance per metabolite (t-test with correction)
  - Identify biomarker signature per cluster
  - Output: Biomarker tables, volcano plots

Step 3.3: Cluster validation
  - Do clusters predict clinical outcomes? (Cox regression)
  - Are clusters reproducible in independent cohort? (external validation)
  - Are clusters clinically meaningful? (expert review)
  Output: Survival curves, clinical interpretation
```

#### **Phase 4: Mechanistic Discovery (Week 7-8)**
```
Step 4.1: Pathway enrichment analysis
  - For each cluster, find enriched pathways (GSEA, Reactome)
  - Identify top dysregulated pathways per subtype
  - Output: Pathway enrichment tables, pathway heatmaps

Step 4.2: Network analysis
  - Build protein interaction network from dysregulated proteins
  - Calculate network metrics (centrality, betweenness)
  - Identify hub genes (candidate drug targets)
  - Output: Network plots, hub gene lists

Step 4.3: Drug target identification
  - Map dysregulated genes to FDA-approved drugs (DrugBank)
  - Rank drug targets by mechanism relevance
  - Output: Drug recommendation tables per subtype
```

#### **Phase 5: Supervised Classification & Prediction (Week 9-10)**
```
Step 5.1: Train supervised models
  - Input: Individual omic features (genomics, transcriptomics, proteomics, metabolomics)
  - Target: Cluster assignment (subtype)
  - Algorithm: Random Forest, XGBoost, SVM
  - Validation: 5-fold cross-validation
  Output: Trained models, cross-validation metrics (AUC, F1, sensitivity/specificity)

Step 5.2: Outcome prediction
  - Train models for clinical outcomes (mortality, HF hospitalization, progression)
  - Input: Subtype assignment + key biomarkers
  - Output: Risk scores per outcome
  - Validation: C-statistic, calibration plots

Step 5.3: Feature importance & interpretability
  - SHAP values: Why did model assign patient to subtype X?
  - Permutation importance: Which features most predictive?
  - Output: Feature importance plots, SHAP dependence plots
```

#### **Phase 6: Reproducible Visualization & Dashboard (Week 11-12)**
```
Step 6.1: Publication-quality figures
  - Multi-omic integration visualization (PCA, t-SNE)
  - Subtype definition (cluster plots, biomarker heatmaps)
  - Outcome prediction (ROC, calibration, risk stratification)
  - Network visualization (dysregulated pathways)

Step 6.2: Interactive Streamlit dashboard
  Structure:
  ├─ Patient Input (multi-omic profile)
  ├─ Subtype Prediction (% confidence per subtype)
  ├─ Risk Stratification (mortality/HF risk scores)
  ├─ Biomarker Panel (key dysregulations)
  ├─ Treatment Recommendations (ranked by mechanism)
  └─ Mechanistic Explanation (pathway summary + visualizations)

Step 6.3: Code documentation & publication prep
  - Jupyter notebooks with narrative + code
  - README with reproducibility instructions
  - Methods section for potential manuscript
```

---

### 3.4 Key Deliverables

| Deliverable | Format | Purpose |
|-------------|--------|---------|
| Literature Review | Markdown | Conceptual foundation & prior work |
| Dataset Documentation | Markdown | Data sourcing & validation |
| Methodology Document | This document | Project rationale & approach |
| Data Processing Notebook | Jupyter (Python) | QC, preprocessing, normalization |
| Integration Notebook | Jupyter (Python/R) | MOFA+, cross-omic correlation |
| Stratification Notebook | Jupyter (Python) | Clustering, differential analysis, validation |
| Discovery Notebook | Jupyter (Python/R) | Pathway enrichment, network analysis |
| ML/Prediction Notebook | Jupyter (Python) | Supervised models, SHAP interpretation |
| Streamlit Dashboard | Python app | Interactive single-patient predictions |
| Final Report | PDF/HTML | Manuscript-ready summary |

---

## PART 4: SUCCESS CRITERIA & EXPECTED OUTCOMES

### 4.1 Quantitative Benchmarks

| Metric | Baseline | Target | Source |
|--------|----------|--------|--------|
| Unsupervised clustering silhouette score | N/A | > 0.5 | Cluster quality |
| Supervised model AUC (cross-validated) | 0.75 | > 0.88 | Literature benchmark |
| Outcome prediction C-statistic | 0.70 (clinical model) | > 0.80 | Portfolio validation |
| Biomarker overlap (literature vs discovered) | 0.40 | > 0.70 | Validation against known subtypes |
| Pathway enrichment p-value (significant pathways) | N/A | FDR < 0.05 | Statistical threshold |

### 4.2 Qualitative Milestones

✓ **Interpretability**: Can a cardiologist read output and understand the result?  
✓ **Novelty**: Do subtypes reveal new biological insights beyond prior literature?  
✓ **Reproducibility**: Can another researcher run pipeline and get same results?  
✓ **Actionability**: Does each subtype have drug targets with existing/upcoming therapies?  
✓ **Scalability**: Can pipeline run on new patient data in <5 minutes?

### 4.3 Research Impact

**Short-term (This Project):**
- Proof-of-concept that multi-omics improves HF stratification over traditional phenotyping
- Identification of 3-5 clinically meaningful molecular subtypes
- Demonstration of mechanistic understanding (genes → pathways → treatment)

**Medium-term (1-2 Years):**
- Validation in independent cohorts (e.g., UK Biobank HF cases)
- Integration with EHR system for prospective patient recruitment
- Preliminary clinical trial design per subtype

**Long-term (2+ Years):**
- FDA approval of diagnostic test (subtype classification)
- Precision medicine HF trials stratified by molecular subtype
- Patient stratification tool integrated into cardiology practice

---

## PART 5: TIMELINE & RESOURCE REQUIREMENTS

### 5.1 Development Timeline
- **Week 1-2**: Data preparation
- **Week 3-4**: Multi-omics integration
- **Week 5-6**: Patient stratification & biomarker discovery
- **Week 7-8**: Mechanistic pathway analysis
- **Week 9-10**: Supervised ML & risk prediction
- **Week 11-12**: Dashboard, documentation, manuscript prep

**Total Timeline**: 12 weeks (3 months)

### 5.2 Computing Resources
- **CPU**: 4+ cores recommended
- **RAM**: 16+ GB (for large omics matrices)
- **Storage**: 100 GB (raw data + outputs)
- **Software**: Linux/macOS preferred (for Bioconductor); Windows with WSL acceptable

### 5.3 Skills & Background
✓ Python programming (pandas, scikit-learn)  
✓ R programming (Bioconductor, ggplot2)  
✓ Statistics (hypothesis testing, machine learning evaluation)  
✓ Biological interpretation (pathway analysis, mechanism of disease)  
✓ Data visualization  
✗ Advanced: Deep learning not required (traditional ML sufficient)  

---

## PART 6: RISKS & MITIGATION

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Small sample size (GTEx ~400 heart samples) | Low statistical power | Use elastic net for feature selection; external validation in UK Biobank |
| Batch effects dominate biology | False subtypes | Pre-register analysis plan; use multiple batch correction methods |
| Subtypes don't align with outcomes | Not clinically useful | Cross-validate with independent outcomes; expert clinician review |
| Data privacy concerns (clinical data) | Regulatory issues | Use synthetic data if needed; IRB approval for real data |
| Reproducibility issues | Cannot replicate results | Containerize code (Docker); version all packages; seed all RNGs |

---

## PART 7: WHY THIS APPROACH IS NOVEL & IMPACTFUL

**vs. Previous HF Prediction Studies:**
- ✓ Multi-omic integration (not single-omics)
- ✓ Mechanistic explanation (not just black-box prediction)
- ✓ Actionable drug recommendations (not just prognosis)
- ✓ Interactive dashboard (not just academic paper)

**vs. Your Prior Work:**
- ✓ Deeper molecular mechanistic focus
- ✓ Production-grade code & reproducibility
- ✓ Clinical actionability (treatment guidance)
- ✓ Generalizable framework (replicable for other diseases)

---

**Document Version**: 1.0  
**Last Updated**: March 2026  
**Status**: Complete - Ready for Implementation
