# %%
# !pip install streamlit

# %%Step 0: Importing Dependencies
import streamlit as st

# Step 1: Extracting Information from Clinical Notes
clinical_notes = """
Patient presents with symptoms of fatigue, increased thirst, and frequent urination. 
HbA1c level is elevated at 7.2%. Blood glucose levels are consistently above 200 mg/dL.
"""

# %% Step 2: Predicting Disease Risk (Example Model)
def predict_disease_risk(clinical_notes):
    # Assume a simple model for demonstration purposes
    return 0.8

risk = predict_disease_risk(clinical_notes)

# %% Step 3: Retrieving Medical Knowledge
def retrieve_medical_knowledge(risk):
    if risk > 0.5:
        return "Type 2 Diabetes is a chronic condition that affects how your body metabolizes sugar (glucose). It is important to manage your blood sugar levels through diet, exercise, and medication as prescribed by your doctor."
    else:
        return ""

knowledge = retrieve_medical_knowledge(risk)

# %% Step 4: GUI Development
st.title("Clinical Decision Support System")
st.subheader("Extracted Information from Clinical Notes:")
st.write(clinical_notes)
st.subheader("Predicted Disease Risk:")
st.write(f"Risk of Type 2 Diabetes: {risk}")
st.subheader("Medical Knowledge:")
st.write(knowledge)

