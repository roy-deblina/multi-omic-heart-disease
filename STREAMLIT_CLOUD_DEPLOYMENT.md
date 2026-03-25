# 🚀 Deploy to Streamlit Cloud - Step-by-Step Guide

**Deployment Date**: March 25, 2026  
**Time Needed**: 15-20 minutes total  
**Final URL**: `https://deblina555-multi-omic-heart-disease-interactive-portal-xxxx.streamlit.app`

---

## ✅ Pre-Deployment Checklist

Before starting, verify:
- [ ] Code compiles (already checked ✅)
- [ ] Portal runs locally without errors
- [ ] GitHub account exists (you have one)
- [ ] Repository ready to push

All good! Let's deploy.

---

## 🎯 3 Steps to Live Deployment

### **STEP 1: Push Code to GitHub (5 minutes)**

```bash
cd /Users/Guddus/Documents/NW-MSDS/Multi-omic-project

# Initialize git (if not already done)
git init

# Configure git
git config user.name "Deblina Roy"
git config user.email "111deblina@gmail.com"

# Add all files
git add .

# Create first commit
git commit -m "Multi-omic heart disease portal with patient-friendly features

- 🔮 Patient Predictor with 6 patient-friendly features
- 📋 Plain English explanations for biomarkers
- 📊 Visual meters instead of raw numbers
- 🎯 Symptom checklist before biomarkers
- ✅ Trust/confidence explanations
- 📧 Shareable doctor summary
- 94.2% validation accuracy on 387 samples"

# Add GitHub as remote
git remote add origin https://github.com/deblina555/multi-omic-heart-disease.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Expected output**: Files uploaded to GitHub (takes ~30 seconds)

---

### **STEP 2: Create Streamlit Cloud Account (2 minutes)**

1. Go to: https://streamlit.io/cloud
2. Click "**Sign in with GitHub**"
3. Authorize Streamlit to access your GitHub
4. You'll see your GitHub repositories listed

Done! You're now connected.

---

### **STEP 3: Deploy Your App (5 minutes)**

**In Streamlit Cloud Dashboard:**

1. Click **"New app"** (top-right button)

2. **Fill in the form:**
   - **Repository**: `deblina555/multi-omic-heart-disease`
   - **Branch**: `main` (already selected)
   - **Main file path**: `interactive_portal.py`

3. Click **"Deploy"**

4. Streamlit will:
   - Clone your GitHub repo
   - Install dependencies from `requirements_mvp.txt`
   - Run your app
   - Generate a live URL

**This takes 2-3 minutes.** You'll see a green "✅ Your app is ready!" message.

---

## 🌐 Your Live URL

Once deployed, your app will be at:

```
https://deblina555-multi-omic-heart-disease-interactive-portal-<random>.streamlit.app
```

**Example:**
```
https://deblina555-multi-omic-heart-disease-interactive-portal-a1b2c3d4.streamlit.app
```

---

## 📋 Complete Terminal Commands (Copy & Paste)

```bash
# Step 1: Navigate to project
cd /Users/Guddus/Documents/NW-MSDS/Multi-omic-project

# Step 2: Initialize and commit
git init
git config user.name "Deblina Roy"
git config user.email "111deblina@gmail.com"
git add .
git commit -m "Multi-omic heart disease portal - patient-friendly version"

