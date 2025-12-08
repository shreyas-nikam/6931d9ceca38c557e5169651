import streamlit as st
from utils import initialize_risk_management_system_st

def main():
    st.subheader("1. Setting the Stage: Initializing QuantFinance Bank's AI Risk Management System")
    st.markdown("""
        Sarah's first step is to lay the groundwork for a robust AI risk management system. This involves setting up the core data structures that will store information about AI models, identified risks, and their associated controls. This centralized repository is crucial for maintaining a transparent and comprehensive overview of all AI-related risks across QuantFinance Bank, aligning with the "Centralized Repository" concept from the AI RMF.

        This foundational setup enables a systematic record of identified AI hazards and risks, which is essential for proactive risk management and effective communication among stakeholders.
    """)
    if st.button("Initialize AI Risk Management System", key="init_system_btn"):
        initialize_risk_management_system_st()
        st.session_state.current_step = 2
        st.rerun()
    
    st.markdown("\n**Current State of Risk Registers (Initially Empty):**")
    st.markdown("### AI Models Register")
    st.dataframe(st.session_state.ai_models_df)
    st.markdown("### AI Risks Register")
    st.dataframe(st.session_state.ai_risks_df)
    st.markdown("### AI Controls Register")
    st.dataframe(st.session_state.ai_controls_df)
