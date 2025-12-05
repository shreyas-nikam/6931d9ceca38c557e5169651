
### 1. Application Overview

**Narrative Alignment: QuantFinance AI Model Risk Manager - Sarah's Workflow**

This Streamlit application guides Sarah, a Senior Risk Manager at QuantFinance Bank, through the essential lifecycle of AI model risk management. The story unfolds as Sarah takes charge of establishing a robust framework to address the unique challenges posed by AI in the financial sector. She'll begin by setting up the bank's centralized AI risk register, defining a comprehensive risk taxonomy, and formally registering new AI models. As new information emerges—from internal adversarial testing to external data provenance concerns and real-time operational monitoring—Sarah will iteratively identify, quantify, and mitigate risks. The application's narrative mirrors the dynamic, adaptive nature of AI risk management, culminating in Sarah presenting a holistic view of the bank's AI risk posture.

**Real-World Problem the Persona is Solving:**

Sarah's primary challenge is to ensure the trustworthiness, safety, and regulatory compliance of QuantFinance Bank's AI models. The financial industry is increasingly reliant on AI for critical functions like credit assessment and fraud detection, but these systems introduce novel risks such as algorithmic bias, adversarial attacks, and data drift. Without a systematic approach, these risks can lead to significant financial losses, reputational damage, and regulatory penalties. Sarah is tasked with building a proactive and adaptive system that identifies, assesses, and manages these AI-specific risks, aligning with frameworks like the AI Risk Management Framework (AI RMF) and existing model risk guidelines (e.g., SR 11-7).

**How the Streamlit App Helps the Persona Apply Concepts:**

The Streamlit app serves as Sarah's interactive workbench for AI risk management. Instead of passively learning about concepts, Sarah actively *applies* them:
- She uses a structured interface to *register* AI models, embodying the "Centralized Repository" concept.
- She *selects* risks from a predefined taxonomy, directly engaging with the "Risk Taxonomy" principle.
- She *assigns* likelihood and magnitude scores via sliders, performing quantitative risk assessment.
- She *defines* controls and risk responses, implementing mitigation strategies.
- She *responds* to simulated operational alerts by updating risk assessments, demonstrating continuous validation.
- She *visualizes* the risk landscape, enabling informed decision-making and stakeholder communication.

The app's step-by-step nature ensures that each action Sarah takes directly contributes to building and maintaining a comprehensive AI Model Risk Register, reflecting a realistic workflow in her role.

**Learning Goals (Focusing on Applied Skills for Sarah):**

By interacting with this application, Sarah will gain practical experience and develop applied skills in:

1.  **Establishing AI Governance Foundations**: Systematically initializing a central repository for AI models, risks, and controls, demonstrating adherence to AI RMF principles.
2.  **Systematic AI Risk Identification**: Proficiently using a structured AI risk taxonomy to identify a diverse range of AI-specific hazards across different models.
3.  **Quantitative Risk Assessment**: Skillfully assigning likelihood and magnitude scores to risks and understanding the calculation of composite risk scores using the formula $ \text{Risk} = P(\text{event}) \times M(\text{consequence}) $ for effective prioritization.
4.  **Integrating Dynamic Risk Intelligence**: Incorporating real-world insights from adversarial testing and supply chain analysis into the risk register, recognizing their impact on overall risk posture.
5.  **Designing & Implementing Mitigation Strategies**: Defining targeted controls and appropriate risk response options (Mitigate, Transfer, Avoid, Accept) for identified AI risks.
6.  **Continuous Risk Monitoring & Adaptation**: Dynamically updating risk assessments based on simulated operational feedback (e.g., data drift alerts), reinforcing the concept of continuous validation in an adaptive AI environment.
7.  **Holistic Risk Reporting**: Generating and interpreting comprehensive risk registers and visualizations to communicate top risks and overall AI risk posture to stakeholders.

---

### 2. User Interface Requirements

#### Layout & Navigation Structure

The application will feature a single-page, sequential narrative flow controlled by `st.session_state` and "Next" buttons, guiding Sarah through each distinct stage of her workflow. Each step will present relevant context, input forms, and immediate feedback or results.

**Overall Page Structure:**

-   **Header**: A fixed header (`st.title` or `st.header`) at the top: "QuantFinance AI Model Risk Manager: Sarah's Workflow"
-   **Main Content Area**: This is the primary interactive section, dynamically updated based on the current step in the narrative. It will contain:
    -   `st.subheader` and `st.markdown` for story context and instructions.
    -   Input widgets for data entry or selection.
    -   Display components for DataFrames and visualizations.
    -   Action buttons to trigger calculations, updates, or to advance the narrative.
-   **Navigation**: Primarily driven by `st.button` labeled "Next Step" or specific action buttons, incrementing a `st.session_state['current_step']` variable. A "Restart Workflow" button in the sidebar (or at the end) will allow Sarah to reset the application.

**Navigation Flow (Chronological Narrative Sequence):**

1.  **Welcome & System Initialization (Step 1)**
    *   **Content**: Introduction to Sarah's role and the AI risk management challenge. Explains the "Centralized Repository" concept.
    *   **Action**: `st.button("Initialize AI Risk Management System")` to set up initial empty DataFrames and counters in `st.session_state`.
    *   **Feedback**: `st.success` message, display of initial empty DataFrames.

2.  **AI Risk Taxonomy Definition (Step 2)**
    *   **Content**: Narrative on the importance of a standardized taxonomy, linking to AI RMF "Risk Taxonomy". Displays the `AI_RISK_TAXONOMY`.
    *   **Action**: `st.button("Acknowledge Taxonomy & Proceed to Model Registration")` to advance.

