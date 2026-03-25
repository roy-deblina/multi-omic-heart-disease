import re

with open('interactive_portal.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace just the radio line with selectbox
old_pattern = r'page = st\.sidebar\.radio\(\s*"Navigate",\s*\[.*?\],\s*help="Select a page to explore"\s*\)'

new_code = '''page = st.sidebar.selectbox(
    "Navigate",
    [
        "🏠 Home",
        "📊 Phase 1: MVP Results",
        "🔬 Phase 2: Proteomics", 
        "🧪 Phase 3: Metabolomics",
        "🔮 Patient Predictor",
        "📈 Comparison",
        "ℹ️ Scientific Details"
    ]
)'''

content = re.sub(old_pattern, new_code, content, flags=re.DOTALL)

with open('interactive_portal.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed navigation")
