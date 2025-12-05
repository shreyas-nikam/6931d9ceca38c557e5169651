"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()

# Explain the overall business scenario and story here
st.markdown("""
In this lab, you will step into the shoes of **Sarah, a Senior Risk Manager at QuantFinance Bank**. Her mission is to establish a robust framework for managing the unique risks posed by Artificial Intelligence (AI) models in the financial sector. This application will guide Sarah through a practical, end-to-end workflow, mirroring real-world tasks in her job rather than just showcasing theoretical concepts.

**The Core Challenge:** QuantFinance Bank relies heavily on AI for critical operations like credit assessment and fraud detection. However, these powerful tools introduce novel risks such as algorithmic bias, adversarial attacks, and data drift. Without a systematic approach, these risks can lead to significant financial losses, reputational damage, and regulatory penalties. Sarah is tasked with building a proactive and adaptive system to identify, assess, and manage these AI-specific risks, aligning with industry best practices and regulatory frameworks.

**How this App Helps Sarah:** This interactive application serves as Sarah's workbench for AI risk management. Through a series of guided steps, she will:
- **Establish Foundations**: Initialize a central repository for AI models, risks, and controls.
- **Identify Risks**: Systematically use a structured taxonomy to identify various AI hazards.
- **Quantify & Prioritize**: Assign likelihood and magnitude scores to risks, calculating composite scores for effective prioritization.
- **Integrate Intelligence**: Incorporate insights from adversarial testing and supply chain analysis.
- **Mitigate & Respond**: Define controls and strategic responses for identified risks.
- **Monitor & Adapt**: Update risk assessments based on simulated operational alerts, demonstrating continuous validation.
- **Report Holistically**: Generate and interpret comprehensive risk registers and visualizations.

Each step in this workflow is designed to reflect Sarah's actual decision-making process, helping her apply crucial AI risk management concepts to real-world scenarios at QuantFinance Bank.
""")

# --- Initialize session state variables if not already present ---
if 'ai_models_df' not in st.session_state:
    st.session_state.ai_models_df = pd.DataFrame(columns=["model_id", "model_name", "use_case", "description", "owner", "status"])
    st.session_state.ai_risks_df = pd.DataFrame(columns=["risk_id", "model_id", "risk_type", "hazard_description", "likelihood_score", "magnitude_score", "composite_risk_score"])
    st.session_state.ai_controls_df = pd.DataFrame(columns=["control_id", "risk_id", "control_description", "effectiveness_score", "risk_response"])
    st.session_state.model_id_counter = 0
    st.session_state.risk_id_counter = 0
    st.session_state.control_id_counter = 0
    st.session_state.current_step = 1 # Start at step 1
    
if 'AI_RISK_TAXONOMY' not in st.session_state:
    st.session_state.AI_RISK_TAXONOMY = {
        "Data Risk": ["Data Quality", "Data Privacy", "Data Drift", "Data Poisoning", "Data Bias", "Data Provenance"],
        "Model Risk": ["Algorithmic Bias", "Fairness", "Explainability", "Robustness", "Performance Degradation", "Adversarial Attacks", "Concept Drift", "Model Interpretability"],
        "System Risk": ["Security Vulnerability", "Integration Issues", "Infrastructure Failure", "Access Control"],
        "Human Risk": ["Operator Error", "Misuse", "Lack of Oversight", "Ethical Misalignment"],
        "Organizational Risk": ["Regulatory Non-Compliance", "Reputational Damage", "Lack of Governance", "Third-Party Dependency"]
    }

# --- Utility functions adapted for Streamlit session state ---

def initialize_risk_management_system_st():
    st.session_state.ai_models_df = pd.DataFrame(columns=["model_id", "model_name", "use_case", "description", "owner", "status"])
    st.session_state.ai_risks_df = pd.DataFrame(columns=["risk_id", "model_id", "risk_type", "hazard_description", "likelihood_score", "magnitude_score", "composite_risk_score"])
    st.session_state.ai_controls_df = pd.DataFrame(columns=["control_id", "risk_id", "control_description", "effectiveness_score", "risk_response"])
    st.session_state.model_id_counter = 0
    st.session_state.risk_id_counter = 0
    st.session_state.control_id_counter = 0
    st.success("AI Model Risk Register system initialized successfully.")

def add_ai_model_st(model_name, use_case, description, owner, status="In Development"):
    st.session_state.model_id_counter += 1
    new_model = {
        "model_id": st.session_state.model_id_counter,
        "model_name": model_name,
        "use_case": use_case,
        "description": description,
        "owner": owner,
        "status": status
    }
    st.session_state.ai_models_df = pd.concat([st.session_state.ai_models_df, pd.DataFrame([new_model])], ignore_index=True)
    st.success(f"Model '{model_name}' (ID: {st.session_state.model_id_counter}) added successfully.")
    return st.session_state.model_id_counter # Return new model ID for linking risks

def add_ai_risk_st(model_id, risk_type, hazard_description, likelihood_score=None, magnitude_score=None):
    st.session_state.risk_id_counter += 1
    new_risk = {
        "risk_id": st.session_state.risk_id_counter,
        "model_id": model_id,
        "risk_type": risk_type,
        "hazard_description": hazard_description,
        "likelihood_score": likelihood_score,
        "magnitude_score": magnitude_score,
        "composite_risk_score": None
    }
    st.session_state.ai_risks_df = pd.concat([st.session_state.ai_risks_df, pd.DataFrame([new_risk])], ignore_index=True)
    st.info(f"Risk '{hazard_description}' (ID: {st.session_state.risk_id_counter}) added for model {model_id}.")
    return st.session_state.risk_id_counter

def assign_risk_scores_st(risk_id, likelihood, magnitude):
    if risk_id in st.session_state.ai_risks_df['risk_id'].values:
        st.session_state.ai_risks_df.loc[st.session_state.ai_risks_df['risk_id'] == risk_id, 'likelihood_score'] = likelihood
        st.session_state.ai_risks_df.loc[st.session_state.ai_risks_df['risk_id'] == risk_id, 'magnitude_score'] = magnitude
        st.info(f"Assigned likelihood ({likelihood}) and magnitude ({magnitude}) scores for risk ID {risk_id}.")
    else:
        st.warning(f"Risk ID {risk_id} not found.")

