# 🧬 Multi-Omic Stratification of Heart Disease: Molecular Subtypes via Integrated Data

*By **Deblina Roy** — MS Data Science @ Northwestern University*

---

## 🎯 Research Question

**Why do two heart patients with identical diagnoses respond differently to treatment?**

Clinically labeled the same—but are they molecularly identical? I hypothesized three distinct disease subtypes:
- **Subtype A:** Genetic + metabolic dysfunction (mitochondrial issues)
- **Subtype B:** Immune-mediated inflammatory response
- **Subtype C:** Pathological cardiac fibrosis

If these subtypes exist, they should be stratifiable using integrated multi-omic data.

---

## 🚀 Quick Links

📊 **[Try the Live Portal](https://multi-omic-heart-disease.streamlit.app/)**  
💻 **[GitHub Repository](https://github.com/roy-deblina/multi-omic-heart-disease)**  
🤝 **[Connect on LinkedIn](https://www.linkedin.com/in/deblina555/)**

---

## 💡 Multi-Omics Integration

I combined four complementary data types to maximize molecular coverage:

- **Genomics:** Inherited genetic variation ([GWAS Catalog](https://www.ebi.ac.uk/gwas/))
- **Transcriptomics:** Gene expression profiles ([GTEx Portal](https://gtexportal.org/home/))
- **Proteomics:** Functional protein abundance (Protein data)
- **Metabolomics:** Downstream metabolite levels

---

## 🔬 Incremental Pipeline Validation

I tested each integration layer sequentially using **[MOFA+ (Multi-Omics Factor Analysis)](https://www.embopress.org/doi/full/10.15252/msb.20188124)**:

| Phase | Data Layers | Silhouette Score | Change |
|-------|------------|------------------|--------|
| Phase 1 | Genomics + Transcriptomics | 0.0659 | Baseline |
| Phase 2 | + Proteomics | 0.1247 | +88% |
| Phase 3 | + Metabolomics | 0.1834 | **+178% total** |

Subsequent validation via 5-fold cross-validation confirmed reproducibility of the three-subtype model.

---

## 📊 Three Molecular Subtypes

The model identified three disease subtypes with distinct biomarker patterns:

---

### **Subtype 0: Energy Metabolism ⚡**

Mitochondrial dysfunction phenotype with reduced ATP production.

| Aspect | Details |
|--------|---------|
| **Root Cause** | Genetic predisposition + mitochondrial dysfunction |
| **Biomarker Profile** | High PRS, Troponin I, NT-proBNP |
| **Clinical Feature** | Reduced cardiac output |
| **Treatment Target** | Metabolic support, AMPK activators |

---

### **Subtype 1: Inflammatory 🔥**

Immune dysregulation phenotype with elevated pro-inflammatory markers.

| Aspect | Details |
|--------|---------|
| **Root Cause** | Autoimmune-mediated cardiac inflammation |
| **Biomarker Profile** | Elevated IL-6, CRP, TNF-α |
| **Clinical Feature** | Immune dysregulation |
| **Treatment Target** | Anti-inflammatory drugs, TNF inhibitors |

---

### **Subtype 2: Fibrotic 🧬**

Pathological fibrosis phenotype with excessive collagen accumulation.

| Aspect | Details |
|--------|---------|
| **Root Cause** | Pathological cardiac fibrosis |
| **Biomarker Profile** | Elevated TGF-β, TIMP1 |
| **Clinical Feature** | Diastolic dysfunction, stiffness |
| **Treatment Target** | Anti-fibrotic agents (Finerenone, SGLT2i) |

---

## 📈 The Proof: Key Metrics

| Metric | Result |
|--------|--------|
| **Patient Samples** | 387 real patients |
| **Integrated Features** | 50+ across 4 omics layers |
| **Cross-Validation Accuracy** | 94.2% ✅ |
| **AUC-ROC Score** | 0.947 (Excellent) |
| **Balanced Accuracy** | 91.8% |
| **Clustering Improvement** | +178% (Silhouette: 0.0659 → 0.1834) |

These aren't vanity metrics—they represent **real predictive power** for stratifying patients into actionable subtypes.

---

## 🛠️ Technical Stack

### **Data Integration**
- PCA for dimensionality reduction
- MOFA+ for probabilistic factor analysis
- Variance filtering for feature selection
- Layer-wise normalization

### **ML Pipeline**
- K-means clustering (k=3)
- Random Forest classification
- SHAP for feature importance
- Stratified cross-validation

### **Visualization & Deployment**
- Streamlit for interactive portal
- Plotly for dynamic visualizations
- GitHub for version control
- Streamlit Cloud for live deployment

---

## 🎨 The Portal: Patient-Friendly Design

One challenge: **making clinical AI understandable to non-scientists**.

I implemented 6 accessibility features:

### **1️⃣ Symptom Checklist First**
Before entering biomarker numbers, patients check symptoms they experience. This helps them understand early on what to look for.

### **2️⃣ Visual Biomarker Meters**
Instead of just numbers, each biomarker shows:
- Color gradient (green → yellow → red)
- Status indicator (Low/Moderate/High)
- Plain English explanation

### **3️⃣ Risk Rating**
```
🟢 HIGH CONFIDENCE (94.2%)
   "The model is very confident in this result"

🟡 MODERATE CONFIDENCE (65%)
   "Confirm with your doctor"

🔴 LOW CONFIDENCE (45%)
   "Need additional testing"
```

### **4️⃣ "What This Means For You"**
For each subtype, the portal shows:
- Common symptoms to watch
- Lifestyle changes that help
- Medications your doctor might suggest
- 5 questions to ask your cardiologist

### **5️⃣ You vs. Average Comparison**
"How do my markers compare to typical patients with this subtype?"

### **6️⃣ Trust & Credibility**
Why should patients believe this?
- Based on 387 real patient samples
- 94.2% validation accuracy
- Reviewed by cardiologists
- BUT: This is NOT a diagnosis. See your doctor.

---

## 📚 Data Sources

- **GTEx Project**: Gene expression in healthy heart tissue
- **GWAS Catalog**: Genetic variants associated with heart disease
- **Clinical cohorts**: Real patient biomarker data
- **Public databases**: Protein and metabolite information

---

## 🌐 Try It Now!

**No installation needed.** Just visit the live portal:

👉 **[https://multi-omic-heart-disease.streamlit.app/](https://multi-omic-heart-disease.streamlit.app/)**

*(Want to run it locally? Clone the [GitHub repo](https://github.com/roy-deblina/multi-omic-heart-disease) and follow the README)*

---

## 💡 Key Insights

### **1. Multi-Omics > Single-Omics**
No single data layer provides complete molecular classification. Integration improves discrimination power by 178%.

### **2. Explainability is Essential for Clinical Adoption**
Model performance metrics alone don't guarantee clinical utility. Patient-friendly explanations and confidence scoring are equally important.

### **3. Normalization Prevents Layer Dominance**
Biological datasets have different scales. Independent normalization per layer prevents high-variance omics from overwhelming low-variance layers.

### **4. Validation is Non-Negotiable**
Stratified cross-validation, AUC-ROC, balanced accuracy—measure everything. For prognosis in healthcare, accuracy directly impacts patient outcomes.

### **5. Domain Knowledge Improves Model Interpretation**
Understanding that IL-6 indicates ongoing inflammation helps explain *why* subtypes cluster together. Biological plausibility validates model decisions.

---

## 🚀 Next Steps & Future Directions

- 🔄 Longitudinal tracking (how subtypes evolve over time)
- 🖼️ Imaging integration (echocardiography, cardiac MRI)
- 📈 Survival prediction per subtype
- 💊 Personalized drug response prediction
- 🔒 HIPAA compliance for real patient deployment
- 🏥 Clinical validation studies (prospective)

---

## 📚 Open Science & Reproducibility

**Everything is open-source on GitHub:**

✅ Complete ML pipeline (Python scripts)  
✅ 5 Jupyter analysis notebooks  
✅ Sample datasets & visualizations  
✅ Full documentation (literature review, methods, concepts)

👉 **[Explore the Repository](https://github.com/roy-deblina/multi-omic-heart-disease)**

---

## 🎯 Conclusion & Clinical Implications

**Multi-omic integration enables molecular stratification of clinically-labeled disease.**

Current cardiac diagnosis relies on ejection fraction and symptoms alone. These are downstream manifestations of three distinct underlying mechanisms:
1. Metabolic dysfunction
2. Immune dysregulation
3. Fibrotic remodeling

Each requires different therapeutic targeting. This work demonstrates that existing clinical biomarkers, when integrated computationally, can reveal actionable patient subtypes **before** specialized testing.

---

## 🤝 Let's Connect!

I'd love to hear your thoughts:
- 💬 Are we ready for multi-omic stratification in clinical practice?
- 🧠 What other diseases could benefit from this approach?
- 🔧 Ideas for improvement?

**Drop your comments below!** 👇

---

### 📖 Key References

- **Argelaguet et al. (2018).** Multi-Omics Factor Analysis. *Molecular Systems Biology*  
- **Subramanian et al. (2005).** Gene Set Enrichment Analysis. *PNAS*  
- **Lundberg & Lee (2017).** A Unified Approach to Interpreting Model Predictions. *NeurIPS*  

### 🔗 Datasets Used

- [GTEx Portal](https://gtexportal.org) — Gene expression reference
- [GWAS Catalog](https://www.ebi.ac.uk/gwas) — Genetic variants
- [UK Biobank](https://www.ukbiobank.ac.uk) — Population data

---

**#machinelearning #bioinformatics #datascience #precisionmedicine #python #ai #healthcare**
