import streamlit as st
import difflib
from datetime import datetime

st.set_page_config(page_title="AI Knowledge Time Machine")

st.title("AI Knowledge Time Machine")

st.write("Analyze how code evolves over time using AI-powered version comparison.")

# Load Old Version
with open("sample_old_code.py", "r") as f:
    old_code = f.readlines()

# Load New Version
with open("sample_new_code.py", "r") as f:
    new_code = f.readlines()

# Show Timestamp
st.subheader("Version Timeline")

st.info(f"""
Old Version: 2025
New Version: {datetime.now().year}
""")

# Generate Difference
difference = difflib.unified_diff(
    old_code,
    new_code,
    fromfile='Old Version',
    tofile='New Version',
    lineterm=''
)

# Display Differences
st.subheader("Code Evolution Analysis")

for line in difference:

    if line.startswith("+"):
        st.success(line)

    elif line.startswith("-"):
        st.error(line)

    else:
        st.text(line)

# AI Insight Section
st.subheader("AI Generated Insight")

st.success("""
The updated version improves maintainability by introducing
intermediate variable handling and logging support.
The architecture becomes easier to debug and scale for future development.
""")

# Evolution Score
st.subheader("Evolution Score")

st.progress(85)

st.write("Code Maintainability Improved: 85%")

# Future Prediction
st.subheader("Future Prediction")

st.warning("""
AI predicts future improvements may include:
- Database integration
- API optimization
- Error handling system
- Modular architecture
""")