def calculate_composite_risk_score_st(risk_id):
    if risk_id in st.session_state.ai_risks_df['risk_id'].values:
        likelihood = st.session_state.ai_risks_df.loc[st.session_state.ai_risks_df['risk_id'] == risk_id, 'likelihood_score'].iloc[0]
        magnitude = st.session_state.ai_risks_df.loc[st.session_state.ai_risks_df['risk_id'] == risk_id, 'magnitude_score'].iloc[0]
        if pd.notna(likelihood) and pd.notna(magnitude):
            composite_score = likelihood * magnitude
            st.session_state.ai_risks_df.loc[st.session_state.ai_risks_df['risk_id'] == risk_id, 'composite_risk_score'] = composite_score
            st.success(f"Calculated composite risk score ({composite_score}) for risk ID {risk_id}.")
        else:
            st.warning(f"Likelihood or magnitude scores missing for risk ID {risk_id}. Cannot calculate composite score.")
    else:
        st.warning(f"Risk ID {risk_id} not found.")

def add_adversarial_risk_st(model_id, attack_type, description, likelihood, magnitude):
    risk_type = "Model Risk"
    new_risk_id = add_ai_risk_st(model_id, risk_type, f"{attack_type}: {description}")
    assign_risk_scores_st(new_risk_id, likelihood, magnitude)
    calculate_composite_risk_score_st(new_risk_id)
    st.success(f"Adversarial risk '{attack_type}' (ID: {new_risk_id}) added and scored for model {model_id}.")
    return new_risk_id

def add_supply_chain_risk_st(model_name, model_use_case, model_description, model_owner, model_status, risk_type, hazard_description, likelihood, magnitude):
    existing_model = st.session_state.ai_models_df[st.session_state.ai_models_df['model_name'] == model_name]
    if not existing_model.empty:
        model_id = existing_model['model_id'].iloc[0]
        st.info(f"Model '{model_name}' (ID: {model_id}) already exists. Using existing model_id.")
    else:
        model_id = add_ai_model_st(model_name, model_use_case, model_description, model_owner, model_status)

    new_risk_id = add_ai_risk_st(model_id, risk_type, hazard_description)
    assign_risk_scores_st(new_risk_id, likelihood, magnitude)
    calculate_composite_risk_score_st(new_risk_id)
    st.success(f"Supply chain/data provenance risk '{hazard_description}' (ID: {new_risk_id}) added and scored for model {model_id}.")
    return model_id, new_risk_id

def add_ai_control_st(risk_id, control_description):
    st.session_state.control_id_counter += 1
    new_control = {
        "control_id": st.session_state.control_id_counter,
        "risk_id": risk_id,
        "control_description": control_description,
        "effectiveness_score": None,
        "risk_response": None
    }
    st.session_state.ai_controls_df = pd.concat([st.session_state.ai_controls_df, pd.DataFrame([new_control])], ignore_index=True)
    st.success(f"Control '{control_description}' (ID: {st.session_state.control_id_counter}) added for risk ID {risk_id}.")
    return st.session_state.control_id_counter

def assign_risk_response_st(control_id, effectiveness_score, risk_response):
    if control_id in st.session_state.ai_controls_df['control_id'].values:
        st.session_state.ai_controls_df.loc[st.session_state.ai_controls_df['control_id'] == control_id, 'effectiveness_score'] = effectiveness_score
        st.session_state.ai_controls_df.loc[st.session_state.ai_controls_df['control_id'] == control_id, 'risk_response'] = risk_response
        st.info(f"Assigned effectiveness score ({effectiveness_score}) and risk response ('{risk_response}') for control ID {control_id}.")
    else:
        st.warning(f"Control ID {control_id} not found.")

def get_full_risk_register_st():
    merged_df = pd.merge(st.session_state.ai_models_df, st.session_state.ai_risks_df, on='model_id', how='left')
    full_register_df = pd.merge(merged_df, st.session_state.ai_controls_df, on='risk_id', how='left')
    selected_columns = [
        'model_name', 'use_case', 'description_x', 'owner', 'status',
        'risk_type', 'hazard_description', 'likelihood_score', 'magnitude_score', 'composite_risk_score',
        'control_description', 'effectiveness_score', 'risk_response'
    ]
    full_register_df = full_register_df[selected_columns]
    full_register_df = full_register_df.rename(columns={'description_x': 'model_description'})
    st.session_state.full_risk_register_df = full_register_df
    st.success("Comprehensive AI Model Risk Register generated.")

def identify_top_risks_st(num_top_risks=5):
    if not st.session_state.full_risk_register_df.empty:
        df_sorted = st.session_state.full_risk_register_df.sort_values(by='composite_risk_score', ascending=False, na_position='last')
        top_risks = df_sorted.head(num_top_risks)
        st.session_state.top_risks_df = top_risks
        st.success(f"Top {num_top_risks} risks identified.")
    else:
        st.warning("Full risk register is empty. Cannot identify top risks.")

def plot_risk_distribution_by_type_st():
    if not st.session_state.ai_risks_df.empty:
        category_map = {}
        for category, types in st.session_state.AI_RISK_TAXONOMY.items():
            for t in types:
                category_map[t] = category
        
        if 'risk_type' in st.session_state.ai_risks_df.columns:
            # Ensure the 'broad_risk_category' is mapped correctly, handling potential NaNs if risk_type is not in taxonomy
            st.session_state.ai_risks_df['broad_risk_category'] = st.session_state.ai_risks_df['risk_type'].map(category_map)
            # Filter out NaNs if some risk_types don't map to a category
            risk_counts = st.session_state.ai_risks_df.dropna(subset=['broad_risk_category'])['broad_risk_category'].value_counts().reset_index()
            risk_counts.columns = ['Broad Risk Category', 'Number of Risks']

            if not risk_counts.empty:
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.barplot(x='Broad Risk Category', y='Number of Risks', data=risk_counts, palette='viridis', ax=ax)
                ax.set_title('Distribution of AI Risks by Broad Category')
                ax.set_xlabel('Broad Risk Category')
                ax.set_ylabel('Number of Risks')
                plt.xticks(rotation=45, ha='right')
                plt.tight_layout()
                st.pyplot(fig)
                plt.close(fig)
                st.caption("This visualization provides Sarah with a high-level understanding of where QuantFinance Bank's AI risks are concentrated.")
            else:
                st.warning("No broad risk categories found to plot distribution after mapping.")
        else:
            st.warning("No 'risk_type' column found in AI risks data to plot distribution.")
    else:
        st.warning("No risks identified yet to plot distribution.")

def simulate_data_drift_alert_st(model_id, risk_type_to_update, hazard_description_if_new, new_likelihood, new_magnitude):
    existing_risk_row = st.session_state.ai_risks_df[(st.session_state.ai_risks_df['model_id'] == model_id) & (st.session_state.ai_risks_df['risk_type'] == risk_type_to_update)]

    if not existing_risk_row.empty:
        risk_id = existing_risk_row['risk_id'].iloc[0]
        st.info(f"Updating existing risk ID {risk_id} for '{risk_type_to_update}' (model ID: {model_id}).")
        assign_risk_scores_st(risk_id, new_likelihood, new_magnitude)
        calculate_composite_risk_score_st(risk_id)
    else:
        st.info(f"Adding new risk '{risk_type_to_update}' for model ID: {model_id}.")
        risk_id = add_ai_risk_st(model_id, risk_type_to_update, hazard_description_if_new, new_likelihood, new_magnitude)
        calculate_composite_risk_score_st(risk_id)
    st.warning("Data drift alert processed and risk assessment updated to reflect the new operational reality.")
    return risk_id

