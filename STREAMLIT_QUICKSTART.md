# Streamlit Portal Quick Start

## 🚀 Launch the Interactive Dashboard

The interactive Streamlit portal allows you to explore MVP and Phase 2 results without writing code.

### Installation

```bash
# Install Streamlit (if not already installed)
pip install streamlit plotly

# Or update requirements
pip install -r requirements_mvp.txt
```

### Running the Portal

```bash
# From project directory
streamlit run interactive_portal.py
```

**Output:**
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

Open `http://localhost:8501` in your browser.

## 📊 Portal Features

### 1️⃣ **Home Page** 🏠
- Project overview
- Key metrics summary
- How to navigate guide

### 2️⃣ **MVP Results** 📊
Interactive exploration of Phase 1 findings:

**Tabs:**
- **🎯 Clusters**: 2D PCA visualization of patient stratification
  - Hover to see patient IDs
  - Color = subtype assignment
  - Point density = cluster tightness
  
- **📊 Feature Importance**: Top features using SHAP analysis
  - Slider to select top N (5-15)
  - Bar chart magnitude = feature influence
  - Distinguish genomic (PRS) vs transcriptomic (PC1-10) contributions
  
- **📍 Distribution**: Pie chart of subtype sizes
  - Absolute counts + percentages
  - Check class balance
  
- **🔗 Correlations**: Heatmap of feature relationships
  - Red = positive correlation
  - Blue = negative correlation
  - Identify co-varying features
  
- **🎨 Profiles**: Radar plot of subtype feature signatures
  - One line per subtype
  - Larger area = higher feature values
  - Compare molecular signatures

**Data Explorer** (bottom):
- Browse raw feature matrix
- View importance rankings
- Download patient assignments

### 3️⃣ **Phase 2 Preview** 🔬
- Timeline of work
- Expected improvements
- Architecture diagram
- (Active once Phase 2 complete)

### 4️⃣ **Compare** 📈
- Phase 1 vs Phase 2 side-by-side
- Metrics improvement table
- (Active once Phase 2 complete)

### 5️⃣ **About** ℹ️
- Project background
- Technical methods
- Data sources
- References
- Contact info

## 🎨 Customization

### Change Number of Features Displayed

```python
# In interactive_portal.py, find line with:
st.slider("Top N features to show", 5, 15, 10)

# Change to:
st.slider("Top N features to show", 5, 20, 15)  # New range: 5-20, default 15
```

### Add Your Logo

```python
# In interactive_portal.py, add after st.set_page_config():
st.image('path/to/your/logo.png', width=200)
```

### Change Color Scheme

```python
# Replace this:
color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c']

# With your colors:
color_discrete_sequence=['#YOUR_COLOR1', '#YOUR_COLOR2', '#YOUR_COLOR3']
```

## 📤 Deployment Options

### Option 1: Streamlit Cloud (Free, Recommended)

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app"
4. Select repository, branch, path to `interactive_portal.py`
5. App goes live automatically

**Advantages:**
- Free
- Auto-deploys on GitHub pushes
- Shareable public URL
- HTTPS by default

### Option 2: Docker (Self-hosted)

```bash
# Create Dockerfile
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements_mvp.txt
CMD ["streamlit", "run", "interactive_portal.py"]

# Build and run
docker build -t multi-omic-portal .
docker run -p 8501:8501 multi-omic-portal
```

### Option 3: AWS / Azure / Google Cloud

[See Streamlit deployment docs](https://docs.streamlit.io/deploy)

## 🔗 Sharing

### Share the Dashboard

Once deployed:

```
LinkedIn Post:
🧬 Excited to share our interactive Multi-Omic Heart Disease Stratification Dashboard!

Explore patient subtypes, feature importance, and molecular signatures in real-time.

[Dashboard Link] 
[GitHub Link]

#datascience #healthcare #bioinformatics
```

### Share Screenshots

```bash
# Take screenshot of favorite visualization
# Cmd+Shift+3 (Mac) / Print Screen (Windows)

# Or use Streamlit's "Share" button (top right)
```

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'streamlit'"
```bash
pip install streamlit
```

### "No MVP results found"
Make sure you've run:
```bash
python MVP_MultiOmic_Pipeline.py
```
Results should be in `./mvp_results/`

### Portal is slow
- Check your internet (Streamlit Cloud uses internet)
- Reduce number of samples in your data
- Use `@st.cache_data` decorator for heavy operations

### "Plotly not installed"
```bash
pip install plotly
```

## 📊 Performance Tips

### For Large Datasets (>1000 samples)
- Filter data before visualization
- Use Plotly's `scattergl` for faster rendering
- Sample data for exploratory analysis

### For Slow Networks
- Pre-compute visualizations (save as PNG)
- Reduce Plotly `.load_external_scripts`
- Deploy on local server (not cloud)

## 🔐 Privacy & Security

**Important**: Never upload:
- Real patient data
- Sensitive health information
- Unencrypted individual-level data

Current portal uses **synthetic data** – safe to share publicly.

If deploying with real data:
- Use authentication (Streamlit Cloud supports)
- Run on secure server
- Encrypt patient identifiers
- Follow HIPAA/GDPR requirements

## ✨ Advanced Features (Optional)

### Add File Upload
```python
uploaded_file = st.file_uploader("Upload your data")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
```

### Add Sidebar Filters
```python
st.sidebar.header("Filters")
selected_subtype = st.sidebar.selectbox("Filter by Subtype", [0, 1, 2, "All"])
filtered_data = integrated_features[clusters == selected_subtype] if selected_subtype != "All" else integrated_features
```

### Add Download Buttons
```python
csv = integrated_features.to_csv(index=False)
st.download_button(
    label="Download Feature Matrix",
    data=csv,
    file_name="integrated_features.csv",
    mime="text/csv"
)
```

## 🎓 Learning Resources

- [Streamlit Docs](https://docs.streamlit.io)
- [Plotly Python](https://plotly.com/python/)
- [Deployment Guide](https://docs.streamlit.io/deploy)
- [Theme Customization](https://docs.streamlit.io/library/get-started/multipage-apps/create-a-multipage-app)

---

**Status**: Streamlit portal ready for Phase 1 MVP. Will expand with Phase 2 results.

**Next**: Publish Dev.to blog + LinkedIn post linking to dashboard!