3.  **Register a New AI Model (Step 3)**
    *   **Content**: Story about registering the "Credit Score Predictor".
    *   **Form**: Inputs for model details.
    *   **Action**: `st.button("Register AI Model")` to add to `st.session_state.ai_models_df`.
    *   **Feedback**: `st.success` message, `st.dataframe` showing updated `ai_models_df`.

4.  **Initial Risk Identification (Step 4)**
    *   **Content**: Narrative on identifying hazards for the newly registered model, referencing "Risk Register: Identification and Categorization".
    *   **Form**: Select model, select risk category, then select specific risk types (multiselect), and optionally add a custom hazard description.
    *   **Action**: `st.button("Add Selected Risks")` to populate `st.session_state.ai_risks_df`.
    *   **Feedback**: `st.success` message, `st.dataframe` showing identified risks for the model.

5.  **Quantifying Risk: Likelihood and Magnitude Assessment (Step 5)**
    *   **Content**: Explains quantifying risks using likelihood and magnitude, introduces the formula: $$ \text{Risk} = P(\text{event}) \times M(\text{consequence}) $$
    *   **Form**: Iterates through identified risks for the current model, providing `st.slider` for `likelihood_score` and `magnitude_score` for each.
    *   **Action**: `st.button("Assign Scores")` to update `st.session_state.ai_risks_df`.
    *   **Feedback**: `st.success` message, `st.dataframe` with updated scores.

6.  **Calculating the Composite Risk Score (Step 6)**
    *   **Content**: Narrative on deriving a single metric for prioritization using the formula.
    *   **Action**: `st.button("Calculate Composite Risk Scores")` to compute for all scored risks.
    *   **Feedback**: `st.success` message, `st.dataframe` showing `composite_risk_score`.

7.  **Integrating Insights from Adversarial Testing (Step 7)**
    *   **Content**: Story about Red-Teaming findings for the Credit Score Predictor, highlighting "Adversarial Testing and Red-Teaming".
    *   **Form**: Inputs for adversarial `attack_type`, `description`, `likelihood_score`, `magnitude_score`.
    *   **Action**: `st.button("Add Adversarial Risk & Score")` to add to `st.session_state.ai_risks_df`.
    *   **Feedback**: `st.success` message, `st.dataframe` showing the new risk.

8.  **Addressing Supply Chain and Data Provenance Risks (Step 8)**
    *   **Content**: Narrative on broadening risk scope to include "AI Supply Chain" and "Data Provenance" for a "Fraud Detection System".
    *   **Form (Dual Purpose)**:
        -   Option to register a new model (Fraud Detection System) if not already present.
        -   Inputs for "Data Provenance" risk (`hazard_description`, `likelihood`, `magnitude`).
        -   Inputs for "Third-Party Dependency" risk (`hazard_description`, `likelihood`, `magnitude`).
    *   **Action**: `st.button("Add Data Provenance Risk")` and `st.button("Add Third-Party Dependency Risk")` to update DFs.
    *   **Feedback**: `st.success` messages, `st.dataframe` for `ai_models_df` and `ai_risks_df`.

9.  **Defining Controls and Mitigation Strategies (Step 9)**
    *   **Content**: Narrative on designing defenses, aligning with "Risk Controls and Mitigation Strategies".
    *   **Form**: Select a risk from existing, input `control_description`.
    *   **Action**: `st.button("Define Control")` to add to `st.session_state.ai_controls_df`.
    *   **Feedback**: `st.success` message, `st.dataframe` showing controls.

10. **Assigning Risk Response Options (Step 10)**
    *   **Content**: Story about formalizing risk responses, referencing "Risk Response Options".
    *   **Form**: Iterates through defined controls, provides `st.slider` for `effectiveness_score` and `st.selectbox` for `risk_response`.
    *   **Action**: `st.button("Assign Risk Responses")` to update `st.session_state.ai_controls_df`.
    *   **Feedback**: `st.success` message, `st.dataframe` with updated control details.

11. **Reviewing the Comprehensive AI Model Risk Register (Step 11)**
    *   **Content**: Narrative on gaining a holistic view, reflecting "Centralized Repository" and "Assurance Documentation".
    *   **Action**: `st.button("Generate Comprehensive AI Model Risk Register")` to merge DataFrames.
    *   **Feedback**: `st.success` message, `st.dataframe` showing `full_risk_register_df`.

12. **Analyzing and Prioritizing High-Scoring Risks (Step 12)**
    *   **Content**: Narrative on identifying top risks, supporting "Risk-based" decision-making.
    *   **Form**: `st.number_input` for `num_top_risks`.
    *   **Action**: `st.button("Identify Top Risks")` to sort and display.
    *   **Feedback**: `st.dataframe` showing `top_risks_df`.

13. **Visualizing Risk Distribution by Type (Step 13)**
    *   **Content**: Narrative on executive overview, supporting "MEASURE" function.
    *   **Action**: `st.button("Generate Risk Distribution Chart")` to render the bar chart.
    *   **Feedback**: `st.pyplot` display of the chart.

14. **Simulating Operational Monitoring Feedback: Detecting Data Drift (Step 14)**
    *   **Content**: Story about a real-time "Data Drift" alert for Credit Score Predictor, emphasizing "Continuous Validation" and "Adaptive Cycle".
    *   **Form**: Pre-filled/read-only inputs for a new Data Drift risk or an update to an existing "Performance Degradation" risk, with sliders for `new_likelihood` and `new_magnitude`.
    *   **Action**: `st.button("Simulate Data Drift & Update Risk")` to update `st.session_state.ai_risks_df`.
    *   **Feedback**: `st.warning` message, `st.dataframe` showing the updated risk.