def update_risk_assessment_from_monitoring_st(model_id, target_risk_type, updated_likelihood, updated_magnitude):
    target_risk_row = st.session_state.ai_risks_df[(st.session_state.ai_risks_df['model_id'] == model_id) & (st.session_state.ai_risks_df['risk_type'] == target_risk_type)]

    if not target_risk_row.empty:
        risk_id = target_risk_row['risk_id'].iloc[0]
        st.info(f"Updating risk assessment for risk ID {risk_id} ('{target_risk_type}') for model ID {model_id}.")
        assign_risk_scores_st(risk_id, updated_likelihood, updated_magnitude)
        calculate_composite_risk_score_st(risk_id)
    else:
        st.warning(f"Risk type '{target_risk_type}' not found for model ID {model_id}. No update performed.")
    st.success("Risk assessment formally updated based on monitoring feedback.")

# Main application logic
st.title("QuantFinance AI Model Risk Manager: Sarah's Workflow")

# --- Step-by-step narrative and UI ---

# Step 1: Welcome & System Initialization
if st.session_state.current_step == 1:
    st.subheader("1. Setting the Stage: Initializing QuantFinance Bank's AI Risk Management System")
    st.markdown("""
        Sarah's first step is to lay the groundwork for a robust AI risk management system. This involves setting up the core data structures that will store information about AI models, identified risks, and their associated controls. This centralized repository is crucial for maintaining a transparent and comprehensive overview of all AI-related risks across QuantFinance Bank, aligning with the "Centralized Repository" concept from the AI RMF.

        This foundational setup enables a systematic record of identified AI hazards and risks, which is essential for proactive risk management and effective communication among stakeholders.
    """)
    if st.button("Initialize AI Risk Management System", key="init_system_btn"):
        initialize_risk_management_system_st()
        st.session_state.current_step = 2
        st.rerun()
    st.markdown("""
        Below are the empty dataframes that will hold our AI models, risks, and controls as Sarah progresses through the workflow.
    """)
    st.dataframe(st.session_state.ai_models_df, use_container_width=True)
    st.dataframe(st.session_state.ai_risks_df, use_container_width=True)
    st.dataframe(st.session_state.ai_controls_df, use_container_width=True)

# Step 2: AI Risk Taxonomy Definition
elif st.session_state.current_step == 2:
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

# Step 3: Register a New AI Model
elif st.session_state.current_step == 3:
    st.subheader("3. Registering a New AI Model: The Credit Score Predictor")
    st.markdown("""
        QuantFinance Bank is preparing to deploy a new AI-powered "Credit Score Predictor" model, which is critical for loan approvals. Sarah's immediate task is to formally register this model in the system, capturing its essential details, intended use, and initial status. This initial registration is a fundamental step in the AI RMF process, ensuring that every AI model under the bank's purview is documented from its inception.

        By registering the model early, Sarah ensures that all subsequent risk assessments and control implementations are tied to a specific, well-defined AI asset, providing clear accountability and traceability.
    """)

    with st.form("add_model_form"):
        model_name = st.text_input("Model Name", "Credit Score Predictor", key="model_name_3")
        use_case = st.text_area("Use Case", "Automating credit risk assessment for loan applications", key="use_case_3")
        description = st.text_area("Description", "Machine learning model predicting creditworthiness based on financial history and demographic data.", key="description_3")
        owner = st.text_input("Owner", "Retail Banking Analytics", key="owner_3")
        status = st.selectbox("Status", ["In Development", "In Production", "Retired"], index=0, key="status_3")
        submitted = st.form_submit_button("Register AI Model")

        if submitted:
            # Check if model already exists before adding
            if model_name not in st.session_state.ai_models_df['model_name'].values:
                new_model_id = add_ai_model_st(model_name, use_case, description, owner, status) 
                st.session_state.credit_score_predictor_model_id = new_model_id # Store the ID for future steps
            else:
                st.warning(f"Model '{model_name}' already registered. Using existing model ID.")
                st.session_state.credit_score_predictor_model_id = st.session_state.ai_models_df[st.session_state.ai_models_df['model_name'] == model_name]['model_id'].iloc[0]
            st.session_state.current_step = 4
            st.rerun()
    
    if not st.session_state.ai_models_df.empty:
        st.markdown("\nUpdated AI Models DataFrame:")
        st.dataframe(st.session_state.ai_models_df, use_container_width=True)

# Step 4: Initial Risk Identification
elif st.session_state.current_step == 4:
    st.subheader("4. Initial Risk Identification: Potential Hazards for the Credit Score Model")
    st.markdown("""
        With the Credit Score Predictor registered, Sarah begins the crucial process of identifying potential AI-specific hazards. She draws upon her expertise and the bank's risk taxonomy to foresee issues that could arise from data quality, model behavior, or operational deployment. This proactive identification is key to mitigating future problems and aligns with Section 4.2 of the AI RMF, focusing on "Risk Register: Identification and Categorization."

        Sarah considers risks like "Data Quality" (poor input data leading to incorrect scores), "Algorithmic Bias" (unfair scoring for certain demographic groups), and "Performance Degradation" (the model's accuracy declining over time). This step is crucial for anticipating challenges and preventing negative impacts on customers and the bank's reputation.
    """)

    credit_score_predictor_model_id = st.session_state.ai_models_df[st.session_state.ai_models_df['model_name'] == 'Credit Score Predictor']['model_id'].iloc[0] if 'Credit Score Predictor' in st.session_state.ai_models_df['model_name'].values else None

    if credit_score_predictor_model_id:
        st.write(f"Adding risks for model: **Credit Score Predictor** (ID: {credit_score_predictor_model_id})")
        
        # Check and add risks only if they don't already exist for this model
        risk_exists_dq = ((st.session_state.ai_risks_df['model_id'] == credit_score_predictor_model_id) & (st.session_state.ai_risks_df['risk_type'] == "Data Quality")).any()
        risk_exists_ab = ((st.session_state.ai_risks_df['model_id'] == credit_score_predictor_model_id) & (st.session_state.ai_risks_df['risk_type'] == "Algorithmic Bias")).any()
        risk_exists_pd = ((st.session_state.ai_risks_df['model_id'] == credit_score_predictor_model_id) & (st.session_state.ai_risks_df['risk_type'] == "Performance Degradation")).any()

        if st.button("Add Data Quality Risk", key="add_dq_risk", disabled=risk_exists_dq):
            add_ai_risk_st(credit_score_predictor_model_id, "Data Quality", "Poor or incomplete historical data leading to inaccurate credit scores.")
            st.rerun()
        if st.button("Add Algorithmic Bias Risk", key="add_ab_risk", disabled=risk_exists_ab):
            add_ai_risk_st(credit_score_predictor_model_id, "Algorithmic Bias", "Model exhibits biased decision-making against certain demographic groups.")
            st.rerun()
        if st.button("Add Performance Degradation Risk", key="add_pd_risk", disabled=risk_exists_pd):
            add_ai_risk_st(credit_score_predictor_model_id, "Performance Degradation", "Model accuracy degrades over time due to changes in credit behavior patterns.")
            st.rerun()
        
        st.markdown("\nIdentified Risks for Credit Score Predictor:")
        st.dataframe(st.session_state.ai_risks_df[st.session_state.ai_risks_df['model_id'] == credit_score_predictor_model_id], use_container_width=True)

        if risk_exists_dq and risk_exists_ab and risk_exists_pd and st.button("Proceed to Quantify Risks", key="next_step4_btn"):
            st.session_state.current_step = 5
            st.rerun()
        elif not (risk_exists_dq and risk_exists_ab and risk_exists_pd):
            st.info("Please add all three risks (Data Quality, Algorithmic Bias, Performance Degradation) to proceed.")
    else:
        st.error("Credit Score Predictor model not found. Please go back to Step 3 to register it.")
        if st.button("Go to Step 3", key="go_to_step3_from4"):
            st.session_state.current_step = 3
            st.rerun()

