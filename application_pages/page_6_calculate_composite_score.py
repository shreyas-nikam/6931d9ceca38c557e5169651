import streamlit as st
from utils import calculate_composite_risk_score_st
import pandas as pd


def main():
    st.subheader("6. Calculating the Composite Risk Score")
    st.markdown(r"""
        With likelihood and magnitude scores assigned, Sarah can now calculate the composite risk score for each hazard. This score, derived from the formula $\text{Risk} = P(\text{event}) \times M(\text{consequence})$, provides a single, aggregated metric for each risk, allowing for easy comparison and prioritization. This calculation is a direct application of the "Quantitative and Qualitative Assessment" mentioned in the AI RMF (Section 4.2).

        By standardizing risk quantification, Sarah ensures that all stakeholders at QuantFinance Bank can understand and compare the severity of different AI risks, guiding resource allocation for risk mitigation.
    """)

    uncalculated_risks = st.session_state.ai_risks_df[
        st.session_state.ai_risks_df['composite_risk_score'].isna() &
        st.session_state.ai_risks_df['likelihood_score'].notna() &
        st.session_state.ai_risks_df['magnitude_score'].notna()
    ]

    if not uncalculated_risks.empty:
        st.info("Sarah, click the button below to calculate the composite risk scores for all risks with assigned likelihood and magnitude.")

        # Show the calculation details for each uncalculated risk
        st.markdown("### Risks Ready for Composite Score Calculation:")
        for idx, risk in uncalculated_risks.iterrows():
            with st.expander(f"Risk ID {int(risk['risk_id'])}: {risk['risk_type']} - {risk['hazard_description'][:50]}..."):
                st.write(f"**Risk Type:** {risk['risk_type']}")
                st.write(
                    f"**Hazard Description:** {risk['hazard_description']}")
                st.write(f"**Likelihood Score:** {risk['likelihood_score']}")
                st.write(f"**Magnitude Score:** {risk['magnitude_score']}")
                st.markdown("---")
                st.markdown("**Calculation:**")
                st.latex(
                    r"\text{Composite Risk Score} = \text{Likelihood} \times \text{Magnitude}")
                st.latex(
                    rf"\text{{Composite Risk Score}} = {risk['likelihood_score']} \times {risk['magnitude_score']} = {risk['likelihood_score'] * risk['magnitude_score']}")

        if st.button("Calculate All Composite Risk Scores", key="calculate_composite_btn"):
            for risk_id in uncalculated_risks['risk_id']:
                calculate_composite_risk_score_st(int(risk_id))
            st.rerun()

    if st.session_state.ai_risks_df['composite_risk_score'].notna().any():
        st.success(
            "✅ Composite scores calculated! Proceed to Integrating Adversarial Insights.")
        st.session_state.current_step = 5
    elif uncalculated_risks.empty:
        st.success(
            "✅ All composite scores are ready! Proceed to Integrating Adversarial Insights.")
        st.session_state.current_step = 5

    st.markdown("\n**Updated AI Risks Register with Composite Risk Scores:**")
    st.dataframe(st.session_state.ai_risks_df)
    st.caption("A higher composite score indicates a more critical risk, requiring greater attention and resource allocation for mitigation.")
