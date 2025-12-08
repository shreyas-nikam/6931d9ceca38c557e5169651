import streamlit as st
from utils import plot_risk_distribution_by_type_st
import pandas as pd


def main():
    st.subheader("13. Visualizing Risk Distribution by Type")
    st.markdown("""
        To provide an executive overview of the bank's overall AI risk posture, Sarah wants to visualize how identified risks are distributed across the different categories defined in the AI Risk Taxonomy (e.g., Data, Model, System). This aggregation helps in understanding systemic weaknesses and informs strategic investments in risk management capabilities. This type of visualization supports the "MEASURE" function of the AI RMF and provides an aggregated view of risks.

        By visualizing the distribution, Sarah can identify if a particular risk category (e.g., "Model Risk") is disproportionately high, indicating a need for more robust controls or new policies in that area.
    """)

    # Check if chart has been generated
    if 'chart_generated' not in st.session_state:
        st.session_state.chart_generated = False

    if st.button("Generate Risk Distribution Chart", key="plot_risk_dist_btn"):
        st.session_state.chart_generated = True

    if st.session_state.chart_generated:
        plot_risk_distribution_by_type_st()
        st.success(
            "✅ Risk distribution chart generated! Proceed to Simulate Operational Monitoring.")
        st.session_state.current_step = 8
        st.session_state.chart_generated = False  # Reset for next time