# Step 5: Quantifying Risk: Likelihood and Magnitude Assessment
elif st.session_state.current_step == 5:
    st.subheader("5. Quantifying Risk: Likelihood and Magnitude Assessment")
    st.markdown(r"""
        Identifying risks is only the first step; Sarah now needs to quantify them to understand their potential impact. For each identified risk, she will assess its likelihood of occurrence ($P(\text{event})$) and the magnitude of potential harm ($M(\text{consequence})$). This quantitative and qualitative assessment is fundamental to the AI RMF (Section 4.2), as it allows for a standardized way to prioritize risks across the bank's AI portfolio.

        The core formula for this assessment is:
        $$ \text{Risk} = P(\text{event}) \times M(\text{consequence}) $$
        where $P(\text{event})$ represents the likelihood of a risk event occurring, and $M(\text{consequence})$ represents the severity of the impact if the event occurs. These scores will typically be qualitative (e.g., Low, Medium, High) mapped to numerical scales (e.g., 1-5).
    """)

    risks_to_score = st.session_state.ai_risks_df[
        (st.session_state.ai_risks_df['likelihood_score'].isna()) | 
        (st.session_state.ai_risks_df['magnitude_score'].isna())
    ].copy()

    if not risks_to_score.empty:
        st.info("Sarah, use the sliders below to assign likelihood and magnitude scores for each risk. These scores are crucial for calculating the overall risk severity.")
        scored_risks_data = []
        with st.form("assign_scores_form"):
            for index, risk in risks_to_score.iterrows():
                st.markdown(f"**Risk ID: {int(risk['risk_id'])}**")
                st.write(f"Type: {risk['risk_type']}")
                st.write(f"Hazard: {risk['hazard_description']}")
                
                likelihood = st.slider(f"Likelihood (1-5) for Risk ID {int(risk['risk_id'])}: How frequently is this risk likely to occur?", 1, 5, 3, key=f"likelihood_{int(risk['risk_id'])}")
                magnitude = st.slider(f"Magnitude (1-5) for Risk ID {int(risk['risk_id'])}: How severe would the impact be if this risk materializes?", 1, 5, 3, key=f"magnitude_{int(risk['risk_id'])}")
                scored_risks_data.append({'risk_id': int(risk['risk_id']), 'likelihood': likelihood, 'magnitude': magnitude})
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

    st.markdown("\nUpdated AI Risks DataFrame with scores:")
    st.dataframe(st.session_state.ai_risks_df, use_container_width=True)

# Step 6: Calculating the Composite Risk Score
elif st.session_state.current_step == 6:
    st.subheader("6. Calculating the Composite Risk Score")
    st.markdown(r"""
        With likelihood and magnitude scores assigned, Sarah can now calculate the composite risk score for each hazard. This score, derived from the formula $Risk = P(\text{event}) \times M(\text{consequence})$, provides a single, aggregated metric for each risk, allowing for easy comparison and prioritization. This calculation is a direct application of the "Quantitative and Qualitative Assessment" mentioned in the AI RMF (Section 4.2).

        By standardizing risk quantification, Sarah ensures that all stakeholders at QuantFinance Bank can understand and compare the severity of different AI risks, guiding resource allocation for risk mitigation. A higher composite score indicates greater urgency for mitigation, helping Sarah prioritize her efforts effectively.
    """)

    uncalculated_risks = st.session_state.ai_risks_df[
        st.session_state.ai_risks_df['composite_risk_score'].isna() &
        st.session_state.ai_risks_df['likelihood_score'].notna() &
        st.session_state.ai_risks_df['magnitude_score'].notna()
    ]

    if not uncalculated_risks.empty:
        st.info(f"Sarah, {len(uncalculated_risks)} risks are ready for composite score calculation.")
        if st.button("Calculate All Composite Risk Scores", key="calculate_composite_btn"):
            for risk_id in uncalculated_risks['risk_id']:
                calculate_composite_risk_score_st(int(risk_id))
            st.session_state.current_step = 7
            st.rerun()
    else:
        st.info("All risks with assigned likelihood and magnitude scores already have composite scores. Proceed to integrating external insights.")
        if st.button("Proceed to Integrating Adversarial Insights", key="next_step6_btn"):
            st.session_state.current_step = 7
            st.rerun()

    st.markdown("\nUpdated AI Risks DataFrame with composite scores:")
    st.dataframe(st.session_state.ai_risks_df, use_container_width=True)

