id: 6931d9ceca38c557e5169651_user_guide
summary: AI Design and Deployment Lab 6 - Clone User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuantFinance AI Model Risk Manager: Sarah's Workflow Codelab

## 1. Setting the Stage: Initializing QuantFinance Bank's AI Risk Management System
Duration: 02:00

In this lab, you will step into the shoes of **Sarah, a Senior Risk Manager at QuantFinance Bank**. Her mission is to establish a robust framework for managing the unique risks posed by Artificial Intelligence (AI) models in the financial sector. This application will guide Sarah through a practical, end-to-end workflow, mirroring real-world tasks in her job rather than just showcasing theoretical concepts.

**The Core Challenge:** QuantFinance Bank relies heavily on AI for critical operations like credit assessment and fraud detection. However, these powerful tools introduce novel risks such as algorithmic bias, adversarial attacks, and data drift. Without a systematic approach, these risks can lead to significant financial losses, reputational damage, and regulatory penalties. Sarah is tasked with building a proactive and adaptive system to identify, assess, and manage these AI-specific risks, aligning with industry best practices and regulatory frameworks.

<aside class="positive">
This foundational setup enables a systematic record of identified AI hazards and risks, which is essential for proactive risk management and effective communication among stakeholders. This aligns with the "Centralized Repository" concept from the AI RMF, emphasizing the importance of a single source of truth for all AI-related risk information.
</aside>

Sarah's first step is to lay the groundwork for a robust AI risk management system. This involves setting up the core data structures that will store information about AI models, identified risks, and their associated controls.

Click the **"Initialize AI Risk Management System"** button to set up the necessary data structures.

You will see three empty dataframes displayed, representing where all the information about AI models, risks, and controls will be stored as Sarah progresses through the workflow.

## 2. Defining Our AI Risk Taxonomy
Duration: 01:30

To ensure a consistent and comprehensive identification of AI-specific risks, Sarah needs a standardized taxonomy. This taxonomy categorizes risks across different dimensions—Data, Model, System, Human, and Organizational—providing a structured framework for assessment.

<aside class="positive">
A well-defined taxonomy helps Sarah and her team systematically identify potential AI-specific hazards, such as data drift, adversarial attacks, algorithmic bias, or privacy breaches, ensuring comprehensive coverage and facilitating communication across different departments within QuantFinance Bank. This aligns with the "Risk Taxonomy" concept in the AI RMF, ensuring that all potential vulnerabilities are considered.
</aside>

Review the displayed JSON object which outlines the AI Risk Taxonomy. This structure helps in systematically categorizing and understanding different types of AI risks.

Click the **"Acknowledge Taxonomy & Proceed to Model Registration"** button to move to the next step.

## 3. Registering a New AI Model: The Credit Score Predictor
Duration: 02:30

QuantFinance Bank is preparing to deploy a new AI-powered "Credit Score Predictor" model, which is critical for loan approvals. Sarah's immediate task is to formally register this model in the system, capturing its essential details, intended use, and initial status.

<aside class="positive">
This initial registration is a fundamental step in the AI RMF process, ensuring that every AI model under the bank's purview is documented from its inception. By registering the model early, Sarah ensures that all subsequent risk assessments and control implementations are tied to a specific, well-defined AI asset, providing clear accountability and traceability.
</aside>

Use the provided form to input the details for the "Credit Score Predictor" model. The fields will be pre-filled with common information for this type of model.

1.  **Model Name:** Credit Score Predictor
2.  **Use Case:** Automating credit risk assessment for loan applications
3.  **Description:** Machine learning model predicting creditworthiness based on financial history and demographic data.
4.  **Owner:** Retail Banking Analytics
5.  **Status:** In Development (selected by default)

Click the **"Register AI Model"** button. The application will then display the updated AI Models DataFrame, now containing the newly registered "Credit Score Predictor".

## 4. Initial Risk Identification: Potential Hazards for the Credit Score Model
Duration: 03:00

With the Credit Score Predictor registered, Sarah begins the crucial process of identifying potential AI-specific hazards. She draws upon her expertise and the bank's risk taxonomy to foresee issues that could arise from data quality, model behavior, or operational deployment.

