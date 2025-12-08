import streamlit as st
from utils import assign_risk_scores_st
import pandas as pd

def main():
    st.subheader("5. Quantifying Risk: Likelihood and Magnitude Assessment")
    st.markdown(r"""
        Identifying risks is only the first step; Sarah now needs to quantify them to understand their potential impact. For each identified risk, she will assess its likelihood of occurrence ($P(\text{event}))$ and the magnitude of potential harm ($M(\text{consequence}))$. This quantitative and qualitative assessment is fundamental to the AI RMF (Section 4.2), as it allows for a standardized way to prioritize risks across the bank's AI portfolio.

        The core formula for this assessment is:
        $$ \text{Risk} = P(\text{event}) \times M(\text{consequence}) $$
        where $P(\text{event})$ represents the likelihood of a risk event occurring, and $M(\text{consequence})$ represents the severity of the impact if the event occurs. These scores will typically be qualitative (e.g., Low, Medium, High) mapped to numerical scales (e.g., 1-5).
    """)

    risks_to_score = st.session_state.ai_risks_df[
        (st.session_state.ai_risks_df['likelihood_score'].isna()) | 
        (st.session_state.ai_risks_df['magnitude_score'].isna())
    ].copy()

    if not risks_to_score.empty:
        st.info("Sarah, use the sliders below to assign likelihood and magnitude scores for each risk. These scores are crucial for calculating the overall severity of each AI risk.")
        
        scored_risks_data = []
        with st.form("assign_scores_form"):
            for index, risk in risks_to_score.iterrows():
                risk_id = int(risk['risk_id'])
                st.markdown(f"**Risk ID: {risk_id}**")
                st.write(f"Type: {risk['risk_type']}")
                st.write(f"Hazard: {risk['hazard_description']}")
                
                likelihood = st.slider(f"Likelihood Score (1=Rarely, 5=Frequently) for Risk ID {risk_id}", 1, 5, 3, key=f"likelihood_{risk_id}")
                magnitude = st.slider(f"Magnitude Score (1=Minor, 5=Catastrophic) for Risk ID {risk_id}", 1, 5, 3, key=f"magnitude_{risk_id}")
                
                scored_risks_data.append({'risk_id': risk_id, 'likelihood': likelihood, 'magnitude': magnitude})
                st.markdown("---")
            
            submitted_scores = st.form_submit_button("Assign All Scores")

            if submitted_scores:
                for score_data in scored_risks_data:
                    assign_risk_scores_st(score_data['risk_id'], score_data['likelihood'], score_data['magnitude'])
                st.session_state.current_step = 6
                st.rerun()
    else:
        st.info("All identified risks have been scored. You can now proceed to calculate composite scores.")
        if st.button("Proceed to Calculate Composite Scores", key="next_step5_btn"):
            st.session_state.current_step = 6
            st.rerun()

    st.markdown("\n**Updated AI Risks Register with Likelihood and Magnitude Scores:**")
    st.dataframe(st.session_state.ai_risks_df)
