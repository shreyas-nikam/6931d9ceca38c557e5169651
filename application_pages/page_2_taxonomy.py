import streamlit as st

def main():
    st.subheader("2. Defining Our AI Risk Taxonomy")
    st.markdown("""
        To ensure a consistent and comprehensive identification of AI-specific risks, Sarah needs a standardized taxonomy. This taxonomy categorizes risks across different dimensions—Data, Model, System, Human, and Organizational—providing a structured framework for assessment. This aligns with the "Risk Taxonomy" concept in the AI RMF, ensuring that all potential vulnerabilities are considered.

        A well-defined taxonomy helps Sarah and her team systematically identify potential AI-specific hazards, such as data drift, adversarial attacks, algorithmic bias, or privacy breaches, ensuring comprehensive coverage and facilitating communication across different departments within QuantFinance Bank.
    """)
    st.json(st.session_state.AI_RISK_TAXONOMY)
    st.info("This taxonomy will serve as a checklist and classification system for Sarah and her team. By having predefined categories like 'Data Risk' and 'Model Risk' with specific types, Sarah ensures no critical area of AI risk is overlooked when assessing new models. This structured approach underpins the systematic identification required for effective risk management.")
    if st.button("Acknowledge Taxonomy & Proceed to Model Registration", key="next_step2_btn"):
        st.session_state.current_step = 3
        st.rerun()
