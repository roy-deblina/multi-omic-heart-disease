# Multi-Omic Stratification for Heart Disease: Datasets Guide

## Overview
This document describes verified, publicly available datasets suitable for multi-omic analysis of heart disease. All datasets listed have been validated in peer-reviewed literature and are appropriate for the stratification project.

---

## 1. PRIMARY DATASETS FOR MULTI-OMICS

### 1.1 TCGA (The Cancer Genome Atlas)
**Institution**: National Cancer Institute (NCI)  
**Access**: GDC Data Portal (https://portal.gdc.cancer.gov/)  
**Sample Size**: ~11,000 samples across 33 cancer types  
**Relevant for Heart Disease**: Uses cardiac tissue samples and cancer-induced cardiomyopathy models

#### Omics Data Available
| Omic Type | Coverage | Resolution | Notes |
|-----------|----------|-----------|-------|
| Genomics | Whole Exome (WXS), Whole Genome (WGS) | SNVs, Indels, CNVs | ~20,000 genes, variant call format |
| Transcriptomics | RNA-seq (Illumina) | HTSeq counts, FPKM | 20K genes, ~500M reads per sample |
| Proteomics | RPPA (Reverse Phase Protein Array) | Quantitative | 200+ antibodies, phosphorylation levels |
| Metabolomics | Limited (via metabolite assays) | Discovery mode | In specific studies |

#### How to Use
```
1. Register at GDC Portal
2. Query lung adenocarcinoma of cardiac origin or heart-related samples
3. Download using GDC Data Transfer Tool or API
4. Format: BAM (genomics), FASTQ (RNA-seq), matrix format (proteomics)
```

#### Advantages
- Multi-platform omics on same individuals
- Large sample size
- Harmonized data preprocessing pipeline
- Open access, no restrictions

#### Limitations
- Primarily cancer tissues (requires careful selection of non-malignant cardiac samples)
- Limited longitudinal follow-up
- Mostly US population (ancestry diversity limited)

---

### 1.2 GTEx (Genotype-Tissue Expression)
**Institution**: National Institutes of Health (NIH)  
**Access**: https://gtexportal.org/  
**Sample Size**: ~900 individuals, 54 tissue types  
**Relevant for Heart Disease**: Includes heart tissue (2 regions: left ventricle, atrial appendage)

#### Omics Data Available
| Omic Type | Coverage | Sample Count | Notes |
|-----------|----------|--------------|-------|
| Genomics | WGS, WXS | 900 individuals | High-quality variant calls |
| Transcriptomics | RNA-seq | Heart: ~300-400 samples | Tissue-specific expression |
| eQTL Mapping | Variant-Expression associations | Pre-computed | SNPs affecting expression |
| Methylation | DNA methylation (WGBS) | Limited heart samples | >25M CpG sites |

#### How to Use
```
1. Visit gtexportal.org
2. Search heart tissue (left ventricle, atrial appendage)
3. Download RNA-seq counts matrix (normalized TPM values)
4. Access eQTL data to map genetic variants to expression
5. Format: TSV (expression), VCF (variants)
```

#### Advantages
- Tissue-specific data ideal for cardiac biology
- eQTL mapping connects genetics to expression (critical for multi-omics)
- Well-characterized phenotypes
- Multiple tissues enable cross-tissue analysis
- Free and open access

#### Limitations
- Limited clinical phenotype (barely any disease samples)
- Smaller sample size than TCGA
- Limited proteomics or metabolomics
- Post-mortem tissue (not acute disease state)

---

### 1.3 UK Biobank
**Institution**: UK Biobank Coordinating Centre  
**Access**: https://www.ukbiobank.ac.uk/  
**Sample Size**: ~500,000 individuals (40-70 years old)  
**Relevant for Heart Disease**: Large genomic dataset, many cardiovascular phenotypes

#### Omics Data Available
| Omic Type | Coverage | Sample Count | Notes |
|-----------|----------|--------------|-------|
| Genomics | SNP microarray, WXS, WGS | 500K (SNP) + 200K (WES) | ~800K SNPs in microarray |
| Transcriptomics | RNA-seq | ~50K samples | Whole blood and specific cell types |
| Proteomics | SomaLogic aptamer assay | ~54K samples | 5K proteins measured |
| Metabolomics | NMR metabolomics | ~120K samples | 249 metabolites |
| Imaging | Cardiac MRI | ~40K samples | Ventricular size, function, tissue characteristics |

#### How to Use
```
1. Apply for access (formal application process, ~8-12 weeks)
2. Register as researcher/institution
3. Request data through online portal (project approvals required)
4. Download via secure FTP
5. UK Biobank provides harmonized, quality-controlled data
```

#### Advantages
- Largest multi-omic dataset for human health
- Cardiovascular imaging data (cardiac MRI) essential for phenotyping
- Proteomic and metabolomic data rare and valuable
- Diverse ancestry (mostly UK residents)
- Longitudinal follow-up: re-assessment visits and electronic health records
- Free for research

#### Limitations
- Application and approval process required (time investment)
- Data access restricted to registered researchers
- Primarily healthy cohort (less disease representation than clinical datasets)
- Need to handle massive data volume locally (requires computational resources)

---

## 2. SPECIALIZED HEART DISEASE DATASETS

### 2.1 Framingham Heart Study
**Institution**: Boston University School of Medicine & NHLBI  
**Access**: dbGaP (https://www.ncbi.nlm.nih.gov/gap/)  
**Sample Size**: ~5,000 original cohort + 5,000 offspring cohort, now ~9,000 participants  
**Study Duration**: 70+ years longitudinal

#### Omics Data Available
| Omic Type | Sample Count | Details |
|-----------|--------------|---------|
| Genomics | ~9,000 | SNP genotyping (Affymetrix), WXS available |
| Transcriptomics | ~2,000 | RNA-seq from blood cells (limited) |
| Metabolomics | ~2,000+ | NMR metabolomics, targeted lipidomics |
| Clinical Data | ~9,000 | Comprehensive HF phenotypes, survival data |

#### Key Features
- Gold standard for cardiovascular epidemiology
- Detailed clinical phenotyping:
  - Echocardiography measurements (EF, diastolic function)
  - ECG findings
  - Cardiac risk factors
  - Heart failure classification
- 70+ years of outcomes data (ideal for risk prediction)

#### How to Use
```
1. Register with dbGaP
2. Prepare data use agreement
3. Access via Framingham Heart Study page on dbGaP
4. Data available in SAS, STATA, CSV formats
```

#### Advantages
- Best longitudinal cardiovascular phenotypes
- Decades of validated outcomes
- Rich environmental and clinical covariates
- Family structure enables heritability analysis
- Extensively validated in literature

#### Limitations
- Limited to predominantly European ancestry (WASP bias)
- Omics data less comprehensive than newer datasets
- Access through dbGaP (slower process)
- Some phenotypes are legacy/outdated assessments

---

### 2.2 TCGA HeartDisease Cohort (From OncoGenomics)
**Institution**: GDC Portal curated  
**Relevant Samples**: Cardiac tissue samples from cancer survivors with cardiotoxicity  
**Sample Size**: ~500 samples with cardiac complications

#### What It Provides
- Actual disease tissue (failing hearts) vs. healthy controls
- Multi-omic data on same tissue
- Known progression (cancer → cardiotoxicity → heart failure)

#### Advantages
- Real diseased tissue samples
- Multi-omics on same individual
- Known disease mechanism (can validate approach on known biology)

---

### 2.3 NHGRI-EBI GWAS Catalog (for Polygenic Risk Scores)
**URL**: https://www.ebi.ac.uk/gwas/  
**Content**: Summary statistics from 5,000+ GWAS studies

#### Key Published GWAS for Heart Disease
1. **Coronary Artery Disease (CAD)**
   - Aragam et al. 2022: 64 new loci identified
   - 185,000 individuals, European-ancestry biased
   - Summary statistics: https://www.levin.org/

2. **Heart Failure (HF)**
   - Arora et al. 2021: 41 loci associated with HF
   - 47K HF cases, 880K controls

3. **Atrial Fibrillation (AF)**
   - Nielsen et al. 2018: 97 loci
   - 288K cases, comprehensive risk score available

#### How to Use
```
1. Download summary statistics from GWAS Catalog
2. Use PRSice-2 (Choi et al., 2018) to calculate polygenic risk scores
3. Validate in your cohort
```

#### Advantages
- Publicly available summary statistics (easy access)
- Well-established methodology
- Validated across multiple populations
- Free and open

---

## 3. PUBLIC DATABASES FOR PATHWAY & DRUG TARGET INFORMATION

### 3.1 Reactome (Pathway Database)
**URL**: https://reactome.org/  
**Content**: Curated pathway information, 2,700+ human pathways

#### Relevant Cardiac Pathways
- Cardiac conduction
- Cardiomyocyte hypertrophy
- Inflammatory signaling in heart failure
- Mitochondrial function and energy metabolism

#### Use in Project
```
Query: "Heart failure" OR "Cardiomyopathy"
Extract: Genes in significant pathways
Validate: Overlap with DEGs and biomarkers
```

---

### 3.2 DrugBank
**URL**: https://go.drugbank.com/  
**Content**: FDA-approved drugs paired with targets

#### Use in Project
```
For each identified disease subtype:
1. Extract dysregulated genes/proteins
2. Match to known drug targets in DrugBank
3. Suggest evidence-based therapeutics per subtype
```

---

### 3.3 Protein-Protein Interaction Databases
- **STRING**: https://string-db.org/ (protein interactions and functional partnerships)
- **BioGRID**: https://thebiogrid.org/ (curated physical/genetic interactions)

#### Use in Project
```
Build network from significant proteins
Identify hub genes (high degree, high betweenness centrality)
Candidate drug targets = hub proteins in dysregulated subnetworks
```

---

## 4. RECOMMENDED DATA INTEGRATION WORKFLOW

```
┌─────────────────────────────────────────────────────────┐
│ START: Select Disease Cohort                            │
└──────────────────┬──────────────────────────────────────┘
                   │
       ┌───────────┼───────────┐
       ↓           ↓           ↓
   ┌────────┐  ┌────────┐  ┌────────┐
   │GENOMICS│  │TRANSCR.│  │PROTEOM.│
   └───┬────┘  └───┬────┘  └────┬───┘
       │           │           │
       └───────────┼───────────┘
                   ↓
        ┌──────────────────────┐
        │ Quality Control &    │
        │ Harmonization        │
        │ - Remove outliers    │
        │ - Batch correction   │
        └──────┬───────────────┘
               │
       ┌───────┴──────────┐
       ↓                  ↓
   ┌─────────┐       ┌─────────┐
   │PCA/UMAP │       │DEG/DPG  │
   │Clustering│      │Analysis │
   └────┬────┘       └────┬────┘
        │                 │
        └────────┬────────┘
                 ↓
      ┌──────────────────────┐
      │ Multi-Omic ML Model  │
      │ - Feature Selection  │
      │ - Classification     │
      │ - SHAP Explanation   │
      └──────────┬───────────┘
                 │
        ┌────────┴────────┐
        ↓                 ↓
    ┌───────────┐     ┌─────────--┐
    │Subtypes & │     │Treatment  │
    │Biomarkers │     │Predictions│
    └───────────┘     └──────────-┘
```

---

## 5. PRACTICAL RECOMMENDATIONS FOR PROJECT START

### Phase 1: Proof of Concept (Suggested Datasets)
**Primary**: GTEx heart tissue (smaller, manageable)  
**Secondary**: GWAS summary statistics (quick polygenic risk score)  
**Tertiary**: TCGA (validate on diseased tissues)

**Rationale**: 
- Start small with GTEx (~300-400 heart samples)
- Build multi-omic ML pipeline
- Expand to larger cohorts once validated

### Phase 2: Production (Recommended Datasets)
**Primary**: UK Biobank (comprehensive data, largest N)  
**Secondary**: Framingham Heart Study (best phenotypes, outcomes)  
**Tertiary**: Specialized disease cohorts (cardiotoxicity, inherited cardiomyopathy)

---

## 6. DATA ACCESS CHECKLISTS

### GTEx (Fastest Access)
- [ ] Visit gtexportal.org
- [ ] Search "heart tissue"
- [ ] Download RNA-seq + genotype data
- [ ] Timeline: Same day

### UK Biobank (Formal Process)
- [ ] Register as researcher
- [ ] Prepare project proposal
- [ ] Institutional review board (IRB) approval
- [ ] Submit formal data access request
- [ ] Timeline: 8-12 weeks

### Framingham Heart Study (Via dbGaP)
- [ ] Register with dbGaP
- [ ] Complete data use agreement
- [ ] Submit request
- [ ] Timeline: 2-4 weeks

### GWAS Summary Stats (Immediate)
- [ ] Visit GWAS Catalog
- [ ] Search disease of interest
- [ ] Download summary statistics
- [ ] Timeline: Same day

---

## 7. DATA CHARACTERISTICS TABLE

| Dataset | Sample Size | Omics Types | Disease Content | Access Speed | Cost |
|---------|-------------|------------|-----------------|--------------|------|
| GTEx | ~900 | Genomics, Transcriptomics | None (controls) | Same day | Free |
| UK Biobank | 500K | Genomics, Transcriptomics, Proteomics, Metabolomics | Many phenotypes | 8-12 weeks | Free |
| Framingham | ~9,000 | Genomics, Metabolomics | Rich HF phenotypes | 2-4 weeks | Free |
| TCGA | 11,000 | Genomics, Transcriptomics, Proteomics | Cancer tissues (cardiac edge cases) | Same day | Free |
| GWAS Catalog | Summary stats | Genomics (summary) | Multiple diseases | Same day | Free |

---

## 8. QUALITY ASSURANCE NOTES

### Data Standardization
- All genomic data should be aligned to GRCh38/hg38 reference
- RNA-seq counts normalized using same pipeline (HTSeq or STAR)
- Batch effects must be assessed and corrected before analysis

### Missing Data Handling
- Document % missing per variable
- Use imputation (mice R package) for <20% missingness
- Remove features/samples if >30% missing

### Ancestry/Diversity
- **Important**: Current datasets are predominantly European ancestry
- Plan for bias assessment and sensitivity analyses
- Consider including non-European cohorts (e.g., All of Us Research Program, future releases)

---

**Document Version**: 1.0  
**Last Updated**: March 2026  

