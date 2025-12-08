id: 6931d9ceca38c557e5169651_documentation
summary: AI Design and Deployment Lab 6 - Clone Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuantFinance AI Model Risk Manager: A Comprehensive Codelab for Developers

## 1. Welcome to QuantFinance Bank's AI Risk Management System
Duration: 0:08:00

Welcome to the QuantFinance AI Model Risk Manager Codelab! In this comprehensive guide, you'll step into the shoes of **Sarah, a Senior Risk Manager at QuantFinance Bank**. Your primary objective is to build and manage a robust framework for assessing, mitigating, and monitoring risks associated with AI models in a highly regulated financial environment. This application demonstrates a practical, end-to-end workflow inspired by real-world AI Risk Management Frameworks (AI RMFs).

**Why is this application important?**
The rapid adoption of AI in critical sectors like finance introduces novel and complex risks. Failures in AI systems can lead to significant financial losses, reputational damage, regulatory non-compliance, and adverse impacts on individuals. This application provides a hands-on experience in addressing these challenges by:
*   **Centralizing Risk Information:** Establishing a single source of truth for all AI models, their risks, and controls.
*   **Standardizing Assessment:** Applying consistent methodologies for identifying and quantifying AI-specific risks.
*   **Enabling Proactive Mitigation:** Designing and implementing controls to address identified vulnerabilities.
*   **Facilitating Continuous Monitoring:** Adapting risk assessments based on operational feedback and evolving threats.
*   **Ensuring Compliance & Trust:** Demonstrating a structured approach to managing AI risks, crucial for regulatory adherence and stakeholder trust.

By following this codelab, developers will gain a deep understanding of the functional components of an AI risk management system and how they integrate to support a dynamic workflow. You'll see how Streamlit can be used to create interactive, data-driven applications for complex enterprise workflows.

### Application Architecture Overview

The application is structured into three main parts:

1.  **`app.py` (Main Orchestrator):** This is the heart of the Streamlit application. It sets up the page configuration, initializes the session state, provides sidebar navigation, and dynamically loads content from different `application_pages`.
2.  **`utils.py` (Core Business Logic):** This file contains all the backend functions responsible for data manipulation. It manages the creation, updating, and querying of AI models, risks, and controls stored as Pandas DataFrames within Streamlit's session state. It also defines the AI Risk Taxonomy.
3.  **`application_pages/` (UI Components for Each Step):** Each `.py` file in this directory represents a distinct step in the AI risk management workflow. These files contain Streamlit UI elements (text, buttons, sliders, dataframes) and call functions from `utils.py` to perform specific actions.

All persistent data (AI models, risks, controls, and counters) is stored in `st.session_state`, ensuring that user interactions across different pages and reruns are remembered.

<aside class="positive">
<b>Streamlit's `st.session_state`</b> is crucial here. It allows the application to maintain state across user interactions, which is fundamental for multi-step workflows like this risk management system. Without it, every interaction would reset the application's data.
</aside>

**Visualizing the Application Flow:**

```mermaid
graph TD
    A[User (Browser)] -- Interacts with --> B(Streamlit UI)
    B -- Calls & Renders --> C(app.py)
    C -- Orchestrates & Manages Step-by-Step UI --> I(application_pages/*.py)
    C -- Initializes & Manages Session State --> D(st.session_state)
    I -- Invokes Business Logic --> J(utils.py)
    J -- Reads/Writes Persistent Data --> D
    D -- Stores DataFrames for --> E[AI Models]
    D -- Stores DataFrames for --> F[AI Risks]
    D -- Stores DataFrames for --> G[AI Controls]
    D -- Stores Dictionary for --> H[AI Risk Taxonomy]

    subgraph Application Structure
        C
        I
        J
    end
    subgraph Data Management
        D
        E
        F
        G
        H
    end
```

### Initializing the System

Sarah's first action is to set up the core data structures. This aligns with establishing a "Centralized Repository" as described in leading AI RMFs, providing a single, transparent record of all AI-related assets and risks.