# Step 7: Integrating Insights from Adversarial Testing
elif st.session_state.current_step == 7:
    st.subheader("7. Integrating Insights from Adversarial Testing: Uncovering Robustness Risks")
    st.markdown("""
        QuantFinance Bank's dedicated Red-Teaming unit has just concluded an exercise targeting the Credit Score Predictor. Their findings reveal vulnerabilities to "Adversarial Attacks" – subtle manipulations of input data that can cause misclassification (e.g., making a high-risk applicant appear low-risk). Sarah must immediately integrate these critical insights into the risk register. This directly reflects the importance of "Adversarial Testing and Red-Teaming" (Section 2) in the AI RMF for uncovering AI-specific security vulnerabilities like "Deceptive Inputs" (2.2) and "Data Poisoning Attacks" (2.4).

        By documenting these specific threats, Sarah ensures the bank can develop targeted defenses, preventing malicious actors from exploiting the model and protecting the integrity of loan decisions.
    """)

    credit_score_predictor_model_id = st.session_state.ai_models_df[st.session_state.ai_models_df['model_name'] == 'Credit Score Predictor']['model_id'].iloc[0] if 'Credit Score Predictor' in st.session_state.ai_models_df['model_name'].values else None

    if credit_score_predictor_model_id:
        st.write(f"Adding adversarial risk for model: **Credit Score Predictor** (ID: {credit_score_predictor_model_id})")
        
        # Check if adversarial risk already added
        adversarial_risk_already_added = ((st.session_state.ai_risks_df['model_id'] == credit_score_predictor_model_id) & 
                                          (st.session_state.ai_risks_df['hazard_description'].str.contains('Adversarial Attack', na=False))).any()

        with st.form("add_adversarial_risk_form"):
            attack_type = st.text_input("Adversarial Attack Type", "Adversarial Attack (Evasion)", key="attack_type_7", disabled=adversarial_risk_already_added)
            description = st.text_area("Description", "Subtle manipulation of input features to cause a misclassification of a high-risk individual as low-risk.", key="description_7", disabled=adversarial_risk_already_added)
            likelihood = st.slider("Likelihood (1-5)", 1, 5, 4, key="adv_likelihood_7", disabled=adversarial_risk_already_added)
            magnitude = st.slider("Magnitude (1-5)", 1, 5, 5, key="adv_magnitude_7", disabled=adversarial_risk_already_added)
            submitted = st.form_submit_button("Add Adversarial Risk & Score", disabled=adversarial_risk_already_added)

            if submitted:
                add_adversarial_risk_st(credit_score_predictor_model_id, attack_type, description, likelihood, magnitude)
                st.session_state.current_step = 8
                st.rerun()
            elif adversarial_risk_already_added:
                st.info("Adversarial attack risk has already been added for this model.")
    else:
        st.error("Credit Score Predictor model not found. Please ensure it's registered in Step 3.")
        if st.button("Go to Step 3", key="go_to_step3_from7"):
            st.session_state.current_step = 3
            st.rerun()
    
    st.markdown("\nUpdated AI Risks DataFrame with adversarial attack risk:")
    st.dataframe(st.session_state.ai_risks_df, use_container_width=True)
    
    if st.button("Proceed to Addressing Supply Chain Risks", key="next_step7_btn"):
        st.session_state.current_step = 8
        st.rerun()

# Step 8: Addressing Supply Chain and Data Provenance Risks
elif st.session_state.current_step == 8:
    st.subheader("8. Addressing Supply Chain and Data Provenance Risks")
    st.markdown("""
        Beyond direct model vulnerabilities, Sarah also considers the broader "AI Supply Chain" (Section 3). A recent internal review highlighted potential data provenance issues for a separate "Fraud Detection System" and its reliance on a critical third-party feature engineering library. Sarah needs to register these "Data Provenance" (3.2) and "Third-Party Dependency" (3.3) risks. This is critical for understanding risks related to data quality, integrity, and external components, concepts that are central to maintaining the trustworthiness of AI systems.

        Ensuring the quality and origin of data, as well as vetting third-party components, helps Sarah manage cascading vulnerabilities and maintain the overall security of QuantFinance Bank's AI portfolio.
    """)

    fraud_detection_model_name = "Fraud Detection System"
    fraud_model_id = None
    existing_fraud_model = st.session_state.ai_models_df[st.session_state.ai_models_df['model_name'] == fraud_detection_model_name]

    if existing_fraud_model.empty:
        st.info(f"Model '{fraud_detection_model_name}' not found. Registering it first.")
        fraud_model_id = add_ai_model_st(
            model_name=fraud_detection_model_name,
            use_case="Detecting fraudulent financial transactions in real-time",
            description="Supervised learning model trained on historical transaction data to flag suspicious activities.",
            owner="Fraud Prevention Unit",
            status="In Production"
        )
        st.session_state.fraud_detection_model_id = fraud_model_id # Store for future reference
        st.rerun() # Rerun to show new model and enable risk forms
    else:
        fraud_model_id = existing_fraud_model['model_id'].iloc[0]
        st.session_state.fraud_detection_model_id = fraud_model_id
        st.info(f"Model '{fraud_detection_model_name}' (ID: {fraud_model_id}) already exists. Using existing model_id.")

    if fraud_model_id:
        st.markdown("### Add Data Provenance Risk for Fraud Detection System")
        data_provenance_risk_exists = ((st.session_state.ai_risks_df['model_id'] == fraud_model_id) & (st.session_state.ai_risks_df['risk_type'] == "Data Provenance")).any()
        with st.form("add_data_provenance_risk_form"):
            dp_hazard_description = st.text_area("Hazard Description (Data Provenance)", "Lack of verifiable data provenance for historical transaction data used in training, raising concerns about data integrity and potential hidden biases.", key="dp_desc_8", disabled=data_provenance_risk_exists)
            dp_likelihood = st.slider("Likelihood (1-5)", 1, 5, 3, key="dp_likelihood_8", disabled=data_provenance_risk_exists)
            dp_magnitude = st.slider("Magnitude (1-5)", 1, 5, 4, key="dp_magnitude_8", disabled=data_provenance_risk_exists)
            dp_submitted = st.form_submit_button("Add Data Provenance Risk", disabled=data_provenance_risk_exists)

            if dp_submitted:
                add_supply_chain_risk_st(
                    model_name=fraud_detection_model_name, model_use_case="", model_description="", model_owner="", model_status="",
                    risk_type="Data Provenance", hazard_description=dp_hazard_description, likelihood=dp_likelihood, magnitude=dp_magnitude
                )
                st.rerun()
            elif data_provenance_risk_exists:
                st.info("Data Provenance risk has already been added.")
        
        st.markdown("### Add Third-Party Dependency Risk for Fraud Detection System")
        third_party_risk_exists = ((st.session_state.ai_risks_df['model_id'] == fraud_model_id) & (st.session_state.ai_risks_df['risk_type'] == "Organizational Risk") & (st.session_state.ai_risks_df['hazard_description'].str.contains('Third-Party Dependency', na=False))).any()
        with st.form("add_third_party_risk_form"):
            tpd_hazard_description = st.text_area("Hazard Description (Third-Party Dependency)", "Reliance on a third-party feature engineering library with unknown vulnerabilities or insufficient documentation.", key="tpd_desc_8", disabled=third_party_risk_exists)
            tpd_likelihood = st.slider("Likelihood (1-5)", 1, 5, 3, key="tpd_likelihood_8", disabled=third_party_risk_exists)
            tpd_magnitude = st.slider("Magnitude (1-5)", 1, 5, 3, key="tpd_magnitude_8", disabled=third_party_risk_exists)
            tpd_submitted = st.form_submit_button("Add Third-Party Dependency Risk", disabled=third_party_risk_exists)

            if tpd_submitted:
                add_supply_chain_risk_st(
                    model_name=fraud_detection_model_name, model_use_case="", model_description="", model_owner="", model_status="",
                    risk_type="Organizational Risk", hazard_description=tpd_hazard_description, likelihood=tpd_likelihood, magnitude=tpd_magnitude
                )
                st.rerun()
            elif third_party_risk_exists:
                st.info("Third-Party Dependency risk has already been added.")

        # Only proceed when both risks are added
        if data_provenance_risk_exists and third_party_risk_exists and st.button("Proceed to Define Controls", key="next_step8_btn"):
            st.session_state.current_step = 9
            st.rerun()
        elif not (data_provenance_risk_exists and third_party_risk_exists):
            st.info("Please add both Data Provenance and Third-Party Dependency risks to proceed.")

    st.markdown("\nUpdated AI Models DataFrame:")
    st.dataframe(st.session_state.ai_models_df, use_container_width=True)
    st.markdown("\nUpdated AI Risks DataFrame:")
    st.dataframe(st.session_state.ai_risks_df, use_container_width=True)


