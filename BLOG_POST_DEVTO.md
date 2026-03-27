# 🧬 I Built an AI That Finds the Hidden "Why" Behind Heart Disease

*By **Deblina Roy** — MS Data Science @ Northwestern University*

---

## 🎯 The Question That Started It All

A few months ago, while diving into cardiovascular data, I hit a wall of curiosity: **Why do two heart patients with the exact same diagnosis respond so differently to the same treatment?**

Clinically, they are labeled the same. But biologically? That didn't feel right. 

Coming from a background in **Microbiology**, I've always been fascinated by the invisible "mechanics" of the cell. Transitioning into **Data Science** at Northwestern allowed me to finally quantify those mechanics at scale.

I imagined three patients:
- **Patient A:** Inherited genetic and metabolic fuel issues
- **Patient B:** Hyper-active immune system driving the damage (inflammation)
- **Patient C:** Heart slowly stiffening from excessive scar tissue (fibrosis)

**Same diagnosis. Completely different molecular realities.** Yet we treat them with a "one-size-fits-all" approach. **I built this AI portal to prove we can do better.**

---

## 🚀 Quick Links

📊 **[Try the Live Portal](https://multi-omic-heart-disease.streamlit.app/)**  
💻 **[GitHub Repository](https://github.com/roy-deblina/multi-omic-heart-disease)**  
🤝 **[Connect on LinkedIn](https://www.linkedin.com/in/deblina555/)**

---

## 💡 The Insight: Synergistic Multi-Omics

If the disease is different at a molecular level, then **the data already knows—we just aren't looking at all the layers at once.**

Instead of using one dataset, I integrated four biological "chapters" of the same story:

- **Genomics:** The blueprint you're born with ([GWAS Catalog](https://www.ebi.ac.uk/gwas/))
- **Transcriptomics:** What your genes are actually doing ([GTEx Portal](https://gtexportal.org/home/))
- **Proteomics:** The functional machinery (Protein data)
- **Metabolomics:** The downstream biochemical consequences

---

## 🔬 The "Aha!" Moment

I didn't jump to all four layers at once. I built the pipeline in phases:

- **Phase 1 (Genomics + Transcriptomics):** The separation was blurry (Silhouette: 0.0659)
- **Phase 2 (+ Proteomics):** Patterns started to emerge (+88% improvement)
- **Phase 3 (+ Metabolomics):** **That's when it clicked.** Using **[MOFA+ (Multi-Omics Factor Analysis)](https://www.embopress.org/doi/full/10.15252/msb.20188124)**, the clustering quality **improved by 178%**

This wasn't just noise—these were **real biological signatures**.

---

## 📊 What the AI Found: 3 Distinct Subtypes

The model consistently identified three "neighborhoods" of disease, each with unique biological characteristics:

---

### **Subtype 0: Energy Metabolism ⚡**

**The Problem:** Mitochondrial dysfunction. The heart doesn't have enough cellular "fuel."

| Aspect | Details |
|--------|---------|
| **Root Cause** | Genetic predisposition + mitochondrial dysfunction |
| **Biomarker Profile** | High PRS, Troponin I, NT-proBNP |
| **Clinical Feature** | Reduced cardiac output |
| **Treatment Target** | Metabolic support, AMPK activators |

---

### **Subtype 1: Inflammatory 🔥**

**The Problem:** The immune system is attacking the heart tissue itself.

| Aspect | Details |
|--------|---------|
| **Root Cause** | Autoimmune-mediated cardiac inflammation |
| **Biomarker Profile** | Elevated IL-6, CRP, TNF-α |
| **Clinical Feature** | Immune dysregulation |
| **Treatment Target** | Anti-inflammatory drugs, TNF inhibitors |

---

### **Subtype 2: Fibrotic 🧬**

**The Problem:** Excessive collagen deposition making the heart muscle stiff and inflexible.

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

## 💡 What I Learned

### **1. Multi-Omics Integration > Single Data Source**
Each biological layer tells a different part of the story. Genomics alone isn't enough—you need the full picture.

### **2. Explainability Builds Trust**
A model is only as good as people's trust in it. I spent as much time on **patient-friendly explanations** as on the ML pipeline itself.

### **3. Normalization is Critical**
Each omic layer has different scales and distributions. Normalize independently to prevent one layer from dominating others.

### **4. Validation is Non-Negotiable** 
For healthcare applications: 5-fold cross-validation, AUC-ROC, balanced accuracy—measure everything. Accuracy isn't optional. It's a life-or-death decision.

### **5. Domain Knowledge Beats Pure ML**
Understanding that **IL-6** indicates inflammation helped explain *why* patients clustered together. Biology informs the algorithm.

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

## 🎯 Key Takeaway

**We don't need a new test. We need better *interpretation* of existing data.**

The biomarkers were always there. We just weren't looking at them together. When you integrate genomics, transcriptomics, proteomics, and metabolomics, **the disease subtypes reveal themselves.**

This is the future of **precision medicine**: Not just treating "heart disease," but treating the *specific biological mechanism* driving heart disease in *each patient*.

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
