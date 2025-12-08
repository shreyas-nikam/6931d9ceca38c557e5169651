import streamlit as st
from utils import initialize_session_state, restart_workflow # Import the utility functions

# Set basic page configuration
st.set_page_config(page_title="QuLab", layout="wide")

# Initialize session state (important to call this first)
initialize_session_state()

# Sidebar for navigation and reset
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()

st.sidebar.markdown("### Navigation")

# Navigation options
page_options = {
    "Welcome & System Initialization": "page_1_welcome",
    "AI Risk Taxonomy Definition": "page_2_taxonomy",
    "Register a New AI Model": "page_3_register_model",
    "Initial Risk Identification": "page_4_identify_risks",
    "Quantifying Risk Assessment": "page_5_quantify_risks",
    "Calculate Composite Risk Score": "page_6_calculate_composite_score",
    "Adversarial Testing Insights": "page_7_adversarial_testing",
    "Supply Chain & Data Provenance Risks": "page_8_supply_chain_risks",
    "Define Controls & Mitigation": "page_9_define_controls",
    "Assign Risk Response Options": "page_10_assign_responses",
    "Review Comprehensive Register": "page_11_review_register",
    "Analyze & Prioritize Top Risks": "page_12_prioritize_risks",
    "Visualize Risk Distribution": "page_13_visualize_risks",
    "Simulate Data Drift": "page_14_data_drift",
    "Update Risk Assessment": "page_15_update_assessment",
    "Workflow Summary": "page_16_summary"
}

# Get current step from session_state to pre-select the page
current_step_name = list(page_options.keys())[st.session_state.current_step - 1]

selected_page_label = st.sidebar.selectbox(
    label="Go to Step:", 
    options=list(page_options.keys()), 
    index=list(page_options.keys()).index(current_step_name),
    key="navigation_selectbox"
)

# Handle page navigation
if st.session_state.navigation_selectbox != current_step_name:
    # If user manually selects a page from the sidebar, update current_step
    new_step_index = list(page_options.keys()).index(st.session_state.navigation_selectbox)
    st.session_state.current_step = new_step_index + 1
    st.rerun()

st.sidebar.divider()
if st.sidebar.button("Restart Workflow", key="sidebar_reset_btn"):
    restart_workflow()


# Main application content
st.header("QuantFinance AI Model Risk Manager: Sarah's Workflow")
st.markdown("""
    In this lab, you will step into the role of **Sarah, a Senior Risk Manager at QuantFinance Bank**. Your mission is to establish a robust framework for managing the unique risks introduced by AI models in the financial sector. The application will guide you through a realistic, story-driven workflow, mirroring the challenges and decisions faced in a dynamic AI environment.

    You will actively engage with the core principles of AI model risk management, from setting up a centralized risk register and defining a comprehensive risk taxonomy, to formally registering new AI models, identifying and quantifying risks, designing mitigation strategies, and adapting to real-time operational feedback.

    This interactive experience is designed to help you not just understand, but *apply* these concepts to real-world tasks, ensuring the trustworthiness, safety, and regulatory compliance of QuantFinance Bank's AI initiatives.
""")
st.divider()

# Dynamically import and run the selected page's main function
current_page_file = page_options[selected_page_label]
if current_page_file == "page_1_welcome":
    from application_pages.page_1_welcome import main
    main()
elif current_page_file == "page_2_taxonomy":
    from application_pages.page_2_taxonomy import main
    main()
elif current_page_file == "page_3_register_model":
    from application_pages.page_3_register_model import main
    main()
elif current_page_file == "page_4_identify_risks":
    from application_pages.page_4_identify_risks import main
    main()
elif current_page_file == "page_5_quantify_risks":
    from application_pages.page_5_quantify_risks import main
    main()
elif current_page_file == "page_6_calculate_composite_score":
    from application_pages.page_6_calculate_composite_score import main
    main()
elif current_page_file == "page_7_adversarial_testing":
    from application_pages.page_7_adversarial_testing import main
    main()
elif current_page_file == "page_8_supply_chain_risks":
    from application_pages.page_8_supply_chain_risks import main
    main()
elif current_page_file == "page_9_define_controls":
    from application_pages.page_9_define_controls import main
    main()
elif current_page_file == "page_10_assign_responses":
    from application_pages.page_10_assign_responses import main
    main()
elif current_page_file == "page_11_review_register":
    from application_pages.page_11_review_register import main
    main()
elif current_page_file == "page_12_prioritize_risks":
    from application_pages.page_12_prioritize_risks import main
    main()
elif current_page_file == "page_13_visualize_risks":
    from application_pages.page_13_visualize_risks import main
    main()
elif current_page_file == "page_14_data_drift":
    from application_pages.page_14_data_drift import main
    main()
elif current_page_file == "page_15_update_assessment":
    from application_pages.page_15_update_assessment import main
    main()
elif current_page_file == "page_16_summary":
    from application_pages.page_16_summary import main
    main()


# License
st.caption('''
---
## QuantUniversity License

© QuantUniversity 2025  
This notebook was created for **educational purposes only** and is **not intended for commercial use**.  

- You **may not copy, share, or redistribute** this notebook **without explicit permission** from QuantUniversity.  
- You **may not delete or modify this license cell** without authorization.  
- This notebook was generated using **QuCreate**, an AI-powered assistant.  
- Content generated by AI may contain **hallucinated or incorrect information**. Please **verify before using**.  

All rights reserved. For permissions or commercial licensing, contact: [info@qusandbox.com](mailto:info@qusandbox.com)
''')