# Step 9: Defining Controls and Mitigation Strategies
elif st.session_state.current_step == 9:
    st.subheader("9. Defining Controls and Mitigation Strategies")
    st.markdown("""
        Having identified and quantified several risks, Sarah's next crucial step is to define and propose specific controls to mitigate them. This involves designing defenses tailored to each identified risk, from technical measures like input sanitization to procedural controls like regular model retraining. This directly applies the "Risk Controls and Mitigation Strategies" concept from the AI RMF (Section 4.3), emphasizing "Mapping Controls to Risks" and "Hierarchical Control Design."

        By establishing clear controls, Sarah ensures that QuantFinance Bank has concrete plans to reduce the likelihood or impact of identified risks, thereby strengthening the overall resilience of its AI systems against threats like adversarial attacks and data quality issues.
    """)

    # Identify risk IDs from notebook for specific controls
    algorithmic_bias_risk_id = st.session_state.ai_risks_df[st.session_state.ai_risks_df['hazard_description'].str.contains('Algorithmic Bias', na=False)]['risk_id'].iloc[0] if not st.session_state.ai_risks_df[st.session_state.ai_risks_df['hazard_description'].str.contains('Algorithmic Bias', na=False)].empty else None
    adversarial_attack_risk_id = st.session_state.ai_risks_df[st.session_state.ai_risks_df['hazard_description'].str.contains('Adversarial Attack', na=False)]['risk_id'].iloc[0] if not st.session_state.ai_risks_df[st.session_state.ai_risks_df['hazard_description'].str.contains('Adversarial Attack', na=False)].empty else None
    data_provenance_risk_id = st.session_state.ai_risks_df[st.session_state.ai_risks_df['hazard_description'].str.contains('Data Provenance', na=False)]['risk_id'].iloc[0] if not st.session_state.ai_risks_df[st.session_state.ai_risks_df['hazard_description'].str.contains('Data Provenance', na=False)].empty else None

    controls_to_add = [
        (algorithmic_bias_risk_id, "Implement fairness metrics monitoring (e.g., Equal Opportunity, Demographic Parity) and regular bias audits.", "Algorithmic Bias"),
        (adversarial_attack_risk_id, "Implement adversarial training techniques and robust input validation/sanitization mechanisms.", "Adversarial Attack"),
        (data_provenance_risk_id, "Establish clear data lineage tracking and cryptographic hashing for all training datasets.", "Data Provenance")
    ]

    all_controls_added = True
    for risk_id, control_desc, risk_name in controls_to_add:
        if risk_id is not None:
            control_exists = (st.session_state.ai_controls_df['risk_id'] == risk_id).any()
            if st.button(f"Add Control for {risk_name} (Risk ID: {int(risk_id)})", key=f"add_control_for_{risk_id}", disabled=control_exists):
                add_ai_control_st(risk_id, control_desc)
                st.rerun()
            elif control_exists:
                st.info(f"Control for {risk_name} (Risk ID: {int(risk_id)}) already added.")
            else:
                all_controls_added = False # Risk exists but control not added
        else:
            st.warning(f"Risk '{risk_name}' not found. Please ensure it was added in previous steps.")
            all_controls_added = False # Missing risk, so not all controls can be added
    
    st.markdown("\nUpdated AI Controls DataFrame:")
    st.dataframe(st.session_state.ai_controls_df, use_container_width=True)

    if all_controls_added and st.button("Proceed to Assign Risk Response Options", key="next_step9_btn"):
        st.session_state.current_step = 10
        st.rerun()
    elif not all_controls_added:
        st.info("Please add all specified controls to proceed to the next step.")


# Step 10: Assigning Risk Response Options
elif st.session_state.current_step == 10:
    st.subheader("10. Assigning Risk Response Options")
    st.markdown("""
        For each identified risk with its proposed controls, Sarah must now formalize the bank's "Risk Response Option" (Section 4.3). This involves deciding whether to mitigate, transfer, avoid, or accept the risk based on the severity of the residual risk (after controls) and the bank's overall risk tolerance. This strategic decision-making is a core part of the AI RMF, ensuring that every risk has a clear management plan.

        This step helps Sarah communicate to stakeholders exactly how each AI risk will be handled, ensuring alignment with the bank's broader risk appetite and regulatory requirements.
    """)

    controls_to_respond = st.session_state.ai_controls_df[
        (st.session_state.ai_controls_df['effectiveness_score'].isna()) | 
        (st.session_state.ai_controls_df['risk_response'].isna())
    ].copy()

    if not controls_to_respond.empty:
        st.info("Sarah, for each control, specify its expected effectiveness (how well it reduces risk) and the bank's chosen risk response strategy.")
        responded_controls_data = []
        
        with st.form("assign_responses_form"):
            for index, control in controls_to_respond.iterrows():
                st.markdown(f"**Control ID: {int(control['control_id'])}**")
                st.write(f"Description: {control['control_description']}")
                
                effectiveness = st.slider(f"Effectiveness Score (1-5) for Control ID {int(control['control_id'])}: How effective is this control at reducing the risk?", 1, 5, 4, key=f"effectiveness_{int(control['control_id'])}")
                risk_response = st.selectbox(f"Risk Response for Control ID {int(control['control_id'])}: What is the bank's strategy for this risk?", ["Mitigate", "Transfer", "Avoid", "Accept"], key=f"response_{int(control['control_id'])}")
                responded_controls_data.append({'control_id': int(control['control_id']), 'effectiveness': effectiveness, 'risk_response': risk_response})
                st.markdown("---")
            
            submitted_responses = st.form_submit_button("Assign All Responses")

            if submitted_responses:
                for response_data in responded_controls_data:
                    assign_risk_response_st(response_data['control_id'], response_data['effectiveness'], response_data['risk_response'])
                st.session_state.current_step = 11
                st.rerun()
    else:
        st.info("All controls have assigned risk response options.")
        if st.button("Proceed to Review Risk Register", key="next_step10_btn"):
            st.session_state.current_step = 11
            st.rerun()
            
    st.markdown("\nUpdated AI Controls DataFrame with risk responses:")
    st.dataframe(st.session_state.ai_controls_df, use_container_width=True)

