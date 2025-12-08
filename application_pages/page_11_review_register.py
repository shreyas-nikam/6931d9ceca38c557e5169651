import streamlit as st
from utils import get_full_risk_register_st
import pandas as pd

def main():
    st.subheader("11. Reviewing the Comprehensive AI Model Risk Register")
    st.markdown("""
        At this stage, Sarah needs to review the entire AI Model Risk Register to get a holistic view of the bank's AI risk landscape. This comprehensive display, integrating models, risks, assessments, and controls, is the "Centralized Repository" described in the AI RMF (Section 4.2). It allows Sarah to verify that all necessary information is captured and interconnected.

        This unified view is essential for Sarah to present to internal audit and senior management, demonstrating transparent and systematic AI risk governance across QuantFinance Bank.
    """)

    if st.button("Generate Comprehensive AI Model Risk Register", key="generate_full_register_btn"):
        get_full_risk_register_st()
        st.session_state.current_step = 12
        st.rerun()
    
    if 'full_risk_register_df' in st.session_state and not st.session_state.full_risk_register_df.empty:
        st.markdown("\n**Comprehensive AI Model Risk Register:**")
        st.dataframe(st.session_state.full_risk_register_df)
    else:
        st.warning("The full risk register has not been generated yet. Click the button above.")
    
    if 'full_risk_register_df' in st.session_state and not st.session_state.full_risk_register_df.empty: # Show next button only if register is generated
        if st.button("Proceed to Analyze Top Risks", key="next_step11_btn"):
            st.session_state.current_step = 12
            st.rerun()
