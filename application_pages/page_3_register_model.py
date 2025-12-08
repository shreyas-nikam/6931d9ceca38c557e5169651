import streamlit as st
from utils import add_ai_model_st
import pandas as pd


def main():
    st.subheader("3. Registering a New AI Model: The Credit Score Predictor")
    st.markdown("""
        QuantFinance Bank is preparing to deploy a new AI-powered "Credit Score Predictor" model, which is critical for loan approvals. Sarah's immediate task is to formally register this model in the system, capturing its essential details, intended use, and initial status. This initial registration is a fundamental step in the AI RMF process, ensuring that every AI model under the bank's purview is documented from its inception.

        By registering the model early, Sarah ensures that all subsequent risk assessments and control implementations are tied to a specific, well-defined AI asset, providing clear accountability and traceability.
    """)

    with st.form("add_model_form"):
        model_name = st.text_input(
            "Model Name", "Credit Score Predictor", key="model_name_3")
        use_case = st.text_area(
            "Use Case", "Automating credit risk assessment for loan applications", key="use_case_3")
        description = st.text_area(
            "Description", "Machine learning model predicting creditworthiness based on financial history and demographic data.", key="description_3")
        owner = st.text_input(
            "Owner", "Retail Banking Analytics", key="owner_3")
        status_options = ["In Development", "In Production", "Retired"]
        status = st.selectbox("Status", status_options, index=status_options.index(
            "In Development"), key="status_3")
        submitted = st.form_submit_button("Register AI Model")

        if submitted:
            # Check if model already exists before adding
            existing_model = st.session_state.ai_models_df[
                st.session_state.ai_models_df['model_name'] == model_name]
            if existing_model.empty:
                new_model_id = add_ai_model_st(
                    model_name, use_case, description, owner, status)
                st.session_state.credit_score_predictor_model_id = new_model_id
                st.session_state.current_step = 3
                st.rerun()
            else:
                st.warning(
                    f"Model '{model_name}' is already registered (ID: {int(existing_model['model_id'].iloc[0])}). Skipping addition.")
                st.session_state.credit_score_predictor_model_id = existing_model[
                    'model_id'].iloc[0]
                st.session_state.current_step = 3
                st.rerun()  # Proceed even if already exists

    st.markdown("\n**Updated AI Models Register:**")
    st.dataframe(st.session_state.ai_models_df)

    if not st.session_state.ai_models_df.empty:
        st.success(
            "✅ Model registered! Proceed to Initial Risk Identification.")
        st.session_state.current_step = 3
