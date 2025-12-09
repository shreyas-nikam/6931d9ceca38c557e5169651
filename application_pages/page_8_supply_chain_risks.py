import streamlit as st
from utils import add_ai_model_st, add_supply_chain_risk_st
import pandas as pd


def main():
    st.subheader("8. Addressing Supply Chain and Data Provenance Risks")
    st.markdown("""
        Beyond direct model vulnerabilities, Sarah also considers the broader "AI Supply Chain" (Section 3). A recent internal review highlighted potential data provenance issues for a separate "Fraud Detection System" and its reliance on a critical third-party feature engineering library. Sarah needs to register these "Data Provenance" (3.2) and "Third-Party Dependency" (3.3) risks. This is critical for understanding risks related to data quality, integrity, and external components, concepts that are central to maintaining the trustworthiness of AI systems.

        Ensuring the quality and origin of data, as well as vetting third-party components, helps Sarah manage cascading vulnerabilities and maintain the overall security of QuantFinance Bank's AI portfolio.
    """)

    fraud_detection_model_name = "Fraud Detection System"
    fraud_model_id = None
    existing_fraud_model = st.session_state.ai_models_df[
        st.session_state.ai_models_df['model_name'] == fraud_detection_model_name]

    if existing_fraud_model.empty:
        st.info(
            f"Model '{fraud_detection_model_name}' not found. Registering it first to proceed.")
        # Automatically add the model if it doesn't exist
        fraud_model_id = add_ai_model_st(
            model_name=fraud_detection_model_name,
            use_case="Detecting fraudulent financial transactions in real-time",
            description="Supervised learning model trained on historical transaction data to flag suspicious activities.",
            owner="Fraud Prevention Unit",
            status="In Production"
        )
        st.session_state.fraud_detection_model_id = fraud_model_id
        st.rerun()  # Rerun to reflect the new model in session state and allow risk addition
    else:
        fraud_model_id = existing_fraud_model['model_id'].iloc[0]
        st.info(
            f"Model '{fraud_detection_model_name}' (ID: {int(fraud_model_id)}) already exists. Proceed to add risks.")
        st.session_state.fraud_detection_model_id = fraud_model_id

    if fraud_model_id:
        st.markdown(
            f"Adding risks for model: **{fraud_detection_model_name}** (ID: {int(fraud_model_id)})")

        data_provenance_risk_exists = st.session_state.ai_risks_df[
            (st.session_state.ai_risks_df['model_id'] == fraud_model_id) &
            (st.session_state.ai_risks_df['hazard_description'].str.contains(
                "Data Provenance", na=False))
        ].empty == False

        third_party_risk_exists = st.session_state.ai_risks_df[
            (st.session_state.ai_risks_df['model_id'] == fraud_model_id) &
            (st.session_state.ai_risks_df['hazard_description'].str.contains(
                "Third-Party Dependency", na=False))
        ].empty == False

        if not data_provenance_risk_exists:
            st.markdown(
                "### Add Data Provenance Risk for Fraud Detection System")
            with st.form("add_data_provenance_risk_form"):
                dp_hazard_description = st.text_area(
                    "Hazard Description (Data Provenance)", "Lack of verifiable data provenance for historical transaction data used in training, raising concerns about data integrity and potential hidden biases.", key="dp_desc_8")
                dp_likelihood = st.slider(
                    "Likelihood (1-5)", 1, 5, 3, key="dp_likelihood_8")
                dp_magnitude = st.slider(
                    "Magnitude (1-5)", 1, 5, 4, key="dp_magnitude_8")
                dp_submitted = st.form_submit_button(
                    "Add Data Provenance Risk")

                if dp_submitted:
                    add_supply_chain_risk_st(
                        model_name=fraud_detection_model_name, model_use_case="Detecting fraudulent financial transactions in real-time", model_description="Supervised learning model trained on historical transaction data to flag suspicious activities.", model_owner="Fraud Prevention Unit", model_status="In Production",
                        risk_type="Data Risk", hazard_description=dp_hazard_description, likelihood=dp_likelihood, magnitude=dp_magnitude
                    )
                    st.session_state.show_dp_success = True
                    st.rerun()
        else:
            st.info("Data Provenance Risk already added.")
        
        # Display success message after rerun
        if st.session_state.get('show_dp_success', False):
            st.success(
                "✅ Data Provenance Risk added successfully! Refer to the updated AI Risk Register below.")
            st.session_state.show_dp_success = False

        if not third_party_risk_exists:
            st.markdown(
                "### Add Third-Party Dependency Risk for Fraud Detection System")
            with st.form("add_third_party_risk_form"):
                tpd_hazard_description = st.text_area("Hazard Description (Third-Party Dependency)",
                                                      "Reliance on a third-party feature engineering library with unknown vulnerabilities or insufficient documentation.", key="tpd_desc_8")
                tpd_likelihood = st.slider(
                    "Likelihood (1-5)", 1, 5, 3, key="tpd_likelihood_8")
                tpd_magnitude = st.slider(
                    "Magnitude (1-5)", 1, 5, 3, key="tpd_magnitude_8")
                tpd_submitted = st.form_submit_button(
                    "Add Third-Party Dependency Risk")

                if tpd_submitted:
                    add_supply_chain_risk_st(
                        model_name=fraud_detection_model_name, model_use_case="Detecting fraudulent financial transactions in real-time", model_description="Supervised learning model trained on historical transaction data to flag suspicious activities.", model_owner="Fraud Prevention Unit", model_status="In Production",
                        risk_type="Organizational Risk", hazard_description=tpd_hazard_description, likelihood=tpd_likelihood, magnitude=tpd_magnitude
                    )
                    st.session_state.show_tpd_success = True
                    st.rerun()
        else:
            st.info("Third-Party Dependency Risk already added.")
        
        # Display success message after rerun
        if st.session_state.get('show_tpd_success', False):
            st.success(
                "✅ Third-Party Dependency Risk added successfully! Refer to the updated AI Risk Register below.")
            st.session_state.show_tpd_success = False

        # Only allow advancing if both risks are added or acknowledged
        if data_provenance_risk_exists and third_party_risk_exists:
            st.success(
                "✅ Supply chain risks added! Proceed to Define Controls...")
            st.session_state.current_step = 9

    st.markdown("\n**Updated AI Models Register:**")
    st.dataframe(st.session_state.ai_models_df)
    st.markdown("\n**Updated AI Risks Register:**")
    st.dataframe(st.session_state.ai_risks_df)