# Step 11: Reviewing the Comprehensive AI Model Risk Register
elif st.session_state.current_step == 11:
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
        st.markdown("\nComprehensive AI Model Risk Register:")
        st.dataframe(st.session_state.full_risk_register_df, use_container_width=True)
        if st.button("Proceed to Analyze Top Risks", key="next_step11_btn_after_gen"):
            st.session_state.current_step = 12
            st.rerun()
    else:
        st.info("Click the button above to generate the full risk register.")

# Step 12: Analyzing and Prioritizing High-Scoring Risks
elif st.session_state.current_step == 12:
    st.subheader("12. Analyzing and Prioritizing High-Scoring Risks")
    st.markdown("""
        With a growing number of AI models and associated risks, Sarah needs an efficient way to identify and prioritize the most critical threats. Analyzing risks by their `composite_risk_score` allows her to pinpoint the highest-scoring hazards, ensuring that resources and attention are directed where they are most needed. This aligns with the AI RMF's principle of "Risk-based" decision-making.

        This analysis helps Sarah focus on the "top risks" that pose the greatest potential harm to QuantFinance Bank, enabling proactive resource allocation and strategic risk mitigation.
    """)
    
    if 'full_risk_register_df' in st.session_state and not st.session_state.full_risk_register_df.empty:
        num_top_risks = st.number_input("Number of Top Risks to Display", min_value=1, value=3, step=1, key="num_top_risks_12")
        if st.button("Identify Top Risks", key="identify_top_risks_btn"):
            identify_top_risks_st(num_top_risks)
            st.session_state.current_step = 13
            st.rerun()

        if 'top_risks_df' in st.session_state and not st.session_state.top_risks_df.empty:
            st.markdown(f"\nTop {num_top_risks} AI Risks by Composite Score (highest first):")
            st.dataframe(st.session_state.top_risks_df, use_container_width=True)
            if st.button("Proceed to Visualize Risk Distribution", key="next_step12_btn_after_id"):
                st.session_state.current_step = 13
                st.rerun()
        else:
            st.info("Click 'Identify Top Risks' to see the prioritized list.")
    else:
        st.warning("Please generate the comprehensive risk register in Step 11 first.")
        if st.button("Go to Step 11", key="go_to_step11_from12"):
            st.session_state.current_step = 11
            st.rerun()

# Step 13: Visualizing Risk Distribution by Type
elif st.session_state.current_step == 13:
    st.subheader("13. Visualizing Risk Distribution by Type")
    st.markdown("""
        To provide an executive overview of the bank's overall AI risk posture, Sarah wants to visualize how identified risks are distributed across the different categories defined in the AI Risk Taxonomy (e.g., Data, Model, System). This aggregation helps in understanding systemic weaknesses and informs strategic investments in risk management capabilities. This type of visualization supports the "MEASURE" function of the AI RMF and provides an aggregated view of risks.

        By visualizing the distribution, Sarah can identify if a particular risk category (e.g., "Model Risk") is disproportionately high, indicating a need for more robust controls or new policies in that area.
    """)

    if st.button("Generate Risk Distribution Chart", key="plot_risk_dist_btn"):
        plot_risk_distribution_by_type_st()
        st.session_state.current_step = 14
        st.rerun()
    elif not st.session_state.ai_risks_df.empty and 'broad_risk_category' in st.session_state.ai_risks_df.columns and not st.session_state.ai_risks_df.dropna(subset=['broad_risk_category']).empty:
        st.info("Chart already generated or can be re-generated. Click 'Proceed' to move on.")
        if st.button("Proceed to Simulate Operational Monitoring", key="next_step13_btn_skip"):
            st.session_state.current_step = 14
            st.rerun()
    else:
        st.warning("No risks identified or categorized yet to plot distribution. Please ensure risks are added and scored in previous steps.")
        if st.button("Go to Step 4 to Add Risks", key="go_to_step4_from13"):
            st.session_state.current_step = 4
            st.rerun()


# Step 14: Simulating Operational Monitoring Feedback: Detecting Data Drift
elif st.session_state.current_step == 14:
    st.subheader("14. Simulating Operational Monitoring Feedback: Detecting Data Drift")
    st.markdown("""
        AI risk management is not a one-time activity; it requires continuous vigilance. Sarah receives an alert from the bank's model monitoring system for the Credit Score Predictor, indicating a significant "Data Drift" (1.4.1) in the input features. This operational feedback is a critical trigger for re-evaluating the associated risks and exemplifies the "Continuous Validation" (4.5) aspect of the AI RMF.

        This scenario demonstrates the necessity of an "Adaptive Cycle" or "outer loop" (1.4.3), where operational data constantly informs risk assessment, prompting Sarah to re-evaluate and update the risk register to maintain trust and performance.
    """)

    credit_score_predictor_model_id = st.session_state.ai_models_df[st.session_state.ai_models_df['model_name'] == 'Credit Score Predictor']['model_id'].iloc[0] if 'Credit Score Predictor' in st.session_state.ai_models_df['model_name'].values else None

    if credit_score_predictor_model_id:
        st.info(f"Simulating data drift alert for model: **Credit Score Predictor** (ID: {credit_score_predictor_model_id})")
        
        data_drift_risk_exists = ((st.session_state.ai_risks_df['model_id'] == credit_score_predictor_model_id) & 
                                  (st.session_state.ai_risks_df['risk_type'] == "Data Drift")).any()

        with st.form("simulate_drift_form"):
            st.text_input("Simulated Alert: Risk Type", "Data Drift", disabled=True, key="drift_risk_type_14")
            hazard_description = st.text_area("Hazard Description (Data Drift)", "Significant shift in demographic distribution of loan applicants causing potential model inaccuracy.", key="drift_hazard_14", disabled=data_drift_risk_exists)
            new_likelihood = st.slider("New Likelihood (1-5)", 1, 5, 4, key="drift_likelihood_14", disabled=data_drift_risk_exists)
            new_magnitude = st.slider("New Magnitude (1-5)", 1, 5, 4, key="drift_magnitude_14", disabled=data_drift_risk_exists)
            submitted = st.form_submit_button("Simulate Data Drift & Update Risk", disabled=data_drift_risk_exists)

            if submitted:
                simulate_data_drift_alert_st(
                    credit_score_predictor_model_id,
                    "Data Drift",
                    hazard_description,
                    new_likelihood,
                    new_magnitude
                )
                st.session_state.current_step = 15
                st.rerun()
            elif data_drift_risk_exists:
                st.info("Data Drift risk has already been simulated and updated.")
    else:
        st.error("Credit Score Predictor model not found. Cannot simulate data drift. Please register it in Step 3.")
        if st.button("Go to Step 3", key="go_to_step3_from14"):
            st.session_state.current_step = 3
            st.rerun()
    
    st.markdown("\nUpdated AI Risks DataFrame after data drift simulation:")
    st.dataframe(st.session_state.ai_risks_df[st.session_state.ai_risks_df['model_id'] == credit_score_predictor_model_id], use_container_width=True)

    if st.button("Proceed to Update Risk Assessment", key="next_step14_btn"):
        st.session_state.current_step = 15
        st.rerun()

