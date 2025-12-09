import streamlit as st
from utils import identify_top_risks_st, get_full_risk_register_st
import pandas as pd


def main():
    st.subheader("12. Analyzing and Prioritizing High-Scoring Risks")
    st.markdown("""
        With a growing number of AI models and associated risks, Sarah needs an efficient way to identify and prioritize the most critical threats. Analyzing risks by their `composite_risk_score` allows her to pinpoint the highest-scoring hazards, ensuring that resources and attention are directed where they are most needed. This aligns with the AI RMF's principle of "Risk-based" decision-making.

        This analysis helps Sarah focus on the "top risks" that pose the greatest potential harm to QuantFinance Bank, enabling proactive resource allocation and strategic risk mitigation.
    """)

    if 'full_risk_register_df' not in st.session_state or st.session_state.full_risk_register_df.empty:
        st.warning(
            "Please generate the comprehensive risk register in Step 11 first to identify top risks.")
        return

    num_top_risks = st.number_input(
        "Number of Top Risks to Display", min_value=1, value=3, step=1, key="num_top_risks_12")

    if st.button("Identify Top Risks", key="identify_top_risks_btn"):
        identify_top_risks_st(num_top_risks)
        st.session_state.current_step = 7
        st.rerun()

    if 'top_risks_df' in st.session_state and not st.session_state.top_risks_df.empty:
        st.markdown(f"\n**Top {num_top_risks} AI Risks by Composite Score:**")
        st.dataframe(st.session_state.top_risks_df)
        st.caption(
            "These are the most critical risks identified, requiring immediate attention.")
        st.success(
            "✅ Top risks identified! Proceed to Visualize Risk Distribution.")
    else:
        st.info("No top risks identified yet. Click 'Identify Top Risks' above.")
