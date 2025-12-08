import streamlit as st
from utils import update_risk_assessment_from_monitoring_st
import pandas as pd

def main():
    st.subheader("15. Updating Risk Assessment based on Monitoring Feedback")
    st.markdown("""
        Following the data drift alert, Sarah must now formally update the risk assessment for the "Credit Score Predictor". This involves adjusting the likelihood and/or magnitude scores for relevant risks, such as "Performance Degradation" or the newly identified "Data Drift," to reflect the new operational reality. This exemplifies "Continuous Validation" and "Post-Deployment Monitoring" (4.5), which are essential for maintaining the trustworthiness of adaptive AI systems.

        By continuously refining risk assessments based on real-time monitoring, Sarah ensures that the risk register remains a living document that accurately reflects the current state of AI risks at QuantFinance Bank, supporting agile risk management.
    """)

    credit_score_predictor_model_id = None
    if 'credit_score_predictor_model_id' in st.session_state:
        credit_score_predictor_model_id = st.session_state.credit_score_predictor_model_id
    elif 'Credit Score Predictor' in st.session_state.ai_models_df['model_name'].values:
        credit_score_predictor_model_id = st.session_state.ai_models_df[st.session_state.ai_models_df['model_name'] == 'Credit Score Predictor']['model_id'].iloc[0]

    if credit_score_predictor_model_id:
        st.info("The data drift event directly impacts the model's 'Performance Degradation' risk, requiring an update to its assessment.")
        
        target_risk_type = "Performance Degradation"
        updated_likelihood_val = 4
        updated_magnitude_val = 4

        # Get current scores for Performance Degradation
        perf_degrad_risk = st.session_state.ai_risks_df[
            (st.session_state.ai_risks_df['model_id'] == credit_score_predictor_model_id) & 
            (st.session_state.ai_risks_df['risk_type'] == target_risk_type)
        ]
        
        needs_update = True
        if not perf_degrad_risk.empty:
            current_likelihood = perf_degrad_risk['likelihood_score'].iloc[0]
            current_magnitude = perf_degrad_risk['magnitude_score'].iloc[0]
            if current_likelihood == updated_likelihood_val and current_magnitude == updated_magnitude_val:
                needs_update = False
        else:
            st.warning(f"Risk type '{target_risk_type}' not found for Credit Score Predictor. Ensure it was added in Step 4.")
            needs_update = False # Cannot update if not found

        if needs_update:
            st.markdown("Updating 'Performance Degradation' risk based on the data drift event:")
            if st.button("Formally Update Performance Degradation Risk", key="update_perf_degrad_btn"):
                update_risk_assessment_from_monitoring_st(
                    credit_score_predictor_model_id,
                    target_risk_type,
                    updated_likelihood_val,
                    updated_magnitude_val
                )
                st.session_state.current_step = 16 # Advance to a final summary view
                st.rerun()
        else:
            st.info("The 'Performance Degradation' risk is already updated or does not exist for the Credit Score Predictor. Proceed to summary.")
            if st.button("Proceed to Final Summary", key="proceed_final_summary_btn"):
                st.session_state.current_step = 16
                st.rerun()

        st.markdown("\n**Updated AI Risks Register after monitoring feedback:**")
        st.dataframe(st.session_state.ai_risks_df[st.session_state.ai_risks_df['model_id'] == credit_score_predictor_model_id])

    else:
        st.error("Credit Score Predictor model not found. Cannot update risk assessment. Please ensure it is registered in Step 3.")
        if st.button("Go to Step 3", key="go_to_step3_from15"):
            st.session_state.current_step = 3
            st.rerun()
