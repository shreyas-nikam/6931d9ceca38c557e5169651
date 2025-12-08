import streamlit as st
from utils import add_ai_risk_st
import pandas as pd

def main():
    st.subheader("4. Initial Risk Identification: Potential Hazards for the Credit Score Model")
    st.markdown("""
        With the Credit Score Predictor registered, Sarah begins the crucial process of identifying potential AI-specific hazards. She draws upon her expertise and the bank's risk taxonomy to foresee issues that could arise from data quality, model behavior, or operational deployment. This proactive identification is key to mitigating future problems and aligns with Section 4.2 of the AI RMF, focusing on "Risk Register: Identification and Categorization."

        Sarah considers risks like "Data Quality" (poor input data leading to incorrect scores), "Algorithmic Bias" (unfair scoring for certain demographic groups), and "Performance Degradation" (the model's accuracy declining over time). This step is crucial for anticipating challenges and preventing negative impacts on customers and the bank's reputation.
    """)

    credit_score_predictor_model_id = None
    if 'credit_score_predictor_model_id' in st.session_state:
        credit_score_predictor_model_id = st.session_state.credit_score_predictor_model_id
    elif 'Credit Score Predictor' in st.session_state.ai_models_df['model_name'].values:
        credit_score_predictor_model_id = st.session_state.ai_models_df[st.session_state.ai_models_df['model_name'] == 'Credit Score Predictor']['model_id'].iloc[0]


    if credit_score_predictor_model_id:
        st.write(f"Adding risks for model: **Credit Score Predictor** (ID: {int(credit_score_predictor_model_id)})")
        
        # Define the risks to add
        risks_to_add = [
            {"type": "Data Quality", "description": "Poor or incomplete historical data leading to inaccurate credit scores."},
            {"type": "Algorithmic Bias", "description": "Model exhibits biased decision-making against certain demographic groups."},
            {"type": "Performance Degradation", "description": "Model accuracy degrades over time due to changes in credit behavior patterns."}
        ]

        # Use a form to add risks to ensure only one action per rerun if multiple buttons are clicked
        with st.form("initial_risk_identification_form"):
            st.markdown("Sarah, select the risks to add to the register for the Credit Score Predictor.")
            
            # Check if risks are already added to avoid duplicates in the UI
            current_risks = st.session_state.ai_risks_df[st.session_state.ai_risks_df['model_id'] == credit_score_predictor_model_id]['hazard_description'].tolist()
            
            for i, risk in enumerate(risks_to_add):
                if risk['description'] not in current_risks:
                    if st.checkbox(f"Add **{risk['type']}**: {risk['description']}", key=f"add_risk_checkbox_{i}"):
                        add_ai_risk_st(credit_score_predictor_model_id, risk['type'], risk['description'])
                else:
                    st.success(f"Risk '{risk['type']}' already added: {risk['description']}")
            
            submitted_add_risks = st.form_submit_button("Confirm Added Risks")
            if submitted_add_risks:
                st.success("Risks confirmed.")
                st.session_state.current_step = 5
                st.rerun()

        st.markdown("\n**Updated AI Risks Register (for Credit Score Predictor):**")
        st.dataframe(st.session_state.ai_risks_df[st.session_state.ai_risks_df['model_id'] == credit_score_predictor_model_id])

        if st.button("Proceed to Quantify Risks", key="next_step4_btn"):
            st.session_state.current_step = 5
            st.rerun()
    else:
        st.error("Credit Score Predictor model not found. Please go back to Step 3 to register it.")
        if st.button("Go to Step 3", key="go_to_step3_from4"):
            st.session_state.current_step = 3
            st.rerun()