<aside class="positive">
Sarah considers risks like "Data Quality" (poor input data leading to incorrect scores), "Algorithmic Bias" (unfair scoring for certain demographic groups), and "Performance Degradation" (the model's accuracy declining over time). This step is crucial for anticipating challenges and preventing negative impacts on customers and the bank's reputation. This proactive identification is key to mitigating future problems and aligns with Section 4.2 of the AI RMF, focusing on "Risk Register: Identification and Categorization."
</aside>

Click the following buttons, one by one, to add the initial identified risks for the "Credit Score Predictor" model:

1.  **"Add Data Quality Risk"**
2.  **"Add Algorithmic Bias Risk"**
3.  **"Add Performance Degradation Risk"**

After adding all three risks, the "Identified Risks for Credit Score Predictor" DataFrame will update. Once all three are added, a "Proceed to Quantify Risks" button will become available. Click it to continue.

## 5. Quantifying Risk: Likelihood and Magnitude Assessment
Duration: 03:30

Identifying risks is only the first step; Sarah now needs to quantify them to understand their potential impact. For each identified risk, she will assess its likelihood of occurrence and the magnitude of potential harm. This quantitative and qualitative assessment is fundamental to the AI RMF (Section 4.2), as it allows for a standardized way to prioritize risks across the bank's AI portfolio.

The core formula for this assessment is:
$$ \text{Risk} = P(\text{event}) \times M(\text{consequence}) $$
where $P(\text{event})$ represents the likelihood of a risk event occurring, and $M(\text{consequence})$ represents the severity of the impact if the event occurs. These scores will typically be qualitative (e.g., Low, Medium, High) mapped to numerical scales (e.g., 1-5).

<aside class="positive">
By quantifying risks, Sarah can assign numerical values to the qualitative assessments of likelihood and magnitude. This enables a standardized approach, allowing for objective comparison and prioritization of diverse risks.
</aside>

Use the sliders provided for each risk to assign:

*   **Likelihood (1-5):** How frequently is this risk likely to occur? (1 = Very Low, 5 = Very High)
*   **Magnitude (1-5):** How severe would the impact be if this risk materializes? (1 = Negligible, 5 = Catastrophic)

Once you've set the scores for all risks, click the **"Assign All Scores"** button. The "Updated AI Risks DataFrame with scores" will reflect your inputs. Then, click **"Proceed to Calculate Composite Scores"** to continue.

## 6. Calculating the Composite Risk Score
Duration: 02:00

With likelihood and magnitude scores assigned, Sarah can now calculate the composite risk score for each hazard. This score, derived from the formula $Risk = P(\text{event}) \times M(\text{consequence})$, provides a single, aggregated metric for each risk, allowing for easy comparison and prioritization.

<aside class="positive">
By standardizing risk quantification, Sarah ensures that all stakeholders at QuantFinance Bank can understand and compare the severity of different AI risks, guiding resource allocation for risk mitigation. A higher composite score indicates greater urgency for mitigation, helping Sarah prioritize her efforts effectively. This calculation is a direct application of the "Quantitative and Qualitative Assessment" mentioned in the AI RMF (Section 4.2).
</aside>

Click the **"Calculate All Composite Risk Scores"** button.

The "Updated AI Risks DataFrame with composite scores" will now show the calculated `composite_risk_score` for each risk.

Click **"Proceed to Integrating Adversarial Insights"** to move to the next step.

## 7. Integrating Insights from Adversarial Testing: Uncovering Robustness Risks
Duration: 03:30

QuantFinance Bank's dedicated Red-Teaming unit has just concluded an exercise targeting the Credit Score Predictor. Their findings reveal vulnerabilities to "Adversarial Attacks" – subtle manipulations of input data that can cause misclassification (e.g., making a high-risk applicant appear low-risk). Sarah must immediately integrate these critical insights into the risk register.

<aside class="positive">
By documenting these specific threats, Sarah ensures the bank can develop targeted defenses, preventing malicious actors from exploiting the model and protecting the integrity of loan decisions. This directly reflects the importance of "Adversarial Testing and Red-Teaming" (Section 2) in the AI RMF for uncovering AI-specific security vulnerabilities like "Deceptive Inputs" (2.2) and "Data Poisoning Attacks" (2.4).
</aside>

Use the form to add the adversarial risk details. The details will be pre-filled to reflect the findings:

1.  **Adversarial Attack Type:** Adversarial Attack (Evasion)
2.  **Description:** Subtle manipulation of input features to cause a misclassification of a high-risk individual as low-risk.
3.  **Likelihood (1-5):** 4
4.  **Magnitude (1-5):** 5

Click **"Add Adversarial Risk & Score"**. The "Updated AI Risks DataFrame" will display the newly added and scored risk.

Click **"Proceed to Addressing Supply Chain Risks"** to continue.

## 8. Addressing Supply Chain and Data Provenance Risks
Duration: 04:00

Beyond direct model vulnerabilities, Sarah also considers the broader "AI Supply Chain" (Section 3). A recent internal review highlighted potential data provenance issues for a separate "Fraud Detection System" and its reliance on a critical third-party feature engineering library. Sarah needs to register these "Data Provenance" (3.2) and "Third-Party Dependency" (3.3) risks.

<aside class="positive">
Ensuring the quality and origin of data, as well as vetting third-party components, helps Sarah manage cascading vulnerabilities and maintain the overall security of QuantFinance Bank's AI portfolio. This is critical for understanding risks related to data quality, integrity, and external components, concepts that are central to maintaining the trustworthiness of AI systems.
</aside>

First, the application will automatically register the "Fraud Detection System" model if it doesn't already exist.

Then, you will add two new risks for the Fraud Detection System:

**For Data Provenance Risk:**
1.  **Hazard Description:** Lack of verifiable data provenance for historical transaction data used in training, raising concerns about data integrity and potential hidden biases.
2.  **Likelihood (1-5):** 3
3.  **Magnitude (1-5):** 4

Click **"Add Data Provenance Risk"**.

**For Third-Party Dependency Risk:**
1.  **Hazard Description:** Reliance on a third-party feature engineering library with unknown vulnerabilities or insufficient documentation.
2.  **Likelihood (1-5):** 3
3.  **Magnitude (1-5):** 3

Click **"Add Third-Party Dependency Risk"**.

Observe the updated AI Models and AI Risks DataFrames. Once both risks are added, click **"Proceed to Define Controls"** to move forward.

## 9. Defining Controls and Mitigation Strategies
Duration: 03:00

Having identified and quantified several risks, Sarah's next crucial step is to define and propose specific controls to mitigate them. This involves designing defenses tailored to each identified risk, from technical measures like input sanitization to procedural controls like regular model retraining.

<aside class="positive">
By establishing clear controls, Sarah ensures that QuantFinance Bank has concrete plans to reduce the likelihood or impact of identified risks, thereby strengthening the overall resilience of its AI systems against threats like adversarial attacks and data quality issues. This directly applies the "Risk Controls and Mitigation Strategies" concept from the AI RMF (Section 4.3), emphasizing "Mapping Controls to Risks" and "Hierarchical Control Design."
</aside>

Click the following buttons, one by one, to add controls for the previously identified risks:

1.  **"Add Control for Algorithmic Bias"**: Implement fairness metrics monitoring (e.g., Equal Opportunity, Demographic Parity) and regular bias audits.
2.  **"Add Control for Adversarial Attack"**: Implement adversarial training techniques and robust input validation/sanitization mechanisms.
3.  **"Add Control for Data Provenance"**: Establish clear data lineage tracking and cryptographic hashing for all training datasets.

The "Updated AI Controls DataFrame" will show the new controls. Once all controls are added, click **"Proceed to Assign Risk Response Options"**.

## 10. Assigning Risk Response Options
Duration: 02:30

For each identified risk with its proposed controls, Sarah must now formalize the bank's "Risk Response Option" (Section 4.3). This involves deciding whether to mitigate, transfer, avoid, or accept the risk based on the severity of the residual risk (after controls) and the bank's overall risk tolerance.

<aside class="positive">
This step helps Sarah communicate to stakeholders exactly how each AI risk will be handled, ensuring alignment with the bank's broader risk appetite and regulatory requirements. This strategic decision-making is a core part of the AI RMF, ensuring that every risk has a clear management plan.
</aside>

For each control listed, use the sliders and dropdowns to assign:

*   **Effectiveness Score (1-5):** How effective is this control at reducing the risk? (1 = Very Low, 5 = Very High)
*   **Risk Response:** What is the bank's strategy for this risk? (Choose from "Mitigate", "Transfer", "Avoid", "Accept").

Common choices:
*   For bias and adversarial attack controls, choose **"Mitigate"** and an effectiveness of **4-5**.
*   For data provenance, also choose **"Mitigate"** and an effectiveness of **4**.

Once you've assigned responses for all controls, click **"Assign All Responses"**. The "Updated AI Controls DataFrame" will reflect your choices.

Then, click **"Proceed to Review Risk Register"**.

## 11. Reviewing the Comprehensive AI Model Risk Register
Duration: 02:00

At this stage, Sarah needs to review the entire AI Model Risk Register to get a holistic view of the bank's AI risk landscape. This comprehensive display, integrating models, risks, assessments, and controls, is the "Centralized Repository" described in the AI RMF (Section 4.2). It allows Sarah to verify that all necessary information is captured and interconnected.

<aside class="positive">
This unified view is essential for Sarah to present to internal audit and senior management, demonstrating transparent and systematic AI risk governance across QuantFinance Bank.
</aside>

Click the **"Generate Comprehensive AI Model Risk Register"** button.

A detailed DataFrame will be displayed, merging information from all models, risks, and controls. This is Sarah's complete risk register.

After reviewing, click **"Proceed to Analyze Top Risks"**.

## 12. Analyzing and Prioritizing High-Scoring Risks
Duration: 01:45

With a growing number of AI models and associated risks, Sarah needs an efficient way to identify and prioritize the most critical threats. Analyzing risks by their `composite_risk_score` allows her to pinpoint the highest-scoring hazards, ensuring that resources and attention are directed where they are most needed.

<aside class="positive">
This analysis helps Sarah focus on the "top risks" that pose the greatest potential harm to QuantFinance Bank, enabling proactive resource allocation and strategic risk mitigation. This aligns with the AI RMF's principle of "Risk-based" decision-making.
</aside>

You can adjust the **"Number of Top Risks to Display"** using the input field (default is 3).

Click **"Identify Top Risks"**. The application will then display a DataFrame showing the risks with the highest composite scores, sorted in descending order.

Click **"Proceed to Visualize Risk Distribution"**.

## 13. Visualizing Risk Distribution by Type
Duration: 01:30

To provide an executive overview of the bank's overall AI risk posture, Sarah wants to visualize how identified risks are distributed across the different categories defined in the AI Risk Taxonomy (e.g., Data, Model, System). This aggregation helps in understanding systemic weaknesses and informs strategic investments in risk management capabilities.

<aside class="positive">
By visualizing the distribution, Sarah can identify if a particular risk category (e.g., "Model Risk") is disproportionately high, indicating a need for more robust controls or new policies in that area. This type of visualization supports the "MEASURE" function of the AI RMF and provides an aggregated view of risks.
</aside>

Click the **"Generate Risk Distribution Chart"** button.

A bar chart will be displayed, showing the number of risks identified within each broad risk category (Data Risk, Model Risk, System Risk, etc.).

Click **"Proceed to Simulate Operational Monitoring"**.

## 14. Simulating Operational Monitoring Feedback: Detecting Data Drift
Duration: 03:00

AI risk management is not a one-time activity; it requires continuous vigilance. Sarah receives an alert from the bank's model monitoring system for the Credit Score Predictor, indicating a significant "Data Drift" (1.4.1) in the input features. This operational feedback is a critical trigger for re-evaluating the associated risks.

<aside class="positive">
This scenario demonstrates the necessity of an "Adaptive Cycle" or "outer loop" (1.4.3), where operational data constantly informs risk assessment, prompting Sarah to re-evaluate and update the risk register to maintain trust and performance. This exemplifies the "Continuous Validation" (4.5) aspect of the AI RMF.
</aside>

The form will simulate the alert with pre-filled details for "Data Drift":

1.  **Simulated Alert: Risk Type:** Data Drift (disabled as it's an alert)
2.  **Hazard Description (Data Drift):** Significant shift in demographic distribution of loan applicants causing potential model inaccuracy.
3.  **New Likelihood (1-5):** 4
4.  **New Magnitude (1-5):** 4

Click **"Simulate Data Drift & Update Risk"**. The application will either add a new "Data Drift" risk or update an existing one for the Credit Score Predictor model with the new scores.

The "Updated AI Risks DataFrame" will reflect this change. Click **"Proceed to Update Risk Assessment"**.

## 15. Updating Risk Assessment based on Monitoring Feedback
Duration: 02:00

Following the data drift alert, Sarah must now formally update the risk assessment for the "Credit Score Predictor". This involves adjusting the likelihood and/or magnitude scores for relevant risks, such as "Performance Degradation," to reflect the new operational reality.

<aside class="positive">
By continuously refining risk assessments based on real-time monitoring, Sarah ensures that the risk register remains a living document that accurately reflects the current state of AI risks at QuantFinance Bank, supporting agile risk management. This exemplifies "Continuous Validation" and "Post-Deployment Monitoring" (4.5), which are essential for maintaining the trustworthiness of adaptive AI systems.
</aside>

The data drift event directly impacts the model's "Performance Degradation" risk. You will update its scores.

Click **"Formally Update Performance Degradation Risk"**. The application will update the `likelihood_score` to `4` and the `magnitude_score` to `4` for the "Performance Degradation" risk associated with the Credit Score Predictor.

The "Updated AI Risks DataFrame" will show this final adjustment. Click **"Proceed to Final Summary"**.

## 16. AI Risk Management Workflow Completed!
Duration: 01:30

Congratulations! Sarah has successfully navigated the complex landscape of AI risk management. From initial system setup and model registration to identifying, assessing, mitigating, and continuously monitoring risks—she has built a comprehensive and adaptive AI risk posture for QuantFinance Bank.

This continuous feedback loop ensures that the bank's AI models remain trustworthy and perform reliably in evolving environments. You have now established a robust AI risk management framework!

You will see:
*   The **Final Comprehensive AI Model Risk Register**, displaying all the models, risks, and controls you've managed.
*   The **Final Top Risks Overview**, summarizing the most critical risks after all assessments and updates.
*   The **Overall AI Risk Distribution** chart, providing a high-level view of risk concentrations across categories.

Click **"Restart Workflow"** if you wish to go through the process again from the beginning.
