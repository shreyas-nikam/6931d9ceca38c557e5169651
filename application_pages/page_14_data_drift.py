import streamlit as st
from utils import simulate_data_drift_alert_st, add_ai_model_st
import pandas as pd


def main():
    st.subheader(
        "14. Simulating Operational Monitoring Feedback: Detecting Data Drift")
    st.markdown("""
        AI risk management is not a one-time activity; it requires continuous vigilance. Sarah receives an alert from the bank's model monitoring system for the Credit Score Predictor, indicating a significant "Data Drift" (1.4.1) in the input features. This operational feedback is a critical trigger for re-evaluating the associated risks and exemplifies the "Continuous Validation" (4.5) aspect of the AI RMF.

        This scenario demonstrates the necessity of an "Adaptive Cycle" or "outer loop" (1.4.3), where operational data constantly informs risk assessment, prompting Sarah to re-evaluate and update the risk register to maintain trust and performance.
    """)

    credit_score_predictor_model_id = None
    if 'credit_score_predictor_model_id' in st.session_state:
        credit_score_predictor_model_id = st.session_state.credit_score_predictor_model_id
    elif 'Credit Score Predictor' in st.session_state.ai_models_df['model_name'].values:
        credit_score_predictor_model_id = st.session_state.ai_models_df[
            st.session_state.ai_models_df['model_name'] == 'Credit Score Predictor']['model_id'].iloc[0]

    if credit_score_predictor_model_id:
        st.info(
            f"Simulating data drift alert for model: **Credit Score Predictor** (ID: {int(credit_score_predictor_model_id)})")

        # Check if Data Drift risk already exists
        data_drift_risk_exists = st.session_state.ai_risks_df[
            (st.session_state.ai_risks_df['model_id'] == credit_score_predictor_model_id) &
            (st.session_state.ai_risks_df['risk_type'] == "Data Drift")
        ].empty == False

        if not data_drift_risk_exists:
            with st.form("simulate_drift_form"):
                st.text_input("Simulated Alert: Risk Type", "Data Drift",
                              disabled=True, key="drift_risk_type_14")
                hazard_description = st.text_area(
                    "Hazard Description (Data Drift)", "Significant shift in demographic distribution of loan applicants causing potential model inaccuracy.", key="drift_hazard_14")
                new_likelihood = st.slider(
                    "New Likelihood (1-5)", 1, 5, 4, key="drift_likelihood_14")
                new_magnitude = st.slider(
                    "New Magnitude (1-5)", 1, 5, 4, key="drift_magnitude_14")
                submitted = st.form_submit_button(
                    "Simulate Data Drift & Update Risk")

                if submitted:
                    simulate_data_drift_alert_st(
                        credit_score_predictor_model_id,
                        "Data Drift",
                        hazard_description,
                        new_likelihood,
                        new_magnitude
                    )
                    st.rerun()
        else:
            st.info(
                "The 'Data Drift' risk for Credit Score Predictor has already been simulated and updated.")

        # Show success message if data drift risk exists
        if data_drift_risk_exists or st.session_state.ai_risks_df[
            (st.session_state.ai_risks_df['model_id'] == credit_score_predictor_model_id) &
            (st.session_state.ai_risks_df['risk_type'] == "Data Drift")
        ].empty == False:
            st.success(
                "✅ Data drift simulated! Proceed to Update Risk Assessment...")
            st.session_state.current_step = 8

    else:
        st.error(
            "Credit Score Predictor model not found. Please ensure it is registered in Step 3.")
        if st.button("Go to Step 3", key="go_to_step3_from14"):
            st.session_state.current_step = 3
            st.rerun()

    st.markdown("\n**Updated AI Risks Register after data drift simulation:**")
    st.dataframe(
        st.session_state.ai_risks_df[st.session_state.ai_risks_df['model_id'] == credit_score_predictor_model_id])
