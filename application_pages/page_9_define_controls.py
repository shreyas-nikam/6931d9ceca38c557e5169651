import streamlit as st
from utils import add_ai_control_st
import pandas as pd


def main():
    st.subheader("9. Defining Controls and Mitigation Strategies")
    st.markdown("""
        Having identified and quantified several risks, Sarah's next crucial step is to define and propose specific controls to mitigate them. This involves designing defenses tailored to each identified risk, from technical measures like input sanitization to procedural controls like regular model retraining. This directly applies the "Risk Controls and Mitigation Strategies" concept from the AI RMF (Section 4.3), emphasizing "Mapping Controls to Risks" and "Hierarchical Control Design."

        By establishing clear controls, Sarah ensures that QuantFinance Bank has concrete plans to reduce the likelihood or impact of identified risks, thereby strengthening the overall resilience of its AI systems against threats like adversarial attacks and data quality issues.
    """)

    # Identify relevant risk IDs for controls
    # Algorithmic Bias is stored in risk_type
    algorithmic_bias_risk_id = st.session_state.ai_risks_df[st.session_state.ai_risks_df['risk_type'].str.contains(
        'Algorithmic Bias', na=False)]['risk_id'].iloc[0] if not st.session_state.ai_risks_df[st.session_state.ai_risks_df['risk_type'].str.contains('Algorithmic Bias', na=False)].empty else None
    # Adversarial Attack is stored in hazard_description (risk_type is "Model Risk")
    adversarial_attack_risk_id = st.session_state.ai_risks_df[st.session_state.ai_risks_df['hazard_description'].str.contains(
        'Adversarial Attack', na=False, case=False)]['risk_id'].iloc[0] if not st.session_state.ai_risks_df[st.session_state.ai_risks_df['hazard_description'].str.contains('Adversarial Attack', na=False, case=False)].empty else None
    # Data Provenance is stored in hazard_description (risk_type is "Data Risk") - search for "provenance" in lowercase
    data_provenance_risk_id = st.session_state.ai_risks_df[st.session_state.ai_risks_df['hazard_description'].str.contains(
        'provenance', na=False, case=False)]['risk_id'].iloc[0] if not st.session_state.ai_risks_df[st.session_state.ai_risks_df['hazard_description'].str.contains('provenance', na=False, case=False)].empty else None

    # Helper to check if a control for a given risk_id and description exists
    def control_exists(risk_id, control_desc_part):
        if risk_id is None:
            return False
        return not st.session_state.ai_controls_df[
            (st.session_state.ai_controls_df['risk_id'] == risk_id) &
            (st.session_state.ai_controls_df['control_description'].str.contains(
                control_desc_part, na=False))
        ].empty

    st.markdown("Sarah, define controls for the following identified risks:")

    all_controls_added = True

    if algorithmic_bias_risk_id:
        if not control_exists(algorithmic_bias_risk_id, "fairness metrics monitoring"):
            if st.button(f"Add Control for Algorithmic Bias (Risk ID: {int(algorithmic_bias_risk_id)})", key="add_control_ab"):
                add_ai_control_st(
                    algorithmic_bias_risk_id,
                    "Implement fairness metrics monitoring (e.g., Equal Opportunity, Demographic Parity) and regular bias audits."
                )
                st.rerun()
            all_controls_added = False
        else:
            st.info(
                f"Control for Algorithmic Bias (Risk ID: {int(algorithmic_bias_risk_id)}) defined below.")
    else:
        st.warning(
            "Algorithmic Bias risk not found. Please ensure it was added in previous steps.")

    if adversarial_attack_risk_id:
        if not control_exists(adversarial_attack_risk_id, "adversarial training techniques"):
            if st.button(f"Add Control for Adversarial Attack (Risk ID: {int(adversarial_attack_risk_id)})", key="add_control_aa"):
                add_ai_control_st(
                    adversarial_attack_risk_id,
                    "Implement adversarial training techniques and robust input validation/sanitization mechanisms."
                )
                st.rerun()
            all_controls_added = False
        else:
            st.info(
                f"Control for Adversarial Attack (Risk ID: {int(adversarial_attack_risk_id)}) defined below.")
    else:
        st.warning(
            "Adversarial Attack risk not found. Please ensure it was added in previous steps.")

    if data_provenance_risk_id:
        if not control_exists(data_provenance_risk_id, "data lineage tracking"):
            if st.button(f"Add Control for Data Provenance (Risk ID: {int(data_provenance_risk_id)})", key="add_control_dp"):
                add_ai_control_st(
                    data_provenance_risk_id,
                    "Establish clear data lineage tracking and cryptographic hashing for all training datasets."
                )
                st.rerun()
            all_controls_added = False
        else:
            st.info(
                f"Control for Data Provenance (Risk ID: {int(data_provenance_risk_id)}) defined below.")
    else:
        st.warning(
            "Data Provenance risk not found. Please ensure it was added in previous steps.")

    st.markdown("\n**Updated AI Controls Register:**")
    st.dataframe(st.session_state.ai_controls_df)

    if all_controls_added:  # Only show 'Proceed' button if all specific controls were added or existed
        st.success(
            "✅ Controls defined! Proceed to Assign Risk Response Options.")
        st.session_state.current_step = 6