# Step 15: Updating Risk Assessment based on Monitoring Feedback (Final Step before Summary)
elif st.session_state.current_step == 15:
    st.subheader("15. Updating Risk Assessment based on Monitoring Feedback")
    st.markdown("""
        Following the data drift alert, Sarah must now formally update the risk assessment for the "Credit Score Predictor". This involves adjusting the likelihood and/or magnitude scores for relevant risks, such as "Performance Degradation" or the newly identified "Data Drift," to reflect the new operational reality. This exemplifies "Continuous Validation" and "Post-Deployment Monitoring" (4.5), which are essential for maintaining the trustworthiness of adaptive AI systems.

        By continuously refining risk assessments based on real-time monitoring, Sarah ensures that the risk register remains a living document that accurately reflects the current state of AI risks at QuantFinance Bank, supporting agile risk management.
    """)

    credit_score_predictor_model_id = st.session_state.ai_models_df[st.session_state.ai_models_df['model_name'] == 'Credit Score Predictor']['model_id'].iloc[0] if 'Credit Score Predictor' in st.session_state.ai_models_df['model_name'].values else None

    if credit_score_predictor_model_id:
        st.info("The data drift event directly impacts the model's 'Performance Degradation' risk, requiring an update to its assessment.")
        
        target_risk_type = "Performance Degradation"
        updated_likelihood_val = 4
        updated_magnitude_val = 4

        # Check the current state of the Performance Degradation risk
        perf_degrad_risk = st.session_state.ai_risks_df[
            (st.session_state.ai_risks_df['model_id'] == credit_score_predictor_model_id) & 
            (st.session_state.ai_risks_df['risk_type'] == target_risk_type)
        ]
        
        is_updated = False
        if not perf_degrad_risk.empty:
            if (perf_degrad_risk['likelihood_score'].iloc[0] == updated_likelihood_val and 
                perf_degrad_risk['magnitude_score'].iloc[0] == updated_magnitude_val):
                is_updated = True
        
        if not is_updated:
            st.markdown("Updating 'Performance Degradation' risk based on the data drift event:")
            if st.button("Formally Update Performance Degradation Risk", key="update_perf_degrad_btn"):
                update_risk_assessment_from_monitoring_st(
                    credit_score_predictor_model_id,
                    target_risk_type,
                    updated_likelihood_val,
                    updated_magnitude_val
                )
                st.session_state.current_step = 16 # Advance to a final summary view
                st.rerun()
        else:
            st.info("The 'Performance Degradation' risk has already been updated to reflect the operational feedback. Proceed to final summary.")
            if st.button("Proceed to Final Summary", key="proceed_final_summary_btn"):
                st.session_state.current_step = 16
                st.rerun()

        st.markdown("\nUpdated AI Risks DataFrame after monitoring feedback:")
        st.dataframe(st.session_state.ai_risks_df[st.session_state.ai_risks_df['model_id'] == credit_score_predictor_model_id], use_container_width=True)

    else:
        st.error("Credit Score Predictor model not found. Cannot update risk assessment. Please register it in Step 3.")
        if st.button("Go to Step 3", key="go_to_step3_from15"):
            st.session_state.current_step = 3
            st.rerun()
    
# Final Summary / Completion Page (Step 16)
elif st.session_state.current_step == 16:
    st.subheader("AI Risk Management Workflow Completed!")
    st.markdown("""
        Sarah has successfully navigated the complex landscape of AI risk management. From initial system setup and model registration to identifying, assessing, mitigating, and continuously monitoring risks—she has built a comprehensive and adaptive AI risk posture for QuantFinance Bank.

        This continuous feedback loop ensures that the bank's AI models remain trustworthy and perform reliably in evolving environments. Congratulations on establishing a robust AI risk management framework!
    """)
    st.balloons()
    
    st.markdown("### Final Comprehensive AI Model Risk Register")
    if 'full_risk_register_df' not in st.session_state or st.session_state.full_risk_register_df.empty:
        get_full_risk_register_st() # Ensure it's generated if skipped
    st.dataframe(st.session_state.full_risk_register_df, use_container_width=True)

    st.markdown("### Final Top Risks Overview")
    if 'top_risks_df' not in st.session_state or st.session_state.top_risks_df.empty:
        identify_top_risks_st(num_top_risks=3) # Default 3 for summary if not already set
    st.dataframe(st.session_state.top_risks_df, use_container_width=True)

    st.markdown("### Overall AI Risk Distribution")
    plot_risk_distribution_by_type_st()

    st.success("Sarah has established a robust AI risk management framework!")
    if st.button("Restart Workflow", key="reset_app_final"):
        st.session_state.clear()
        st.rerun()

# Sidebar Navigation (Optional, given sequential flow, but useful for quick access if steps are independent)
st.sidebar.markdown("## Workflow Navigation")
# Create buttons for each step in the sidebar
for step_num in range(1, 17): # Up to 16 for final summary
    if step_num == st.session_state.current_step:
        st.sidebar.button(f"Step {step_num}", key=f"nav_step_{step_num}", disabled=True)
    else:
        if st.sidebar.button(f"Step {step_num}", key=f"nav_step_{step_num}"):
            st.session_state.current_step = step_num
            st.rerun()

st.sidebar.divider()
if st.sidebar.button("Full Restart Workflow", key="sidebar_reset_app"):
    st.session_state.clear()
    st.rerun()
"""