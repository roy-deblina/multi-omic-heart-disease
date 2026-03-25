# GitHub Quick Reference - Common Commands

## 1️⃣ Initial Setup (Run Once)

```bash
cd /Users/Guddus/Documents/NW-MSDS/Multi-omic-project

# Initialize git
git init

# Configure your identity
git config user.name "Deblina Roy"
git config user.email "111deblina@gmail.com"

# Verify configuration
git config --list
```

---

## 2️⃣ Ready to Commit (Before First Push)

```bash
# Check status
git status

# Add all files (respects .gitignore)
git add .

# Preview what will be committed
git ls-files

# Make first commit
git commit -m "Initial commit: Multi-omic heart disease project"
```

---

## 3️⃣ Connect to GitHub

```bash
# Add remote (replace "YOUR_USERNAME" if different)
git remote add origin https://github.com/deblina555/multi-omic-heart-disease.git

# Verify connection
git remote -v

# Rename main branch (GitHub default)
git branch -M main

# Push to GitHub
git push -u origin main
```

---

## 4️⃣ Making Updates After Initial Push

```bash
# Make your changes, then:
git add .
git commit -m "Your descriptive commit message"
git push origin main
```

---

## 5️⃣ Staged Commits (Recommended Approach)

### Commit 1: Core Documentation
```bash
git add README.md PROJECT_STRUCTURE.md *.LITERATURE_REVIEW.md 02_DATASETS_GUIDE.md 03_METHODOLOGY_OVERVIEW.md ML_CONCEPTS_APPLIED.md
git commit -m "Add comprehensive project documentation"
git push origin main
```

### Commit 2: Main Code
```bash
git add interactive_portal.py MVP_MultiOmic_Pipeline.py generate_phase3.py fix_nav.py requirements_mvp.txt
git commit -m "Add ML pipeline and Streamlit portal"
git push origin main
```

### Commit 3: Supporting Guides
```bash
git add MVP_QUICKSTART.md STREAMLIT_QUICKSTART.md MVP_README.md NEXT_STEPS.md DEVTO_BLOG_DRAFT.md GITHUB_SETUP_GUIDE.md
git commit -m "Add quick-start guides and setup documentation"
git push origin main
```

### Commit 4: Notebooks & Results
```bash
git add notebooks/ src/ mvp_results/*.png mvp_results/*.csv
git commit -m "Add analysis notebooks and visualization results"
git push origin main
```

---

## 6️⃣ Using GitHub Copilot Write for Commit Messages

**In VS Code:**
1. Open Command Palette: `Cmd + Shift + P`
2. Type: `GitHub: Create Commit Message`
3. VS Code shows changed files - review
4. Copilot generates 3-4 commit message options
5. Click the one you prefer
6. Edit if needed, then confirm

**Template for Copilot Prompts:**
```
"I'm committing updates to my multi-omic heart disease project.
Changes:
- [List what you changed]
- [Features added/fixed]
- [Why these changes matter]

Generate a professional commit message that's:
- Specific about what changed
- No longer than 72 characters for title
- Clear about impact
- Suitable for GitHub/LinkedIn showcase"
```

---

## 7️⃣ Useful Git Commands

```bash
# Check commit history
git log --oneline

# See differences before commit
git diff

# Undo last commit (keep files)
git reset --soft HEAD~1

# See all branches
git branch -a

# Create a new branch for experiments
git checkout -b feature/symptom-predictor

# Switch branches
git checkout main

# Delete a branch
git branch -d feature/symptom-predictor
```

---

## 8️⃣ File-by-File Reference

**Always Include:**
```
✅ README.md
✅ interactive_portal.py
✅ MVP_MultiOmic_Pipeline.py
✅ requirements_mvp.txt
✅ All .md documentation
```

**Include if Available:**
```
✅ notebooks/
✅ src/
✅ mvp_results/*.png
✅ mvp_results/patient_subtypes.csv
✅ mvp_results/phase3_feature_importance.csv
```

**Exclude (via .gitignore):**
```
❌ Large CSV files (>50MB)
❌ __pycache__/
❌ .DS_Store
❌ .venv/
❌ *.ipynb_checkpoints
```

---

## 9️⃣ Status Checks

```bash
# Check how many files will be added
git add . && git status

# See size of files
ls -lh | grep -E '\.py|\.md|\.csv'

# Count commits
git log --oneline | wc -l

# Check remote connection
git remote -v
```

---

## 🔟 Final Push Checklist

- [ ] All files added? (`git status`)
- [ ] Commit message is descriptive? 
- [ ] .gitignore created? (excludes large files)
- [ ] Remote configured? (`git remote -v`)
- [ ] Pushed successfully? (`git push origin main`)
- [ ] GitHub page shows files? (Check GitHub.com)

---

## Pro Tips

1. **Small, logical commits** are better than one massive commit
   - Easy to track changes
   - Easy to revert if needed
   - Looks professional

2. **Use descriptive messages**
   - "Add feature X" ✅
   - "fix bug" ❌

3. **Commit related changes together**
   - Don't mix documentation + code + data in one commit
   - Helps others understand project evolution

4. **Check before pushing**
   - `git diff --cached` to see what's being committed
   - `git status` to verify repo state

---

## Username Verification

Your GitHub details for this project:
- **GitHub Username**: deblina555
- **Email**: 111deblina@gmail.com
- **Repository**: https://github.com/deblina555/multi-omic-heart-disease
- **Branch**: main
- **Project**: Multi-Omic Heart Disease Stratification

---
