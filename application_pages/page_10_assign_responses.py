import streamlit as st
from utils import assign_risk_response_st
import pandas as pd


def main():
    st.subheader("10. Assigning Risk Response Options")
    st.markdown("""
        For each identified risk with its proposed controls, Sarah must now formalize the bank's "Risk Response Option" (Section 4.3). This involves deciding whether to mitigate, transfer, avoid, or accept the risk based on the severity of the residual risk (after controls) and the bank's overall risk tolerance. This strategic decision-making is a core part of the AI RMF, ensuring that every risk has a clear management plan.

        This step helps Sarah communicate to stakeholders exactly how each AI risk will be handled, ensuring alignment with the bank's broader risk appetite and regulatory requirements.
    """)

    controls_to_respond = st.session_state.ai_controls_df[
        (st.session_state.ai_controls_df['effectiveness_score'].isna()) |
        (st.session_state.ai_controls_df['risk_response'].isna())
    ].copy()

    risk_response_options = ["Mitigate", "Transfer", "Avoid", "Accept"]

    if not controls_to_respond.empty:
        st.info("Sarah, for each control, specify its expected effectiveness (1=Ineffective, 5=Highly Effective) and the bank's chosen risk response (Mitigate, Transfer, Avoid, or Accept).")

        responded_controls_data = []
        with st.form("assign_responses_form"):
            for index, control in controls_to_respond.iterrows():
                control_id = int(control['control_id'])
                st.markdown(f"**Control ID: {control_id}**")
                st.write(f"Description: {control['control_description']}")

                effectiveness = st.slider(
                    f"Effectiveness Score (1-5) for Control ID {control_id}", 1, 5, 4, key=f"effectiveness_{control_id}")
                risk_response_index = 0  # Default to Mitigate
                if control['risk_response'] in risk_response_options:
                    risk_response_index = risk_response_options.index(
                        control['risk_response'])
                risk_response = st.selectbox(
                    f"Risk Response for Control ID {control_id}", risk_response_options, index=risk_response_index, key=f"response_{control_id}")

                responded_controls_data.append(
                    {'control_id': control_id, 'effectiveness': effectiveness, 'risk_response': risk_response})
                st.markdown("---")

            submitted_responses = st.form_submit_button("Assign All Responses")

            if submitted_responses:
                for response_data in responded_controls_data:
                    assign_risk_response_st(
                        response_data['control_id'], response_data['effectiveness'], response_data['risk_response'])
                st.session_state.current_step = 7
                st.rerun()
    else:
        st.success(
            "✅ All risk responses assigned! Proceed to Review Risk Register.")
        st.session_state.current_step = 7

    st.markdown("\n**Updated AI Controls Register with risk responses:**")
    st.dataframe(st.session_state.ai_controls_df)
