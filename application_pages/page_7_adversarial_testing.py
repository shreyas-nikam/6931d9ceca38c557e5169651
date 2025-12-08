import streamlit as st
from utils import add_adversarial_risk_st
import pandas as pd


def main():
    st.subheader(
        "7. Integrating Insights from Adversarial Testing: Uncovering Robustness Risks")
    st.markdown("""
        QuantFinance Bank's dedicated Red-Teaming unit has just concluded an exercise targeting the Credit Score Predictor. Their findings reveal vulnerabilities to "Adversarial Attacks" – subtle manipulations of input data that can cause misclassification (e.g., making a high-risk applicant appear low-risk). Sarah must immediately integrate these critical insights into the risk register. This directly reflects the importance of "Adversarial Testing and Red-Teaming" (Section 2) in the AI RMF for uncovering AI-specific security vulnerabilities like "Deceptive Inputs" (2.2) and "Data Poisoning Attacks" (2.4).

        By documenting these specific threats, Sarah ensures the bank can develop targeted defenses, preventing malicious actors from exploiting the model and protecting the integrity of loan decisions.
    """)

    credit_score_predictor_model_id = None
    if 'credit_score_predictor_model_id' in st.session_state:
        credit_score_predictor_model_id = st.session_state.credit_score_predictor_model_id
    elif 'Credit Score Predictor' in st.session_state.ai_models_df['model_name'].values:
        credit_score_predictor_model_id = st.session_state.ai_models_df[
            st.session_state.ai_models_df['model_name'] == 'Credit Score Predictor']['model_id'].iloc[0]

    if credit_score_predictor_model_id:
        st.write(
            f"Adding adversarial risk for model: **Credit Score Predictor** (ID: {int(credit_score_predictor_model_id)})")

        # Check if the adversarial risk is already added
        adversarial_risk_exists = st.session_state.ai_risks_df[
            (st.session_state.ai_risks_df['model_id'] == credit_score_predictor_model_id) &
            (st.session_state.ai_risks_df['risk_type'] == "Model Risk") &
            (st.session_state.ai_risks_df['hazard_description'].str.contains(
                "Adversarial Attack", na=False))
        ].empty == False

        if not adversarial_risk_exists:
            with st.form("add_adversarial_risk_form"):
                attack_type = st.text_input(
                    "Adversarial Attack Type", "Adversarial Attack (Evasion)", key="attack_type_7")
                description = st.text_area(
                    "Description", "Subtle manipulation of input features to cause a misclassification of a high-risk individual as low-risk.", key="description_7")
                likelihood = st.slider(
                    "Likelihood (1-5)", 1, 5, 4, key="adv_likelihood_7")
                magnitude = st.slider(
                    "Magnitude (1-5)", 1, 5, 5, key="adv_magnitude_7")
                submitted = st.form_submit_button(
                    "Add Adversarial Risk & Score")

                if submitted:
                    add_adversarial_risk_st(
                        credit_score_predictor_model_id, attack_type, description, likelihood, magnitude)
                    st.session_state.current_step = 5
                    st.rerun()
        else:
            st.success(
                "✅ Adversarial risk already added! Proceed to Supply Chain & Data Provenance Risks.")
            st.session_state.current_step = 5

    else:
        st.error(
            "Credit Score Predictor model not found. Please ensure it's registered in Step 3.")
        if st.button("Go to Step 3", key="go_to_step3_from7"):
            st.session_state.current_step = 3
            st.rerun()

    st.markdown("\n**Updated AI Risks Register with adversarial attack risk:**")
    st.dataframe(st.session_state.ai_risks_df)