15. **Updating Risk Assessment based on Monitoring Feedback (Step 15)**
    *   **Content**: Narrative on formally updating risk assessment, highlighting "Post-Deployment Monitoring".
    *   **Action (Implicit/Automatic)**: Displays the specific updated risk (e.g., Performance Degradation) and its new composite score.
    *   **Final Action**: `st.button("Acknowledge Update & Complete Workflow")` to signify completion, potentially displaying final summary.
    *   **Feedback**: `st.balloons()` and a `st.success` message for workflow completion, with final dashboard views.

#### Input Widgets and Controls

-   **`st.button`**:
    -   **Purpose**: Trigger actions like initializing the system, registering models, adding risks, assigning scores, calculating, generating reports, and advancing the story (`"Next Step"`).
    -   **Real-World Action**: Sarah making a decision, committing an entry, or requesting an analysis.
    -   **Parameters**: `label` (string, e.g., "Register AI Model"), `key` (optional, string for uniqueness).
-   **`st.text_input`**:
    -   **Purpose**: Capture single-line text data such as `model_name`, `owner`, `risk_type` (for custom entry), `attack_type`.
    -   **Real-World Action**: Sarah entering specific factual details about models or risks.
    -   **Parameters**: `label` (string), `value` (string, default), `key` (string).
    -   *Example*: `st.text_input("Model Name", "Credit Score Predictor", key="model_name_input")`
-   **`st.text_area`**:
    -   **Purpose**: Capture multi-line text data such as `description`, `use_case`, `hazard_description`, `control_description`.
    -   **Real-World Action**: Sarah providing detailed descriptions, rationales, or mitigation plans.
    -   **Parameters**: `label` (string), `value` (string, default), `height` (int, optional), `key` (string).
    -   *Example*: `st.text_area("Hazard Description", "Poor or incomplete historical data leading to inaccurate credit scores.", key="hazard_desc_input")`
-   **`st.selectbox`**:
    -   **Purpose**: Select a single option from a predefined list, e.g., `model_name` for context, `risk_category` from `AI_RISK_TAXONOMY`, `status` for a model, `risk_response` for a control.
    -   **Real-World Action**: Sarah categorizing an item, selecting a specific entity to focus on, or choosing a strategic response.
    -   **Parameters**: `label` (string), `options` (list or tuple), `index` (int, default index of selected option), `key` (string).
    -   *Example*: `st.selectbox("Select Model", options=st.session_state.ai_models_df['model_name'].tolist(), key="select_model_dropdown")`
-   **`st.multiselect`**:
    -   **Purpose**: Select multiple options from a predefined list, specifically for `risk_type` from a chosen `AI_RISK_TAXONOMY` category.
    -   **Real-World Action**: Sarah identifying multiple specific hazards associated with a model simultaneously.
    -   **Parameters**: `label` (string), `options` (list or tuple), `default` (list of selected options), `key` (string).
    -   *Example*: `st.multiselect("Select Specific Risk Types", options=st.session_state.AI_RISK_TAXONOMY[selected_category], key="risk_types_multiselect")`
-   **`st.slider`**:
    -   **Purpose**: Assign numerical scores for `likelihood_score`, `magnitude_score`, `effectiveness_score`. Range will typically be 1 to 5.
    -   **Real-World Action**: Sarah performing a quantitative assessment of risk severity or control efficacy, reflecting a spectrum of impact.
    -   **Parameters**: `label` (string), `min_value` (int), `max_value` (int), `value` (int, default starting value), `step` (int), `key` (string).
    -   *Example*: `st.slider("Likelihood Score (1-5)", 1, 5, 3, key=f"likelihood_slider_{risk_id}")`
-   **`st.number_input`**:
    -   **Purpose**: Input a specific number, e.g., for `num_top_risks` to display.
    -   **Real-World Action**: Sarah customizing her view for risk prioritization.
    -   **Parameters**: `label` (string), `min_value` (int), `max_value` (int), `value` (int, default), `step` (int), `key` (string).
    -   *Example*: `st.number_input("Number of Top Risks to Display", min_value=1, value=3, step=1, key="num_top_risks_input")`

#### Visualization Components

-   **`st.dataframe`**:
    -   **Purpose**: Display the current state of `ai_models_df`, `ai_risks_df`, `ai_controls_df`, `full_risk_register_df`, and `top_risks_df`.
    -   **Library**: Pandas DataFrames, rendered natively by Streamlit.
    -   **Format**: Interactive table, with sortable columns and basic filtering capabilities.
    -   **Expected Outputs**:
        -   Detailed list of registered AI models.
        -   Table of identified risks with their hazard descriptions, assigned likelihood, magnitude, and calculated composite scores.
        -   List of defined controls with descriptions, effectiveness scores, and risk responses.
        -   A comprehensive merged table showing models, their associated risks, and corresponding controls.
        -   A prioritized table listing the highest-scoring risks.
    -   **Tie-back to Story**: Provides Sarah with clear, auditable records and immediate updates on the impact of her inputs, forming the core "Centralized Repository" and "Assurance Documentation."

-   **`st.pyplot`**:
    -   **Purpose**: Display the bar chart showing the distribution of AI risks by broad category.
    -   **Library**: Matplotlib and Seaborn (as used in the notebook).
    -   **Format**: Static bar chart.
    -   **Expected Output**: A bar plot titled 'Distribution of AI Risks by Broad Category', with categories (e.g., "Data Risk", "Model Risk") on the x-axis and "Number of Risks" on the y-axis, rotated x-axis labels for readability.
    -   **Tie-back to Story**: Allows Sarah to gain a high-level, strategic understanding of where AI risks are concentrated across the bank, supporting the "MEASURE" function of the AI RMF and informing strategic investments in risk mitigation.

#### Interactive Elements & Feedback Mechanisms

