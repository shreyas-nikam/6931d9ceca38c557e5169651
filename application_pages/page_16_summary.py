import streamlit as st
from utils import get_full_risk_register_st, identify_top_risks_st, plot_risk_distribution_by_type_st, restart_workflow
import pandas as pd

def main():
    st.subheader("AI Risk Management Workflow Completed!")
    st.markdown("""
        Sarah has successfully navigated the complex landscape of AI risk management. From initial system setup and model registration to identifying, assessing, mitigating, and continuously monitoring risks—she has built a comprehensive and adaptive AI risk posture for QuantFinance Bank.

        This continuous feedback loop ensures that the bank's AI models remain trustworthy and perform reliably in evolving environments.
    """)
    st.balloons()
    
    st.markdown("### Final Comprehensive AI Model Risk Register")
    if 'full_risk_register_df' not in st.session_state or st.session_state.full_risk_register_df.empty:
        get_full_risk_register_st()
    st.dataframe(st.session_state.full_risk_register_df)

    st.markdown("### Final Top Risks Overview")
    if 'top_risks_df' not in st.session_state or st.session_state.top_risks_df.empty:
        identify_top_risks_st(num_top_risks=3) # Default 3 for summary
    st.dataframe(st.session_state.top_risks_df)
    st.caption("These represent the most critical AI risks for QuantFinance Bank, requiring ongoing attention.")

    st.markdown("### Overall AI Risk Distribution")
    plot_risk_distribution_by_type_st()
    st.caption("This chart provides a strategic overview of risk concentrations across different categories.")

    st.success("Sarah has established a robust AI risk management framework!")
    if st.button("Restart Workflow", key="reset_app_final"):
        restart_workflow()