# Step 3: Push to GitHub
git remote add origin https://github.com/deblina555/multi-omic-heart-disease.git
git branch -M main
git push -u origin main
```

After this, go to Streamlit Cloud and deploy (browser steps above).

---

## 🔧 If Deployment Fails

### **Error: "requirements.txt not found"**
Solution: Rename your file
```bash
cp requirements_mvp.txt requirements.txt
git add requirements.txt
git commit -m "Add requirements.txt for Streamlit Cloud"
git push origin main
```

### **Error: "Module not found"**
Streamlit Cloud will auto-install from `requirements_mvp.txt` but if it fails:
1. Go to app settings (gear icon)
2. Add missing packages manually
3. Redeploy

### **Error: "Data file not found"**
Solution: Make sure `mvp_results/*.csv` are in repo:
```bash
git ls-files | grep mvp_results
# Should show your CSV files
```

---

## ✨ After Deployment

### **Share Your Live App:**

**LinkedIn Post Template:**
```
🚀 Live: Multi-Omic Heart Disease Portal

Just deployed my 3-phase ML pipeline to Streamlit Cloud!

🧬 94.2% validation accuracy
📈 +178% improvement in patient stratification  
🫀 Patient-friendly predictor with 6 accessibility features
💻 Try it live: [YOUR_STREAMLIT_URL]

Built with:
• Genomics + Transcriptomics + Proteomics + Metabolomics
• 387 patient samples across 3 disease subtypes
• Open-source on GitHub

#MachineLearning #Healthcare #OpenScience

github.com/deblina555/multi-omic-heart-disease
```

### **Update Your GitHub README:**

Add this section to your README.md:

```markdown
## 🚀 Try the Live Portal

**[Click here to use the portal](https://deblina555-multi-omic-heart-disease-interactive-portal-xxxx.streamlit.app)**

The portal is live on Streamlit Cloud. No installation needed - just click and explore!

### Features:
- 📋 Symptom checklist
- 📊 Interactive biomarker predictor
- 🎯 Patient-friendly results with plain English explanations
- ✅ Shareable doctor summary
```

---

## 📊 What Gets Deployed

Your Streamlit Cloud deployment includes:

```
✅ interactive_portal.py (main app)
✅ All .md documentation
✅ All Python scripts
✅ mvp_results/ (sample data & visualizations)
✅ src/ (reusable modules)
✅ notebooks/ (if included)
❌ Large CSV files (excluded by .gitignore)
```

Total size uploaded: ~50MB (Streamlit Cloud can handle 250MB+)

---

## ⚡ Auto-Deploy Updates

Great news: **Every time you push to GitHub, Streamlit Cloud automatically redeploys!**

```bash
# Make changes locally
nano interactive_portal.py

# Update and push
git add .
git commit -m "Update feature..."
git push origin main

# 🤖 Streamlit Cloud automatically rebuilds in ~2 minutes
```

---

## 🎯 Deployment Timeline

| Step | Time | Status |
|------|------|--------|
| Push to GitHub | 5 min | Ready |
| Streamlit Cloud signup | 2 min | Ready |
| Deploy app | 5 min | Ready |
| App goes live | 2-3 min | Automatic |
| **Total** | **15 min** | **✅ Ready!** |

---

## 🔑 Important Notes

### **GitHub Token (Auto-handled)**
- Streamlit Cloud uses OAuth
- No need to create personal tokens
- Just click "Sign in with GitHub"

### **App goes to sleep**
- Free tier: App sleeps after 7 days of inactivity
- Premium tier: Always-on
- Free tier wakes up immediately when someone visits

### **View app logs**
In Streamlit Cloud dashboard:
- Click your app
- Manage app → View logs
- Shows any errors or output

---

## 📞 Troubleshooting

**Q: Push failed "fatal: unable to access"**
```bash
# Make sure remote is correct
git remote -v
# Should show https://github.com/deblina555/...
```

**Q: Streamlit Cloud says "repository not found"**
- Make sure repo is PUBLIC (Settings → Repository visibility)
- Or use personal access token instead of OAuth

**Q: App loads but shows errors**
- Check app logs in Streamlit Cloud dashboard
- Common: Missing package in requirements.txt
- Solution: Update requirements, push again

**Q: Want to change main file?**
- App settings (gear icon) → Change "Main file path"
- Or keep as `interactive_portal.py` (recommended)

---

## 🎉 You're Done!

Once deployed:
1. ✅ Portal is live 24/7
2. ✅ No server costs (free tier)
3. ✅ Auto-updates when you push to GitHub
4. ✅ Professional portfolio piece
5. ✅ Shareable URL for LinkedIn/blog

**Your app is production-ready!** 🚀

---

## 📋 Quick Reference

**Live URL format:**
```
https://deblina555-multi-omic-heart-disease-interactive-portal-[random].streamlit.app
```

**GitHub repo:**
```
https://github.com/deblina555/multi-omic-heart-disease
```

**Share with:**
- LinkedIn (post with portal URL)
- Dev.to blog (with portal + GitHub link)
- Email/resume (impressive portfolio project)

---

**Ready to deploy? Follow Steps 1-3 above, then you're live! 🚀**

Need help with any step? Everything is detailed above.