-   **Action Buttons**: As described in "Input Widgets and Controls," buttons are central to advancing the narrative and committing changes.
-   **Dynamic Content Update**:
    -   **DataFrames**: Each `add_ai_model`, `add_ai_risk`, `assign_risk_scores`, `calculate_composite_risk_score`, `add_ai_control`, `assign_risk_response`, `get_full_risk_register`, `identify_top_risks`, `simulate_data_drift_alert`, and `update_risk_assessment_from_monitoring` operation will immediately re-render the relevant `st.dataframe` to show the updated state of the AI risk register. This instant feedback loop is crucial for Sarah to see the direct consequence of her actions.
    -   **Widget Visibility**: Certain widgets or sections will only appear once previous steps are completed (e.g., risk assessment sliders appear after risks are identified).
-   **Feedback Messages**:
    -   `st.success("Action completed successfully!")`: Appears after successful data additions, updates, or calculations.
    -   `st.info("Contextual information or guidance for the next step.")`: Provides non-critical information or narrative progression.
    -   `st.warning("Attention: A data drift alert has been triggered!")`: Used for simulated alerts or important notifications requiring Sarah's attention.
    -   `st.error("Error: Please check inputs.")`: For validation errors (if implemented).
-   **Narrative Progression**: Each button click that advances the `st.session_state['current_step']` will clear the previous content and render the next narrative segment, forms, and outputs, maintaining a clear story-driven flow.
-   **Highlighting Changes**: When risks are updated (e.g., after data drift simulation), the relevant rows in the displayed `st.dataframe` could be highlighted (e.g., using `st.dataframe`'s `highlight_cols` or custom CSS if possible) to draw Sarah's attention to the changes.

---

### 3. Additional Requirements

#### Annotations & Tooltips

Annotations and contextual explanations are crucial to ensure Sarah understands the significance of her actions and the outputs within the real-world scenario, without resorting to direct conceptual explanations.

-   **`st.markdown` for Narrative & Context**:
    -   Each major section (corresponding to a notebook step) will start with `st.subheader` and `st.markdown` to provide Sarah with the ongoing narrative, explaining *why* she is performing the current task and its real-world relevance to QuantFinance Bank.
    -   *Example*: Before risk quantification: `st.markdown("Quantifying risks helps you understand their potential impact. You will assess the likelihood ($P(\text{event})$) of a hazard occurring and the magnitude ($M(\text{consequence})$) of its potential harm. This feeds into the core formula: $$ \text{Risk} = P(\text{event}) \times M(\text{consequence}) $$")`

-   **`st.info` / `st.caption` for In-Context Guidance**:
    -   These will be used adjacent to input widgets or output displays to offer specific guidance or interpretation related to the persona's task.
    -   *Example (next to `likelihood_score` slider)*: `st.info("Sarah, assess how frequently this risk is likely to occur (1=Rarely, 5=Frequently).")`
    -   *Example (next to `composite_risk_score` column)*: `st.caption("A higher composite score indicates greater urgency for mitigation. This guides your resource allocation.")`
    -   *Example (next to `AI_RISK_TAXONOMY` display)*: `st.info("This taxonomy ensures a systematic approach to identifying diverse AI-specific risks, preventing blind spots.")`

-   **Dynamic Annotations**:
    -   After a composite score is calculated, a brief `st.write` or `st.markdown` message could appear, interpreting the score in simple terms, e.g., `st.write(f"Risk ID {risk_id} has a composite score of {composite_score}. This is a { 'high' if composite_score >= 15 else ('medium' if composite_score >= 8 else 'low') }-severity risk.")`

#### State Management Requirements

Robust state management is paramount for a story-driven application to ensure a seamless and uninterrupted workflow for Sarah.

-   **Centralized `st.session_state`**: All dynamic data, counters, and the current position in the narrative flow will be stored in `st.session_state`.
    -   `st.session_state['ai_models_df']`: Pandas DataFrame for registered models.
    -   `st.session_state['ai_risks_df']`: Pandas DataFrame for identified risks.
    -   `st.session_state['ai_controls_df']`: Pandas DataFrame for defined controls.
    -   `st.session_state['model_id_counter']`: Integer for auto-incrementing model IDs.
    -   `st.session_state['risk_id_counter']`: Integer for auto-incrementing risk IDs.
    -   `st.session_state['control_id_counter']`: Integer for auto-incrementing control IDs.
    -   `st.session_state['AI_RISK_TAXONOMY']`: The predefined Python dictionary for risk classification.
    -   `st.session_state['current_step']`: Integer representing the current step in Sarah's narrative workflow (e.g., 1 to 15).
    -   `st.session_state['full_risk_register_df']`: The merged DataFrame for the comprehensive register.
    -   `st.session_state['top_risks_df']`: DataFrame for prioritized risks.

-   **Initialization and Persistence**:
    -   Upon the very first load of the application, `st.session_state` variables will be initialized according to the initial state defined in the `initialize_risk_management_system` function and the `AI_RISK_TAXONOMY` definition.
    -   Each function that modifies these data structures or counters will explicitly update the corresponding `st.session_state` entry.
    -   All input widgets will be linked to `st.session_state` using unique `key` parameters to ensure their values persist across reruns and throughout the narrative.

-   **No Loss of Progress**: If Sarah navigates away from the application or refreshes the page (within the same browser session), `st.session_state` will automatically preserve her progress, allowing her to continue from where she left off. A "Restart Workflow" button will be provided to intentionally clear all `st.session_state` data and reset the application to its initial state.

---

### 4. Notebook Content and Code Requirements

This section explicitly maps each significant component of the Jupyter Notebook to its interactive Streamlit counterpart, including code stubs and how markdown explanations transition into the UI.

**Global Setup & Data Management (Initial `app.py` structure):**

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set display options (optional, as st.dataframe handles much of this)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

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
        
        # Ensure 'risk_type' column exists and map to broad categories
        if 'risk_type' in st.session_state.ai_risks_df.columns:
            st.session_state.ai_risks_df['broad_risk_category'] = st.session_state.ai_risks_df['risk_type'].map(category_map)
            risk_counts = st.session_state.ai_risks_df['broad_risk_category'].value_counts().reset_index()
            risk_counts.columns = ['Broad Risk Category', 'Number of Risks']

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
    st.dataframe(st.session_state.ai_models_df)
    st.dataframe(st.session_state.ai_risks_df)
    st.dataframe(st.session_state.ai_controls_df)

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

# --- Subsequent steps would follow a similar pattern ---

# Example for Step 3: Registering a New AI Model
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
            new_model_id = add_ai_model_st(model_name, use_case, description, owner, status)
            # Store the ID for future steps if needed
            st.session_state.credit_score_predictor_model_id = new_model_id 
            st.session_state.current_step = 4
            st.rerun()
    
    if not st.session_state.ai_models_df.empty:
        st.markdown("\nUpdated AI Models DataFrame:")
        st.dataframe(st.session_state.ai_models_df)

# Example for Step 4: Initial Risk Identification
elif st.session_state.current_step == 4:
    st.subheader("4. Initial Risk Identification: Potential Hazards for the Credit Score Model")
    st.markdown("""
        With the Credit Score Predictor registered, Sarah begins the crucial process of identifying potential AI-specific hazards. She draws upon her expertise and the bank's risk taxonomy to foresee issues that could arise from data quality, model behavior, or operational deployment. This proactive identification is key to mitigating future problems and aligns with Section 4.2 of the AI RMF, focusing on "Risk Register: Identification and Categorization."

        Sarah considers risks like "Data Quality" (poor input data leading to incorrect scores), "Algorithmic Bias" (unfair scoring for certain demographic groups), and "Performance Degradation" (the model's accuracy declining over time). This step is crucial for anticipating challenges and preventing negative impacts on customers and the bank's reputation.
    """)

    credit_score_predictor_model_id = st.session_state.ai_models_df[st.session_state.ai_models_df['model_name'] == 'Credit Score Predictor']['model_id'].iloc[0] if 'Credit Score Predictor' in st.session_state.ai_models_df['model_name'].values else None

    if credit_score_predictor_model_id:
        st.write(f"Adding risks for model: **Credit Score Predictor** (ID: {credit_score_predictor_model_id})")
        
        # Add risks as per notebook (Data Quality, Algorithmic Bias, Performance Degradation)
        if st.button("Add Data Quality Risk", key="add_dq_risk"):
            add_ai_risk_st(credit_score_predictor_model_id, "Data Quality", "Poor or incomplete historical data leading to inaccurate credit scores.")
        if st.button("Add Algorithmic Bias Risk", key="add_ab_risk"):
            add_ai_risk_st(credit_score_predictor_model_id, "Algorithmic Bias", "Model exhibits biased decision-making against certain demographic groups.")
        if st.button("Add Performance Degradation Risk", key="add_pd_risk"):
            add_ai_risk_st(credit_score_predictor_model_id, "Performance Degradation", "Model accuracy degrades over time due to changes in credit behavior patterns.")
        
        st.markdown("\nUpdated AI Risks DataFrame:")
        st.dataframe(st.session_state.ai_risks_df[st.session_state.ai_risks_df['model_id'] == credit_score_predictor_model_id])

        if st.button("Proceed to Quantify Risks", key="next_step4_btn"):
            st.session_state.current_step = 5
            st.rerun()
    else:
        st.error("Credit Score Predictor model not found. Please go back to Step 3.")


# Example for Step 5: Quantifying Risk: Likelihood and Magnitude Assessment
elif st.session_state.current_step == 5:
    st.subheader("5. Quantifying Risk: Likelihood and Magnitude Assessment")
    st.markdown("""
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
        st.info("Sarah, use the sliders below to assign likelihood and magnitude scores for each risk.")
        scored_risks_data = []
        for index, risk in risks_to_score.iterrows():
            st.markdown(f"**Risk ID: {int(risk['risk_id'])}**")
            st.write(f"Type: {risk['risk_type']}")
            st.write(f"Hazard: {risk['hazard_description']}")
            
            likelihood = st.slider(f"Likelihood (1-5) for Risk ID {int(risk['risk_id'])}", 1, 5, 3, key=f"likelihood_{int(risk['risk_id'])}")
            magnitude = st.slider(f"Magnitude (1-5) for Risk ID {int(risk['risk_id'])}", 1, 5, 3, key=f"magnitude_{int(risk['risk_id'])}")
            scored_risks_data.append({'risk_id': int(risk['risk_id']), 'likelihood': likelihood, 'magnitude': magnitude})
            st.markdown("---")
        
        if st.button("Assign All Scores", key="assign_scores_btn"):
            for score_data in scored_risks_data:
                assign_risk_scores_st(score_data['risk_id'], score_data['likelihood'], score_data['magnitude'])
            st.session_state.current_step = 6
            st.rerun()
    else:
        st.info("All identified risks have been scored. Proceed to composite score calculation.")
        if st.button("Proceed to Calculate Composite Scores", key="next_step5_btn"):
            st.session_state.current_step = 6
            st.rerun()

    st.markdown("\nUpdated AI Risks DataFrame with scores:")
    st.dataframe(st.session_state.ai_risks_df)

# Example for Step 6: Calculating the Composite Risk Score
elif st.session_state.current_step == 6:
    st.subheader("6. Calculating the Composite Risk Score")
    st.markdown("""
        With likelihood and magnitude scores assigned, Sarah can now calculate the composite risk score for each hazard. This score, derived from the formula $Risk = P(\text{event}) \times M(\text{consequence})$, provides a single, aggregated metric for each risk, allowing for easy comparison and prioritization. This calculation is a direct application of the "Quantitative and Qualitative Assessment" mentioned in the AI RMF (Section 4.2).

        By standardizing risk quantification, Sarah ensures that all stakeholders at QuantFinance Bank can understand and compare the severity of different AI risks, guiding resource allocation for risk mitigation.
    """)

    uncalculated_risks = st.session_state.ai_risks_df[
        st.session_state.ai_risks_df['composite_risk_score'].isna() &
        st.session_state.ai_risks_df['likelihood_score'].notna() &
        st.session_state.ai_risks_df['magnitude_score'].notna()
    ]

    if not uncalculated_risks.empty:
        if st.button("Calculate All Composite Risk Scores", key="calculate_composite_btn"):
            for risk_id in uncalculated_risks['risk_id']:
                calculate_composite_risk_score_st(int(risk_id))
            st.session_state.current_step = 7
            st.rerun()
    else:
        st.info("All risks with assigned likelihood and magnitude scores already have composite scores.")
        if st.button("Proceed to Integrating Adversarial Insights", key="next_step6_btn"):
            st.session_state.current_step = 7
            st.rerun()

    st.markdown("\nUpdated AI Risks DataFrame with composite scores:")
    st.dataframe(st.session_state.ai_risks_df)

# Example for Step 7: Integrating Insights from Adversarial Testing
elif st.session_state.current_step == 7:
    st.subheader("7. Integrating Insights from Adversarial Testing: Uncovering Robustness Risks")
    st.markdown("""
        QuantFinance Bank's dedicated Red-Teaming unit has just concluded an exercise targeting the Credit Score Predictor. Their findings reveal vulnerabilities to "Adversarial Attacks" – subtle manipulations of input data that can cause misclassification (e.g., making a high-risk applicant appear low-risk). Sarah must immediately integrate these critical insights into the risk register. This directly reflects the importance of "Adversarial Testing and Red-Teaming" (Section 2) in the AI RMF for uncovering AI-specific security vulnerabilities like "Deceptive Inputs" (2.2) and "Data Poisoning Attacks" (2.4).

        By documenting these specific threats, Sarah ensures the bank can develop targeted defenses, preventing malicious actors from exploiting the model and protecting the integrity of loan decisions.
    """)

    credit_score_predictor_model_id = st.session_state.ai_models_df[st.session_state.ai_models_df['model_name'] == 'Credit Score Predictor']['model_id'].iloc[0] if 'Credit Score Predictor' in st.session_state.ai_models_df['model_name'].values else None

    if credit_score_predictor_model_id:
        st.write(f"Adding adversarial risk for model: **Credit Score Predictor** (ID: {credit_score_predictor_model_id})")
        with st.form("add_adversarial_risk_form"):
            attack_type = st.text_input("Adversarial Attack Type", "Adversarial Attack (Evasion)", key="attack_type_7")
            description = st.text_area("Description", "Subtle manipulation of input features to cause a misclassification of a high-risk individual as low-risk.", key="description_7")
            likelihood = st.slider("Likelihood (1-5)", 1, 5, 4, key="adv_likelihood_7")
            magnitude = st.slider("Magnitude (1-5)", 1, 5, 5, key="adv_magnitude_7")
            submitted = st.form_submit_button("Add Adversarial Risk & Score")

            if submitted:
                add_adversarial_risk_st(credit_score_predictor_model_id, attack_type, description, likelihood, magnitude)
                st.session_state.current_step = 8
                st.rerun()
    else:
        st.error("Credit Score Predictor model not found. Please ensure it's registered.")
    
    st.markdown("\nUpdated AI Risks DataFrame with adversarial attack risk:")
    st.dataframe(st.session_state.ai_risks_df)
    
    if st.session_state.current_step == 7 and st.button("Skip Step (if risk already added) & Proceed", key="skip_step7_btn"):
        st.session_state.current_step = 8
        st.rerun()

# Example for Step 8: Addressing Supply Chain and Data Provenance Risks
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
    else:
        fraud_model_id = existing_fraud_model['model_id'].iloc[0]
        st.info(f"Model '{fraud_detection_model_name}' (ID: {fraud_model_id}) already exists. Using existing model_id.")

    if fraud_model_id:
        st.markdown("### Add Data Provenance Risk for Fraud Detection System")
        with st.form("add_data_provenance_risk_form"):
            dp_hazard_description = st.text_area("Hazard Description (Data Provenance)", "Lack of verifiable data provenance for historical transaction data used in training, raising concerns about data integrity and potential hidden biases.", key="dp_desc_8")
            dp_likelihood = st.slider("Likelihood (1-5)", 1, 5, 3, key="dp_likelihood_8")
            dp_magnitude = st.slider("Magnitude (1-5)", 1, 5, 4, key="dp_magnitude_8")
            dp_submitted = st.form_submit_button("Add Data Provenance Risk")

            if dp_submitted:
                add_supply_chain_risk_st(
                    model_name=fraud_detection_model_name, model_use_case="", model_description="", model_owner="", model_status="",
                    risk_type="Data Risk", hazard_description=dp_hazard_description, likelihood=dp_likelihood, magnitude=dp_magnitude
                )
        
        st.markdown("### Add Third-Party Dependency Risk for Fraud Detection System")
        with st.form("add_third_party_risk_form"):
            tpd_hazard_description = st.text_area("Hazard Description (Third-Party Dependency)", "Reliance on a third-party feature engineering library with unknown vulnerabilities or insufficient documentation.", key="tpd_desc_8")
            tpd_likelihood = st.slider("Likelihood (1-5)", 1, 5, 3, key="tpd_likelihood_8")
            tpd_magnitude = st.slider("Magnitude (1-5)", 1, 5, 3, key="tpd_magnitude_8")
            tpd_submitted = st.form_submit_button("Add Third-Party Dependency Risk")

            if tpd_submitted:
                add_supply_chain_risk_st(
                    model_name=fraud_detection_model_name, model_use_case="", model_description="", model_owner="", model_status="",
                    risk_type="Organizational Risk", hazard_description=tpd_hazard_description, likelihood=tpd_likelihood, magnitude=tpd_magnitude
                )
        
        if st.button("Proceed to Define Controls", key="next_step8_btn"):
            st.session_state.current_step = 9
            st.rerun()

    st.markdown("\nUpdated AI Models DataFrame:")
    st.dataframe(st.session_state.ai_models_df)
    st.markdown("\nUpdated AI Risks DataFrame:")
    st.dataframe(st.session_state.ai_risks_df)


# Example for Step 9: Defining Controls and Mitigation Strategies
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

    if algorithmic_bias_risk_id:
        if st.button(f"Add Control for Algorithmic Bias (Risk ID: {int(algorithmic_bias_risk_id)})", key="add_control_ab"):
            add_ai_control_st(
                algorithmic_bias_risk_id,
                "Implement fairness metrics monitoring (e.g., Equal Opportunity, Demographic Parity) and regular bias audits."
            )
    if adversarial_attack_risk_id:
        if st.button(f"Add Control for Adversarial Attack (Risk ID: {int(adversarial_attack_risk_id)})", key="add_control_aa"):
            add_ai_control_st(
                adversarial_attack_risk_id,
                "Implement adversarial training techniques and robust input validation/sanitization mechanisms."
            )
    if data_provenance_risk_id:
        if st.button(f"Add Control for Data Provenance (Risk ID: {int(data_provenance_risk_id)})", key="add_control_dp"):
            add_ai_control_st(
                data_provenance_risk_id,
                "Establish clear data lineage tracking and cryptographic hashing for all training datasets."
            )

    st.markdown("\nUpdated AI Controls DataFrame:")
    st.dataframe(st.session_state.ai_controls_df)

    if st.button("Proceed to Assign Risk Response Options", key="next_step9_btn"):
        st.session_state.current_step = 10
        st.rerun()

# Example for Step 10: Assigning Risk Response Options
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
        st.info("Sarah, for each control, specify its expected effectiveness and the bank's chosen risk response.")
        responded_controls_data = []
        for index, control in controls_to_respond.iterrows():
            st.markdown(f"**Control ID: {int(control['control_id'])}**")
            st.write(f"Description: {control['control_description']}")
            
            effectiveness = st.slider(f"Effectiveness Score (1-5) for Control ID {int(control['control_id'])}", 1, 5, 4, key=f"effectiveness_{int(control['control_id'])}")
            risk_response = st.selectbox(f"Risk Response for Control ID {int(control['control_id'])}", ["Mitigate", "Transfer", "Avoid", "Accept"], key=f"response_{int(control['control_id'])}")
            responded_controls_data.append({'control_id': int(control['control_id']), 'effectiveness': effectiveness, 'risk_response': risk_response})
            st.markdown("---")
        
        if st.button("Assign All Responses", key="assign_responses_btn"):
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
    st.dataframe(st.session_state.ai_controls_df)

# Example for Step 11: Reviewing the Comprehensive AI Model Risk Register
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
        st.dataframe(st.session_state.full_risk_register_df)
    
    if st.session_state.current_step == 11 and st.button("Proceed to Analyze Top Risks", key="next_step11_btn_skip"):
        st.session_state.current_step = 12
        st.rerun()

# Example for Step 12: Analyzing and Prioritizing High-Scoring Risks
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
            st.markdown(f"\nTop {num_top_risks} AI Risks by Composite Score:")
            st.dataframe(st.session_state.top_risks_df)
        elif st.button("Proceed to Visualize Risk Distribution", key="next_step12_btn_skip"):
            st.session_state.current_step = 13
            st.rerun()
    else:
        st.warning("Please generate the comprehensive risk register in Step 11 first.")
        if st.button("Go to Step 11", key="go_to_step11_from12"):
            st.session_state.current_step = 11
            st.rerun()

# Example for Step 13: Visualizing Risk Distribution by Type
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
    elif st.button("Proceed to Simulate Operational Monitoring", key="next_step13_btn_skip"):
        st.session_state.current_step = 14
        st.rerun()

# Example for Step 14: Simulating Operational Monitoring Feedback: Detecting Data Drift
elif st.session_state.current_step == 14:
    st.subheader("14. Simulating Operational Monitoring Feedback: Detecting Data Drift")
    st.markdown("""
        AI risk management is not a one-time activity; it requires continuous vigilance. Sarah receives an alert from the bank's model monitoring system for the Credit Score Predictor, indicating a significant "Data Drift" (1.4.1) in the input features. This operational feedback is a critical trigger for re-evaluating the associated risks and exemplifies the "Continuous Validation" (4.5) aspect of the AI RMF.

        This scenario demonstrates the necessity of an "Adaptive Cycle" or "outer loop" (1.4.3), where operational data constantly informs risk assessment, prompting Sarah to re-evaluate and update the risk register to maintain trust and performance.
    """)

    credit_score_predictor_model_id = st.session_state.ai_models_df[st.session_state.ai_models_df['model_name'] == 'Credit Score Predictor']['model_id'].iloc[0] if 'Credit Score Predictor' in st.session_state.ai_models_df['model_name'].values else None

    if credit_score_predictor_model_id:
        st.info(f"Simulating data drift alert for model: **Credit Score Predictor** (ID: {credit_score_predictor_model_id})")
        with st.form("simulate_drift_form"):
            st.text_input("Simulated Alert: Risk Type", "Data Drift", disabled=True, key="drift_risk_type_14")
            hazard_description = st.text_area("Hazard Description (Data Drift)", "Significant shift in demographic distribution of loan applicants causing potential model inaccuracy.", key="drift_hazard_14")
            new_likelihood = st.slider("New Likelihood (1-5)", 1, 5, 4, key="drift_likelihood_14")
            new_magnitude = st.slider("New Magnitude (1-5)", 1, 5, 4, key="drift_magnitude_14")
            submitted = st.form_submit_button("Simulate Data Drift & Update Risk")

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
    else:
        st.error("Credit Score Predictor model not found. Cannot simulate data drift.")
    
    st.markdown("\nUpdated AI Risks DataFrame after data drift simulation:")
    st.dataframe(st.session_state.ai_risks_df[st.session_state.ai_risks_df['model_id'] == credit_score_predictor_model_id])

    if st.session_state.current_step == 14 and st.button("Skip Simulation (if already run) & Proceed", key="skip_step14_btn"):
        st.session_state.current_step = 15
        st.rerun()

# Example for Step 15: Updating Risk Assessment based on Monitoring Feedback (Final Step)
elif st.session_state.current_step == 15:
    st.subheader("15. Updating Risk Assessment based on Monitoring Feedback")
    st.markdown("""
        Following the data drift alert, Sarah must now formally update the risk assessment for the "Credit Score Predictor". This involves adjusting the likelihood and/or magnitude scores for relevant risks, such as "Performance Degradation" or the newly identified "Data Drift," to reflect the new operational reality. This exemplifies "Continuous Validation" and "Post-Deployment Monitoring" (4.5), which are essential for maintaining the trustworthiness of adaptive AI systems.

        By continuously refining risk assessments based on real-time monitoring, Sarah ensures that the risk register remains a living document that accurately reflects the current state of AI risks at QuantFinance Bank, supporting agile risk management.
    """)

    credit_score_predictor_model_id = st.session_state.ai_models_df[st.session_state.ai_models_df['model_name'] == 'Credit Score Predictor']['model_id'].iloc[0] if 'Credit Score Predictor' in st.session_state.ai_models_df['model_name'].values else None

    if credit_score_predictor_model_id:
        st.info("The data drift event directly impacts the model's 'Performance Degradation' risk.")
        
        # We need to simulate the update for Performance Degradation
        # The notebook had an explicit call: update_risk_assessment_from_monitoring(ai_risks_df, model_id=credit_score_predictor_model_id, target_risk_type="Performance Degradation", updated_likelihood=4, updated_magnitude=4)
        
        # Check if this update has already happened
        perf_degrad_risk = st.session_state.ai_risks_df[(st.session_state.ai_risks_df['model_id'] == credit_score_predictor_model_id) & (st.session_state.ai_risks_df['risk_type'] == "Performance Degradation")]
        
        updated_likelihood_val = 4
        updated_magnitude_val = 4

        if not perf_degrad_risk.empty and (perf_degrad_risk['likelihood_score'].iloc[0] != updated_likelihood_val or perf_degrad_risk['magnitude_score'].iloc[0] != updated_magnitude_val):
            st.markdown("Updating 'Performance Degradation' risk based on the data drift event:")
            if st.button("Formally Update Performance Degradation Risk", key="update_perf_degrad_btn"):
                update_risk_assessment_from_monitoring_st(
                    credit_score_predictor_model_id,
                    "Performance Degradation",
                    updated_likelihood_val,
                    updated_magnitude_val
                )
                st.session_state.current_step = 16 # Advance to a final summary view
                st.rerun()
        else:
            st.info("The 'Performance Degradation' risk is already updated or does not exist for the Credit Score Predictor. Proceed to summary.")
            if st.button("Proceed to Final Summary", key="proceed_final_summary_btn"):
                st.session_state.current_step = 16
                st.rerun()

        st.markdown("\nUpdated AI Risks DataFrame after monitoring feedback:")
        st.dataframe(st.session_state.ai_risks_df[st.session_state.ai_risks_df['model_id'] == credit_score_predictor_model_id])

    else:
        st.error("Credit Score Predictor model not found. Cannot update risk assessment.")
    
# Final Summary / Completion Page (Step 16, or final stage of step 15)
elif st.session_state.current_step == 16:
    st.subheader("AI Risk Management Workflow Completed!")
    st.markdown("""
        Sarah has successfully navigated the complex landscape of AI risk management. From initial system setup and model registration to identifying, assessing, mitigating, and continuously monitoring risks—she has built a comprehensive and adaptive AI risk posture for QuantFinance Bank.

        This continuous feedback loop ensures that the bank's AI models remain trustworthy and perform reliably in evolving environments.
    """)
    st.balloons()
    
    st.markdown("### Final Comprehensive AI Model Risk Register")
    if 'full_risk_register_df' in st.session_state and not st.session_state.full_risk_register_df.empty:
        st.dataframe(st.session_state.full_risk_register_df)
    else:
        get_full_risk_register_st()
        st.dataframe(st.session_state.full_risk_register_df)

    st.markdown("### Final Top Risks Overview")
    if 'top_risks_df' in st.session_state and not st.session_state.top_risks_df.empty:
        st.dataframe(st.session_state.top_risks_df)
    else:
        identify_top_risks_st(num_top_risks=3) # Default 3 for summary
        st.dataframe(st.session_state.top_risks_df)

    st.markdown("### Overall AI Risk Distribution")
    plot_risk_distribution_by_type_st()

    st.success("Sarah has established a robust AI risk management framework!")
    if st.button("Restart Workflow", key="reset_app_final"):
        st.session_state.clear()
        st.rerun()

```

