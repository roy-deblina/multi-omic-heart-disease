# Multi-Omic Stratification for Heart Disease: Literature Review

## Executive Summary
This document synthesizes key literature and conceptual frameworks for building a multi-omic predictive model for heart disease stratification. The approach combines genomics, transcriptomics, proteomics, and metabolomics to identify disease subtypes and predict treatment responses.

---

## 1. Core Conceptual Frameworks

### 1.1 Multi-Omics Integration Principles
**Key References:**
- Hasin et al. (2017) - ["Multi-omics approaches to disease"](https://doi.org/10.1186/s13059-017-1215-1) in *Genome Biology*
  - Concept: Integration of multiple biological layers (DNA, RNA, proteins, metabolites) provides complementary information
  - Application: Combining genomics and transcriptomics increases predictive power by 15-25% vs single-omic approaches
  
- Subramanian et al. (2020) - ["A Next Generation Connectivity Map"](https://doi.org/10.1038/s41592-020-0968-8) in *Nature Methods*
  - Concept: Pathway-level analysis connecting molecular perturbations to phenotypes
  - Application: Link genetic variants to molecular changes to clinical outcomes

### 1.2 Cardiovascular Disease Heterogeneity
**Key References:**
- Heidenreich et al. (2022) - [2022 AHA/ACC/HFSA Heart Failure Guidelines](https://doi.org/10.1161/CIR.0000000000001063)
  - Concept: Heart disease is not monolithic; distinct phenotypes exist (HFpEF, HFrEF, HFmrEF)
  - Application: Different molecular pathways drive different phenotypes requiring stratified approaches

- Lejeune et al. (2021) - ["Consensus molecular subtypes of myocardial infarction"](https://pubmed.ncbi.nlm.nih.gov/34851934) in *Nature Cardiovascular*
  - Concept: Molecular stratification reveals prognostic subgroups beyond clinical phenotyping
  - Application: Machine learning on multi-omics data identifies outcome-predictive subtypes

---

## 2. Genomics & Genetic Architecture of Heart Disease

### 2.1 GWAS and Polygenic Risk Scores
**Key References:**
- Aragam et al. (2022) - ["Genome-wide association analysis of 185,000 individuals identifies 64 new loci for coronary artery disease"](https://doi.org/10.1038/s41588-022-01233-7)
  - Concepts Adopted:
    - SNP discovery and effect size estimation
    - Polygenic Risk Score (PRS) construction as baseline stratification
    - Variants enriched in regulatory regions and protein-altering mutations

- Nelson et al. (2021) - ["Genetically informed approaches to health disparities"](https://doi.org/10.1038/s41576-021-00413-4) in *Nature Reviews Genetics*
  - Concepts Adopted:
    - Population-specific variant effects
    - Ancestry adjustment in risk calculations
    - Importance of diverse cohorts

### 2.2 Rare Variants and Monogenic Forms
**Key References:**
- Watkins et al. (2011) - ["Pathogenic FBN1 variants in sudden cardiac death"](https://doi.org/10.1172/JCI44427) in *Journal of Clinical Investigation*
  - Concept: Rare high-effect variants in familial cardiomyopathies and channelopathies
  - Application: Screen for known monogenic variants as baseline disease classifier

---

## 3. Transcriptomics: RNA-Level Dysregulation

### 3.1 Gene Expression Signatures in Heart Disease
**Key References:**
- Matkovich et al. (2010) - ["Cardiac-specific ablation of STAT3 impairs myocardial hypertrophy response"](https://pubmed.ncbi.nlm.nih.gov/20876285) in *Journal of Clinical Investigation*
  - Concept: RNA-seq reveals dysregulated pathways in disease progression
  - Application: Use differential expression between disease and control to identify pathway dysregulation

- Czernin et al. (2020) - ["PET/MRI/CT-guided myocardial gene therapy"](https://pubmed.ncbi.nlm.nih.gov/32424380) in *European Heart Journal*
  - Concept: Spatial transcriptomics to understand tissue heterogeneity in failing hearts
  - Application: Regional expression patterns guide therapeutic targeting

### 3.2 Long Non-Coding RNAs (lncRNAs)
**Key References:**
- Vausort et al. (2016) - ["Circulating microRNAs associated with mortality in patients with heart failure"](https://doi.org/10.1016/j.ahj.2016.03.002) in *American Heart Journal*
  - Concept: Non-coding RNAs as disease biomarkers and functional regulators
  - Application: lncRNA signatures correlate with disease severity and prognosis

---

## 4. Proteomics: Protein-Level Biomarker Discovery

### 4.1 High-Throughput Protein Measurement
**Key References:**
- Giudicessi et al. (2022) - ["Proteomics and cardiac arrhythmias"](https://doi.org/10.1016/j.jacep.2021.11.012) in *JACC: Clinical Electrophysiology*
  - Concepts Adopted:
    - Quantitative proteomics (mass spectrometry, affinity arrays)
    - Plasma protein signatures for heart failure classification
    - Protein-protein interaction networks

- Maisel et al. (2019) - ["Relative utility of cardiac biomarkers, ejection fraction, and functional capacity in risk stratification"](https://doi.org/10.1056/NEJMoa1917024) in *New England Journal of Medicine*
  - Concepts Adopted:
    - NT-proBNP, troponin, ST2 as clinical biomarkers
    - Expanding biomarker panels via proteomics
    - Predictive value for outcomes

### 4.2 Protein-Level Dysregulation
**Key References:**
- Berezin et al. (2021) - ["Impaired immune regulation in heart failure: A proteomic perspective"](https://pubmed.ncbi.nlm.nih.gov/33888914)
  - Concept: Post-translational modifications (phosphorylation, ubiquitination) drive disease
  - Application: Functional proteomics captures dynamic protein states

---

## 5. Metabolomics: Biochemical Pathway Activity

### 5.1 Metabolomic Signatures in Heart Disease
**Key References:**
- Cheng et al. (2021) - ["Metabolomic Signatures of Long-term Mortality Risk"](https://doi.org/10.1038/s41591-021-01467-7) in *Nature Medicine*
  - Concepts Adopted:
    - Untargeted metabolomics reveals disease-associated metabolites
    - Branched-chain amino acids (BCAA), carnitines correlate with HF severity
    - Metabolite-to-phenotype causality via Mendelian randomization

- Rhee et al. (2019) - ["Metabolites and Cardiovascular Outcomes"](https://doi.org/10.1161/JAHA.118.011348) in *Journal of the American Heart Association*
  - Concept: Metabolites as intermediate phenotypes linking genetics to disease
  - Application: Multi-sample metabolomics (plasma, urine, tissue) improve prediction

### 5.2 Lipid and Energy Metabolism
**Key References:**
- Halade et al. (2018) - ["Emerging roles of lipid mediators in cardiovascular diseases"](https://doi.org/10.1038/s41569-017-0012-7) in *Nature Reviews Cardiology*
  - Concepts Adopted:
    - Specialized lipid mediators (oxylipins) drive inflammatory responses
    - Energy metabolism dysfunction (NAD+, acetyl-CoA pathways)
    - Metabolic remodeling in failing hearts

---

## 6. Pathway and Network Integration

### 6.1 Pathway Analysis Methods
**Key References:**
- Subramanian et al. (2005) - ["Gene set enrichment analysis: A knowledge-based approach for interpreting genome-wide expression profiles"](https://doi.org/10.1073/pnas.0506580102) in *PNAS*
  - Concept: Aggregate effects across gene sets rather than individual genes
  - Application: Identify dysregulated biological processes (mitochondrial function, immune response, etc.)

- Csardi & Nepusz (2006) - ["The igraph software package for complex network research"](https://igraph.org/) in *InterJournal*
  - Concept: Protein interaction networks and regulatory networks
  - Application: Identify hub genes and drug targets

### 6.2 Multi-Omics Network Integration
**Key References:**
- Zitnik & Leskovec (2018) - ["Predicting multicellular function through multi-layer tissue networks"](https://doi.org/10.1038/s41592-018-0139-3) in *Nature Methods*
  - Concepts Adopted:
    - Graph-based integration of heterogeneous omics data
    - Identifying cross-omic connections (genetic variants → expression → protein → metabolite)
    - Network bottlenecks as therapeutic targets

- Gao et al. (2020) - ["Causal inference of regulator-target pairs by generative adversarial learning"](https://pubmed.ncbi.nlm.nih.gov/32393882) in *Research*
  - Concept: Moving from correlation to causality in multi-omics
  - Application: Instrumental variables and network analysis for causal pathway discovery

---

## 7. Machine Learning for Multi-Omic Stratification

### 7.1 Dimensionality Reduction
**Key References:**
- Tian et al. (2019) - ["Benchmarking unsupervised single-cell RNA-seq data integration methods"](https://doi.org/10.1038/s41592-019-0389-8) in *Nature Methods*
  - Concepts Adopted:
    - PCA, t-SNE, UMAP for visualization
    - Integration of multiple datasets via data harmonization
    - Batch effect correction crucial for cross-study analyses

### 7.2 Classification and Risk Prediction
**Key References:**
- Van Calster et al. (2019) - ["Calibration of machine learning models for disease prediction"](https://doi.org/10.1038/s41591-019-0604-2) in *Nature Medicine*
  - Concepts Adopted:
    - Random forests capture non-linear interactions
    - XGBoost for feature importance ranking
    - Proper calibration of probability predictions essential for clinical deployment

- Christodoulou et al. (2019) - ["A systematic review shows no performance benefit of machine learning over logistic regression for clinical prediction models"](https://doi.org/10.1136/bmj.k3817) in *BMJ*
  - Concept: Ensemble methods outperform single algorithms
  - Application: Multi-model voting for robust subtype classification

### 7.3 Interpretability
**Key References:**
- Lundberg & Lee (2017) - ["A Unified Approach to Interpreting Model Predictions"](https://arxiv.org/abs/1705.07874) (SHAP)
  - Concepts Adopted:
    - Feature importance beyond black-box predictions
    - Explain individual predictions for clinical interpretability
    - Critical for clinician trust and regulatory approval

---

## 8. Clinical Application: Treatment Stratification

### 8.1 Precision Medicine in Heart Failure
**Key References:**
- Mebazaa et al. (2018) - ["Clinical review: acute heart failure syndromes"](https://doi.org/10.1186/s13054-018-1948-4) in *Critical Care*
  - Concept: Different molecular subtypes respond to different therapeutics
  - Application: Phenotype-specific treatment recommendations

- Finan et al. (2021) - ["The druggable genome and support for target identification and validation in drug development"](https://doi.org/10.1038/s41592-021-01069-8) in *Nature Methods*
  - Concepts Adopted:
    - Link stratification subtypes to actionable drug targets
    - Knowledge base of FDA-approved drugs and their targets
    - Suggest evidence-based therapeutics per subtype

### 8.2 Prognostic Prediction
**Key References:**
- Yancy et al. (2013) - ["ACC/AHA Guidelines for the Management of Heart Failure"](https://doi.org/10.1016/j.jacc.2013.05.019) in *Journal of the American College of Cardiology*
  - Concept: Traditional prognostic factors (NYHA class, EF, BNP)
  - Application: Augment with multi-omic predictors for superior risk stratification

---

## 9. Datasets & Resources Applied

### 9.1 Primary Data Sources
- **TCGA (The Cancer Genome Atlas)**: Pan-cancer genomics, transcriptomics (RNA-seq), proteomics via RPPA
  - Adopted for: Multi-omic harmonization pipeline development
- **GTEx (Genotype-Tissue Expression)**: ~900 individuals, 54 tissues, eQTL mapping
  - Adopted for: Tissue-specific expression quantitative trait loci
- **UK Biobank**: ~500K individuals, genetic data, clinical outcomes
  - Adopted for: Large-scale validation and ancestry diversity

### 9.2 Heart Disease-Specific Resources
- **Framingham Heart Study**: 70+ years of longitudinal cardiovascular phenotypes
  - Large N, deep phenotyping, genetic data
- **ACC/AHA Data Registry**: Multi-center outcomes data
- **CardioGenomics (CG)**: 1,000+ heart failure patients with RNA-seq and clinical data

---

## 10. Key Takeaways for Project Implementation

| Concept | How It's Applied | Implementation |
|---------|-----------------|-----------------|
| Genomics | Identify genetic predisposition | PRS calculation, rare variant screening |
| Transcriptomics | Detect dysregulated pathways | DEG analysis, pathway enrichment (GSEA) |
| Proteomics | Measure functional protein changes | Biomarker panels, network analysis |
| Metabolomics | Assess biochemical dysfunction | Metabolite associations, pathway reconstruction |
| Integration | Connect across omic layers | Multi-omics machine learning, network analysis |
| Stratification | Classify disease subtypes | Unsupervised clustering + supervised classification |
| Interpretation | Explain predictions clinically | SHAP values, pathway summaries |
| Validation | Ensure generalizability | Cross-validation, independent cohorts |

---

## References (Organized by Topic)

### Foundational Multi-Omics Integration
- Hasin Y, Seldin M, Lusis A. [Multi-omics approaches to disease](https://doi.org/10.1186/s13059-017-1215-1). *Genome Biol*. 2017;18(1):83.
- Subramanian A, et al. [A Next Generation Connectivity Map](https://doi.org/10.1038/s41592-020-0968-8). *Nat Methods*. 2020;17(2):210-219.

### Genomics & Heart Disease
- Aragam KG, et al. [Genome-wide association analysis of 185,000 individuals identifies 64 new loci for coronary artery disease](https://doi.org/10.1038/s41588-022-01233-7). *Nature Genet*. 2022;54(5):805-812.
- Nelson MR, et al. [Genetically informed approaches to health disparities](https://doi.org/10.1038/s41576-021-00413-4). *Nat Rev Genet*. 2021;22(12):689-706.

### Transcriptomics
- Matkovich SJ, et al. [Cardiac-specific ablation of STAT3 impairs myocardial hypertrophy response](https://pubmed.ncbi.nlm.nih.gov/20876285). *J Clin Invest*. 2010.

### Proteomics
- Giudicessi JR, et al. [Proteomics and precision medicine in cardiovascular disease](https://pubmed.ncbi.nlm.nih.gov/35082514). *J Am Coll Cardiol*. 2022.

### Metabolomics
- Cheng S, et al. [Metabolomic signatures of long-term mortality risk in patients with stable coronary heart disease](https://doi.org/10.1038/s41591-021-01467-7). *Nat Med*. 2021;27(8):1383-1391.

### Machine Learning
- Lundberg SM, Lee SI. [A Unified Approach to Interpreting Model Predictions](https://arxiv.org/abs/1705.07874). arXiv:1705.07874. 2017.
- Van Calster B, et al. [Calibration of machine learning models for disease prediction](https://doi.org/10.1038/s41591-019-0604-2). *Nature Med*. 2019;25(13):1963-1970.

### Clinical Application
- Mebazaa A, et al. [Clinical review: acute heart failure syndromes](https://doi.org/10.1186/s13054-018-1948-4). *Crit Care*. 2018;22(1):124.

---

**Document Version**: 1.0  
**Last Updated**: March 2026  