Let's look at the initialization logic in `utils.py`:

```python
# utils.py
def initialize_session_state():
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
    # ... other initializations
```

The `initialize_session_state` function ensures that if the DataFrames and counters don't exist in `st.session_state`, they are created with empty structures. This is called once at the start of `app.py`. The `initialize_risk_management_system_st` function, called from `page_1_welcome.py`, provides a way to explicitly reset these DataFrames, simulating a fresh start.

**Your Action:**
On the Streamlit application, click the "**Initialize AI Risk Management System**" button. Observe that the "AI Models Register", "AI Risks Register", and "AI Controls Register" are displayed as empty DataFrames.

<aside class="positive">
Notice the use of `st.rerun()` after actions that change `st.session_state.current_step`. This forces Streamlit to re-execute the script, reflecting the new state and navigating to the next page. This pattern is common in Streamlit for explicit state-driven navigation.
</aside>

## 2. Defining Our AI Risk Taxonomy
Duration: 0:03:00

To ensure a consistent and comprehensive identification of AI-specific risks, Sarah needs a standardized taxonomy. This taxonomy categorizes risks across different dimensions (e.g., Data, Model, System, Human, Organizational) and provides a structured framework for assessment. This aligns with the "Risk Taxonomy" concept in the AI RMF, ensuring that all potential vulnerabilities are considered.

A well-defined taxonomy helps Sarah and her team systematically identify potential AI-specific hazards, such as data drift, adversarial attacks, algorithmic bias, or privacy breaches, ensuring comprehensive coverage and facilitating communication across different departments within QuantFinance Bank.

The taxonomy is stored in `st.session_state.AI_RISK_TAXONOMY` and is defined in `utils.py`:

```python
# utils.py snippet
if 'AI_RISK_TAXONOMY' not in st.session_state:
    st.session_state.AI_RISK_TAXONOMY = {
        "Data Risk": ["Data Quality", "Data Privacy", "Data Drift", "Data Poisoning", "Data Bias", "Data Provenance"],
        "Model Risk": ["Algorithmic Bias", "Fairness", "Explainability", "Robustness", "Performance Degradation", "Adversarial Attacks", "Concept Drift", "Model Interpretability"],
        "System Risk": ["Security Vulnerability", "Integration Issues", "Infrastructure Failure", "Access Control"],
        "Human Risk": ["Operator Error", "Misuse", "Lack of Oversight", "Ethical Misalignment"],
        "Organizational Risk": ["Regulatory Non-Compliance", "Reputational Damage", "Lack of Governance", "Third-Party Dependency"]
    }
```

This structured dictionary allows for easy categorization and ensures that all team members use the same language when discussing AI risks.

**Your Action:**
Review the displayed AI Risk Taxonomy. This structure helps in systematically identifying hazards.
Click "**Acknowledge Taxonomy & Proceed to Model Registration**" to move to the next step.

## 3. Registering a New AI Model: The Credit Score Predictor
Duration: 0:05:00

QuantFinance Bank is preparing to deploy a new AI-powered "Credit Score Predictor" model, which is critical for loan approvals. Sarah's immediate task is to formally register this model in the system, capturing its essential details, intended use, and initial status. This initial registration is a fundamental step in the AI RMF process, ensuring that every AI model under the bank's purview is documented from its inception.

By registering the model early, Sarah ensures that all subsequent risk assessments and control implementations are tied to a specific, well-defined AI asset, providing clear accountability and traceability.

The `add_ai_model_st` function in `utils.py` handles adding new models:

```python
# utils.py
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
    return st.session_state.model_id_counter
```

This function increments a counter for `model_id` (a simple auto-incrementing ID for demonstration), creates a new DataFrame row from the provided details, and concatenates it to the `ai_models_df` in session state.

**Your Action:**
On the Streamlit application, fill in the details for the "Credit Score Predictor" (pre-filled by the application) and click "**Register AI Model**". Observe the "AI Models Register" updating with the new entry. A specific model ID (`credit_score_predictor_model_id`) is stored in session state for later use.

