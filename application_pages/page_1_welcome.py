import streamlit as st
from utils import initialize_risk_management_system_st


def main():
    st.subheader(
        "1. Setting the Stage: Initializing QuantFinance Bank's AI Risk Management System")
    st.markdown("""
        Sarah's first step is to lay the groundwork for a robust AI risk management system. This involves setting up the core data structures that will store information about AI models, identified risks, and their associated controls. This centralized repository is crucial for maintaining a transparent and comprehensive overview of all AI-related risks across QuantFinance Bank, aligning with the "Centralized Repository" concept from the AI RMF.

        This foundational setup enables a systematic record of identified AI hazards and risks, which is essential for proactive risk management and effective communication among stakeholders.
    """)

    # Check if system is already initialized
    if 'system_initialized' not in st.session_state:
        st.session_state.system_initialized = False

    if st.button("Initialize AI Risk Management System", key="init_system_btn"):
        initialize_risk_management_system_st()
        st.session_state.system_initialized = True
        st.rerun()

    # Only show registers after initialization
    if st.session_state.system_initialized:
        st.success("✅ AI Model Risk Register system initialized successfully!")
        st.info(
            "👉 The system has created three empty registers ready to track AI models, risks, and controls.")
        st.markdown("\n**Current State of Risk Registers:**")
        st.markdown(
            "**Status:** ✅ System Initialized - Ready to register models and risks")

        st.markdown("### AI Models Register")
        st.dataframe(st.session_state.ai_models_df, use_container_width=True)
        if st.session_state.ai_models_df.empty:
            st.caption(
                "_No models registered yet. Models will be added in Step 3._")

        st.markdown("### AI Risks Register")
        st.dataframe(st.session_state.ai_risks_df, use_container_width=True)
        if st.session_state.ai_risks_df.empty:
            st.caption(
                "_No risks identified yet. Risks will be added starting from Step 4._")

        st.markdown("### AI Controls Register")
        st.dataframe(st.session_state.ai_controls_df, use_container_width=True)
        if st.session_state.ai_controls_df.empty:
            st.caption(
                "_No controls defined yet. Controls will be added in Step 9._")

        # Auto-advance to next step
        st.success("✅ Step 1 completed! Proceed to AI Risk Taxonomy.")
        st.session_state.current_step = 2