Click "**Proceed to Initial Risk Identification**".

## 4. Initial Risk Identification: Potential Hazards for the Credit Score Model
Duration: 0:06:00

With the Credit Score Predictor registered, Sarah begins the crucial process of identifying potential AI-specific hazards. She draws upon her expertise and the bank's risk taxonomy to foresee issues that could arise from data quality, model behavior, or operational deployment. This proactive identification is key to mitigating future problems and aligns with Section 4.2 of the AI RMF, focusing on "Risk Register: Identification and Categorization."

Sarah considers risks like "Data Quality" (poor input data leading to incorrect scores), "Algorithmic Bias" (unfair scoring for certain demographic groups), and "Performance Degradation" (the model's accuracy declining over time). This step is crucial for anticipating challenges and preventing negative impacts on customers and the bank's reputation.

The `add_ai_risk_st` function in `utils.py` adds new risks:

```python
# utils.py
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
```

Similar to adding models, this function increments a `risk_id_counter`, creates a new risk entry, and appends it to `ai_risks_df`. It takes the `model_id` as a foreign key, linking the risk to a specific model.

**Your Action:**
On the Streamlit application, Sarah will identify three initial risks for the "Credit Score Predictor".
Check the checkboxes for the following risks:
*   **Data Quality**: Poor or incomplete historical data leading to inaccurate credit scores.
*   **Algorithmic Bias**: Model exhibits biased decision-making against certain demographic groups.
*   **Performance Degradation**: Model accuracy degrades over time due to changes in credit behavior patterns.

Click "**Confirm Added Risks**". Observe the "AI Risks Register" updating with these new entries.

Click "**Proceed to Quantify Risks**".

## 5. Quantifying Risk: Likelihood and Magnitude Assessment
Duration: 0:07:00

Identifying risks is only the first step; Sarah now needs to quantify them to understand their potential impact. For each identified risk, she will assess its likelihood of occurrence ($P(\text{event}))$ and the magnitude of potential harm ($M(\text{consequence}))$. This quantitative and qualitative assessment is fundamental to the AI RMF (Section 4.2), as it allows for a standardized way to prioritize risks across the bank's AI portfolio.

The core formula for this assessment is:
$$ \text{Risk} = P(\text{event}) \times M(\text{consequence}) $$
where $P(\text{event})$ represents the likelihood of a risk event occurring, and $M(\text{consequence})$ represents the severity of the impact if the event occurs. These scores will typically be qualitative (e.g., Low, Medium, High) mapped to numerical scales (e.g., 1-5).

The `assign_risk_scores_st` function in `utils.py` updates the risk DataFrame:

```python
# utils.py
def assign_risk_scores_st(risk_id, likelihood, magnitude):
    if risk_id in st.session_state.ai_risks_df['risk_id'].values:
        st.session_state.ai_risks_df.loc[st.session_state.ai_risks_df['risk_id'] == risk_id, 'likelihood_score'] = likelihood
        st.session_state.ai_risks_df.loc[st.session_state.ai_risks_df['risk_id'] == risk_id, 'magnitude_score'] = magnitude
        st.info(f"Assigned likelihood ({likelihood}) and magnitude ({magnitude}) scores for risk ID {risk_id}.")
    else:
        st.warning(f"Risk ID {risk_id} not found.")
```

This function uses Pandas' `.loc` accessor to efficiently update the `likelihood_score` and `magnitude_score` for a specific `risk_id`.

**Your Action:**
On the Streamlit application, use the sliders to assign Likelihood and Magnitude scores (1-5) for each of the identified risks. You can use the default values or adjust them as you see fit.
*   **Data Quality:** (Example: Likelihood 3, Magnitude 4)
*   **Algorithmic Bias:** (Example: Likelihood 3, Magnitude 5)
*   **Performance Degradation:** (Example: Likelihood 4, Magnitude 3)

Click "**Assign All Scores**". Observe the "AI Risks Register" updating with the assigned scores.

Click "**Proceed to Calculate Composite Scores**".

## 6. Calculating the Composite Risk Score
Duration: 0:04:00

With likelihood and magnitude scores assigned, Sarah can now calculate the composite risk score for each hazard. This score, derived from the formula $\text{Risk} = P(\text{event}) \times M(\text{consequence})$, provides a single, aggregated metric for each risk, allowing for easy comparison and prioritization. This calculation is a direct application of the "Quantitative and Qualitative Assessment" mentioned in the AI RMF (Section 4.2).

By standardizing risk quantification, Sarah ensures that all stakeholders at QuantFinance Bank can understand and compare the severity of different AI risks, guiding resource allocation for risk mitigation.

The `calculate_composite_risk_score_st` function in `utils.py` performs this calculation:

```python
# utils.py
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
```

This function retrieves the likelihood and magnitude for a given `risk_id`, performs the multiplication, and updates the `composite_risk_score` column.

**Your Action:**
On the Streamlit application, click "**Calculate All Composite Risk Scores**". Observe the "AI Risks Register" updating with the new `composite_risk_score` values.

Click "**Proceed to Integrating Adversarial Insights**".

## 7. Integrating Insights from Adversarial Testing: Uncovering Robustness Risks
Duration: 0:05:00

QuantFinance Bank's dedicated Red-Teaming unit has just concluded an exercise targeting the Credit Score Predictor. Their findings reveal vulnerabilities to "Adversarial Attacks" – subtle manipulations of input data that can cause misclassification (e.g., making a high-risk applicant appear low-risk). Sarah must immediately integrate these critical insights into the risk register. This directly reflects the importance of "Adversarial Testing and Red-Teaming" (Section 2) in the AI RMF for uncovering AI-specific security vulnerabilities like "Deceptive Inputs" (2.2) and "Data Poisoning Attacks" (2.4).

By documenting these specific threats, Sarah ensures the bank can develop targeted defenses, preventing malicious actors from exploiting the model and protecting the integrity of loan decisions.

The `add_adversarial_risk_st` function in `utils.py` streamlines the process of adding and scoring this specific type of risk:

```python
# utils.py
def add_adversarial_risk_st(model_id, attack_type, description, likelihood, magnitude):
    risk_type = "Model Risk" # Adversarial attacks fall under Model Risk
    new_risk_id = add_ai_risk_st(model_id, risk_type, f"{attack_type}: {description}")
    assign_risk_scores_st(new_risk_id, likelihood, magnitude)
    calculate_composite_risk_score_st(new_risk_id)
    st.success(f"Adversarial risk '{attack_type}' (ID: {new_risk_id}) added and scored for model {model_id}.")
    return new_risk_id
```

This utility function wraps the `add_ai_risk_st`, `assign_risk_scores_st`, and `calculate_composite_risk_score_st` functions to simplify the addition of a complete risk entry with scores.

**Your Action:**
On the Streamlit application, the details for the adversarial risk are pre-filled. Click "**Add Adversarial Risk & Score**". Observe the "AI Risks Register" updating with the new "Adversarial Attack" risk and its calculated composite score.

Click "**Proceed to Supply Chain & Data Provenance Risks**".

## 8. Addressing Supply Chain and Data Provenance Risks
Duration: 0:08:00

Beyond direct model vulnerabilities, Sarah also considers the broader "AI Supply Chain" (Section 3). A recent internal review highlighted potential data provenance issues for a separate "Fraud Detection System" and its reliance on a critical third-party feature engineering library. Sarah needs to register these "Data Provenance" (3.2) and "Third-Party Dependency" (3.3) risks. This is critical for understanding risks related to data quality, integrity, and external components, concepts that are central to maintaining the trustworthiness of AI systems.

Ensuring the quality and origin of data, as well as vetting third-party components, helps Sarah manage cascading vulnerabilities and maintain the overall security of QuantFinance Bank's AI portfolio.

The `add_supply_chain_risk_st` function in `utils.py` handles adding models (if they don't exist) and their associated supply chain risks:

```python
# utils.py
def add_supply_chain_risk_st(model_name, model_use_case, model_description, model_owner, model_status, risk_type, hazard_description, likelihood, magnitude):
    existing_model = st.session_state.ai_models_df[st.session_state.ai_models_df['model_name'] == model_name]
    if not existing_model.empty:
        model_id = existing_model['model_id'].iloc[0]
        st.info(f"Model '{model_name}' (ID: {int(model_id)}) already exists. Using existing model_id.")
    else:
        model_id = add_ai_model_st(model_name, model_use_case, model_description, model_owner, model_status)

    new_risk_id = add_ai_risk_st(model_id, risk_type, hazard_description)
    assign_risk_scores_st(new_risk_id, likelihood, magnitude)
    calculate_composite_risk_score_st(new_risk_id)
    st.success(f"Supply chain/data provenance risk '{hazard_description}' (ID: {new_risk_id}) added and scored for model {model_id}.")
    return model_id, new_risk_id
```

This function first checks if the `Fraud Detection System` model already exists. If not, it registers it using `add_ai_model_st`. Then, it adds the specific risk, assigns scores, and calculates the composite score.

**Your Action:**
The `Fraud Detection System` model is automatically registered if it doesn't exist.
1.  Click "**Add Data Provenance Risk**" to add the risk related to data integrity and origin.
2.  Click "**Add Third-Party Dependency Risk**" to add the risk related to external components.

Observe the "AI Models Register" and "AI Risks Register" updating with the new model and its associated supply chain risks.

Click "**Proceed to Define Controls**".

## 9. Defining Controls & Mitigation Strategies
Duration: 0:07:00

Having identified and quantified several risks, Sarah's next crucial step is to define and propose specific controls to mitigate them. This involves designing defenses tailored to each identified risk, from technical measures like input sanitization to procedural controls like regular model retraining. This directly applies the "Risk Controls and Mitigation Strategies" concept from the AI RMF (Section 4.3), emphasizing "Mapping Controls to Risks" and "Hierarchical Control Design."

By establishing clear controls, Sarah ensures that QuantFinance Bank has concrete plans to reduce the likelihood or impact of identified risks, thereby strengthening the overall resilience of its AI systems against threats like adversarial attacks and data quality issues.

The `add_ai_control_st` function in `utils.py` adds new control entries:

```python
# utils.py
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
```

This function creates a new control entry, linking it to a `risk_id` and adds it to the `ai_controls_df`.

**Your Action:**
Sarah needs to define controls for "Algorithmic Bias", "Adversarial Attack", and "Data Provenance" risks.
Click the buttons:
1.  "**Add Control for Algorithmic Bias**"
2.  "**Add Control for Adversarial Attack**"
3.  "**Add Control for Data Provenance**"

Observe the "AI Controls Register" updating with these new controls.

Click "**Proceed to Assign Risk Response Options**".

## 10. Assigning Risk Response Options
Duration: 0:06:00

For each identified risk with its proposed controls, Sarah must now formalize the bank's "Risk Response Option" (Section 4.3). This involves deciding whether to mitigate, transfer, avoid, or accept the risk based on the severity of the residual risk (after controls) and the bank's overall risk tolerance. This strategic decision-making is a core part of the AI RMF, ensuring that every risk has a clear management plan.

This step helps Sarah communicate to stakeholders exactly how each AI risk will be handled, ensuring alignment with the bank's broader risk appetite and regulatory requirements.

The `assign_risk_response_st` function in `utils.py` updates the control DataFrame:

```python
# utils.py
def assign_risk_response_st(control_id, effectiveness_score, risk_response):
    if control_id in st.session_state.ai_controls_df['control_id'].values:
        st.session_state.ai_controls_df.loc[st.session_state.ai_controls_df['control_id'] == control_id, 'effectiveness_score'] = effectiveness_score
        st.session_state.ai_controls_df.loc[st.session_state.ai_controls_df['control_id'] == control_id, 'risk_response'] = risk_response
        st.info(f"Assigned effectiveness score ({effectiveness_score}) and risk response ('{risk_response}') for control ID {control_id}.")
    else:
        st.warning(f"Control ID {control_id} not found.")
```

This function updates the `effectiveness_score` and `risk_response` for a given `control_id`.

**Your Action:**
On the Streamlit application, for each control, specify its expected effectiveness (1=Ineffective, 5=Highly Effective) and select the appropriate risk response. You can use the default values or adjust them.
*   **Algorithmic Bias Control:** (Example: Effectiveness 4, Response "Mitigate")
*   **Adversarial Attack Control:** (Example: Effectiveness 5, Response "Mitigate")
*   **Data Provenance Control:** (Example: Effectiveness 4, Response "Mitigate")

Click "**Assign All Responses**". Observe the "AI Controls Register" updating with the assigned effectiveness scores and risk responses.

Click "**Proceed to Review Risk Register**".

## 11. Reviewing the Comprehensive AI Model Risk Register
Duration: 0:04:00

At this stage, Sarah needs to review the entire AI Model Risk Register to get a holistic view of the bank's AI risk landscape. This comprehensive display, integrating models, risks, assessments, and controls, is the "Centralized Repository" described in the AI RMF (Section 4.2). It allows Sarah to verify that all necessary information is captured and interconnected.

This unified view is essential for Sarah to present to internal audit and senior management, demonstrating transparent and systematic AI risk governance across QuantFinance Bank.

The `get_full_risk_register_st` function in `utils.py` performs the DataFrame merges:

```python
# utils.py
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
```

This function uses Pandas `merge` operations to combine the `ai_models_df`, `ai_risks_df`, and `ai_controls_df` into a single, comprehensive DataFrame. This consolidated view is then stored in `st.session_state.full_risk_register_df`.

**Your Action:**
Click "**Generate Comprehensive AI Model Risk Register**". Observe the display of the merged DataFrame, showing all models, their identified risks, and the associated controls and responses.

Click "**Proceed to Analyze Top Risks**".

## 12. Analyzing and Prioritizing High-Scoring Risks
Duration: 0:04:00

With a growing number of AI models and associated risks, Sarah needs an efficient way to identify and prioritize the most critical threats. Analyzing risks by their `composite_risk_score` allows her to pinpoint the highest-scoring hazards, ensuring that resources and attention are directed where they are most needed. This aligns with the AI RMF's principle of "Risk-based" decision-making.

This analysis helps Sarah focus on the "top risks" that pose the greatest potential harm to QuantFinance Bank, enabling proactive resource allocation and strategic risk mitigation.

The `identify_top_risks_st` function in `utils.py` performs the sorting and selection:

```python
# utils.py
def identify_top_risks_st(num_top_risks=5):
    if 'full_risk_register_df' not in st.session_state or st.session_state.full_risk_register_df.empty:
        get_full_risk_register_st() # Ensure full register is generated if not present
    if not st.session_state.full_risk_register_df.empty:
        df_sorted = st.session_state.full_risk_register_df.sort_values(by='composite_risk_score', ascending=False, na_position='last')
        top_risks = df_sorted.head(num_top_risks)
        st.session_state.top_risks_df = top_risks
        st.success(f"Top {num_top_risks} risks identified.")
    else:
        st.warning("Full risk register is empty. Cannot identify top risks.")
```

This function first ensures the full risk register is available, then sorts it by `composite_risk_score` in descending order, and selects the top `num_top_risks`.

**Your Action:**
Adjust the "Number of Top Risks to Display" slider (e.g., to 3). Click "**Identify Top Risks**". Observe the DataFrame displaying the highest-scoring risks.

Click "**Proceed to Visualize Risk Distribution**".

## 13. Visualizing Risk Distribution by Type
Duration: 0:05:00

To provide an executive overview of the bank's overall AI risk posture, Sarah wants to visualize how identified risks are distributed across the different categories defined in the AI Risk Taxonomy (e.g., Data, Model, System). This aggregation helps in understanding systemic weaknesses and informs strategic investments in risk management capabilities. This type of visualization supports the "MEASURE" function of the AI RMF and provides an aggregated view of risks.

By visualizing the distribution, Sarah can identify if a particular risk category (e.g., "Model Risk") is disproportionately high, indicating a need for more robust controls or new policies in that area.

The `plot_risk_distribution_by_type_st` function in `utils.py` generates this plot:

```python
# utils.py
def plot_risk_distribution_by_type_st():
    if not st.session_state.ai_risks_df.empty:
        category_map = {}
        for category, types in st.session_state.AI_RISK_TAXONOMY.items():
            for t in types:
                category_map[t] = category
        
        temp_risks_df = st.session_state.ai_risks_df.copy()
        temp_risks_df['broad_risk_category'] = temp_risks_df['risk_type'].map(category_map)
        temp_risks_df = temp_risks_df.dropna(subset=['broad_risk_category'])
            
        if not temp_risks_df.empty:
            risk_counts = temp_risks_df['broad_risk_category'].value_counts().reset_index()
            risk_counts.columns = ['Broad Risk Category', 'Number of Risks']

            fig, ax = plt.subplots(figsize=(10, 6))
            sns.barplot(x='Broad Risk Category', y='Number of Risks', data=risk_counts, palette='viridis', ax=ax)
            ax.set_title('Distribution of AI Risks by Broad Category')
            ax.set_xlabel('Broad Risk Category')
            ax.set_ylabel('Number of Risks')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            st.pyplot(fig)
            plt.close(fig) # Important for Streamlit to prevent plots from accumulating
            st.caption("This visualization provides Sarah with a high-level understanding of where QuantFinance Bank's AI risks are concentrated.")
        # ... error handling
    # ... error handling
```

This function maps specific risk types back to their broader categories defined in `AI_RISK_TAXONOMY`, counts the occurrences, and then uses `matplotlib` and `seaborn` to create a bar chart. `st.pyplot(fig)` is used to display the `matplotlib` figure in Streamlit.

**Your Action:**
Click "**Generate Risk Distribution Chart**". Observe the bar chart showing the distribution of identified risks across broad categories (Data Risk, Model Risk, Organizational Risk).

Click "**Proceed to Simulate Operational Monitoring**".

## 14. Simulating Operational Monitoring Feedback: Detecting Data Drift
Duration: 0:06:00

AI risk management is not a one-time activity; it requires continuous vigilance. Sarah receives an alert from the bank's model monitoring system for the Credit Score Predictor, indicating a significant "Data Drift" (1.4.1) in the input features. This operational feedback is a critical trigger for re-evaluating the associated risks and exemplifies the "Continuous Validation" (4.5) aspect of the AI RMF.

This scenario demonstrates the necessity of an "Adaptive Cycle" or "outer loop" (1.4.3), where operational data constantly informs risk assessment, prompting Sarah to re-evaluate and update the risk register to maintain trust and performance.

The `simulate_data_drift_alert_st` function in `utils.py` handles this simulation:

```python
# utils.py
def simulate_data_drift_alert_st(model_id, risk_type_to_update, hazard_description_if_new, new_likelihood, new_magnitude):
    existing_risk_row = st.session_state.ai_risks_df[(st.session_state.ai_risks_df['model_id'] == model_id) & (st.session_state.ai_risks_df['risk_type'] == risk_type_to_update)]

    if not existing_risk_row.empty:
        risk_id = existing_risk_row['risk_id'].iloc[0]
        st.info(f"Updating existing risk ID {int(risk_id)} for '{risk_type_to_update}' (model ID: {int(model_id)}).")
        assign_risk_scores_st(risk_id, new_likelihood, new_magnitude)
        calculate_composite_risk_score_st(risk_id)
    else:
        st.info(f"Adding new risk '{risk_type_to_update}' for model ID: {int(model_id)}.")
        risk_id = add_ai_risk_st(model_id, risk_type_to_update, hazard_description_if_new, new_likelihood, new_magnitude)
        calculate_composite_risk_score_st(risk_id)
    st.warning("Data drift alert processed and risk assessment updated to reflect the new operational reality.")
    return risk_id
```

This function simulates a real-time monitoring alert. It checks if a "Data Drift" risk already exists for the Credit Score Predictor. If so, it updates its scores; otherwise, it adds it as a new risk.

**Your Action:**
On the Streamlit application, the details for the simulated data drift are pre-filled. Click "**Simulate Data Drift & Update Risk**". Observe the "AI Risks Register" updating to include (or update) the "Data Drift" risk for the Credit Score Predictor.

Click "**Proceed to Update Risk Assessment**".

## 15. Updating Risk Assessment based on Monitoring Feedback
Duration: 0:05:00

Following the data drift alert, Sarah must now formally update the risk assessment for the "Credit Score Predictor". This involves adjusting the likelihood and/or magnitude scores for relevant risks, such as "Performance Degradation" or the newly identified "Data Drift," to reflect the new operational reality. This exemplifies "Continuous Validation" and "Post-Deployment Monitoring" (4.5), which are essential for maintaining the trustworthiness of adaptive AI systems.

By continuously refining risk assessments based on real-time monitoring, Sarah ensures that the risk register remains a living document that accurately reflects the current state of AI risks at QuantFinance Bank, supporting agile risk management.

The `update_risk_assessment_from_monitoring_st` function in `utils.py` handles this formal update:

```python
# utils.py
def update_risk_assessment_from_monitoring_st(model_id, target_risk_type, updated_likelihood, updated_magnitude):
    target_risk_row = st.session_state.ai_risks_df[(st.session_state.ai_risks_df['model_id'] == model_id) & (st.session_state.ai_risks_df['risk_type'] == target_risk_type)]

    if not target_risk_row.empty:
        risk_id = target_risk_row['risk_id'].iloc[0]
        st.info(f"Updating risk assessment for risk ID {int(risk_id)} ('{target_risk_type}') for model ID {int(model_id)}.")
        assign_risk_scores_st(risk_id, updated_likelihood, updated_magnitude)
        calculate_composite_risk_score_st(risk_id)
    else:
        st.warning(f"Risk type '{target_risk_type}' not found for model ID {int(model_id)}. No update performed.")
    st.success("Risk assessment formally updated based on monitoring feedback.")
```

This function specifically targets an existing risk (in this case, "Performance Degradation") and updates its scores, then recalculates its composite risk score.

**Your Action:**
On the Streamlit application, click "**Formally Update Performance Degradation Risk**". Observe the "AI Risks Register" updating the `likelihood_score`, `magnitude_score`, and `composite_risk_score` for "Performance Degradation."

Click "**Proceed to Final Summary**".

## 16. Workflow Summary
Duration: 0:03:00

Congratulations! Sarah has successfully navigated the complex landscape of AI risk management. From initial system setup and model registration to identifying, assessing, mitigating, and continuously monitoring risks—she has built a comprehensive and adaptive AI risk posture for QuantFinance Bank.

This continuous feedback loop ensures that the bank's AI models remain trustworthy and perform reliably in evolving environments.

This final page consolidates the results of the entire workflow, displaying the final comprehensive risk register, the top risks, and the overall risk distribution.

The `restart_workflow` function in `utils.py` provides a way to reset the entire application:

```python
# utils.py
def restart_workflow():
    st.session_state.clear()
    initialize_session_state() # Re-initialize after clearing
    st.success("Workflow has been restarted.")
    st.rerun()
```

This function is critical for allowing users to re-run the entire simulation from a clean slate. It clears all data from `st.session_state` and then re-initializes it, effectively resetting the application.

**Your Action:**
Review the final comprehensive risk register, the updated top risks, and the overall risk distribution. You have successfully completed the codelab!

You can click "**Restart Workflow**" to reset the application and go through the steps again if you wish.
