id: 6931d9ceca38c557e5169651_user_guide
summary: AI Design and Deployment Lab 6 - Clone User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuantFinance AI Model Risk Manager: A Codelab for Sarah

## Introduction: Embarking on AI Risk Management at QuantFinance Bank

Welcome to this interactive codelab! You will step into the shoes of **Sarah, a Senior Risk Manager at QuantFinance Bank**. In today's rapidly evolving financial landscape, AI models are becoming indispensable, but they also introduce unique and complex risks. Your mission in this codelab is to establish and navigate a robust framework for managing these AI-specific risks, ensuring the trustworthiness, safety, and regulatory compliance of QuantFinance Bank's AI initiatives.

This codelab will guide you through a realistic, story-driven workflow, mirroring the challenges and decisions faced in a dynamic AI environment. You will actively engage with core principles of AI model risk management, from setting up a centralized risk register and defining a comprehensive risk taxonomy, to formally registering new AI models, identifying and quantifying risks, designing mitigation strategies, and adapting to real-time operational feedback.

By the end of this journey, you will have a practical understanding of how to manage AI risks effectively, ensuring responsible AI deployment within a critical financial institution.

## 1. Setting the Stage: Initializing QuantFinance Bank's AI Risk Management System
Duration: 01:00

Sarah's first crucial task is to lay the groundwork for a robust AI risk management system. This involves setting up the core data structures that will store information about AI models, identified risks, and their associated controls. This **centralized repository** is crucial for maintaining a transparent and comprehensive overview of all AI-related risks across QuantFinance Bank, aligning with fundamental concepts from leading AI Risk Management Frameworks (RMFs).

This foundational setup enables a systematic record of identified AI hazards and risks, which is essential for proactive risk management and effective communication among stakeholders.

### Your Task:

Click the "Initialize AI Risk Management System" button to set up the necessary registers.

<aside class="positive">
This step is fundamental. Think of it like preparing a new filing system before you start collecting documents. Without this initial setup, Sarah would have no structured way to track her AI models and their associated risks.
</aside>

Once initialized, you will see the initially empty dataframes for AI Models, AI Risks, and AI Controls, ready to be populated.

## 2. Defining Our AI Risk Taxonomy
Duration: 01:00

To ensure consistent and comprehensive identification of AI-specific risks, Sarah needs a standardized **risk taxonomy**. This taxonomy categorizes risks across different dimensions—Data, Model, System, Human, and Organizational—providing a structured framework for assessment. This aligns with the "Risk Taxonomy" concept in AI RMFs, ensuring that all potential vulnerabilities are considered.

A well-defined taxonomy helps Sarah and her team systematically identify potential AI-specific hazards, such as data drift, adversarial attacks, algorithmic bias, or privacy breaches. This structured approach ensures comprehensive coverage and facilitates communication across different departments within QuantFinance Bank.

### Your Task:

Review the displayed AI Risk Taxonomy, which categorizes risks into broad areas with specific types. This JSON structure shows how different kinds of risks (e.g., Data Quality, Algorithmic Bias) fall under larger categories (e.g., Data Risk, Model Risk).

<aside class="info">
This taxonomy will serve as a checklist and classification system for Sarah and her team. By having predefined categories like 'Data Risk' and 'Model Risk' with specific types, Sarah ensures no critical area of AI risk is overlooked when assessing new models. This structured approach underpins the systematic identification required for effective risk management.
</aside>

Once you've reviewed the taxonomy, click "Acknowledge Taxonomy & Proceed to Model Registration".

## 3. Registering a New AI Model: The Credit Score Predictor
Duration: 01:30

QuantFinance Bank is preparing to deploy a new AI-powered "**Credit Score Predictor**" model, which is critical for loan approvals. Sarah's immediate task is to formally register this model in the system, capturing its essential details, intended use, and initial status. This initial registration is a fundamental step in any AI RMF process, ensuring that every AI model under the bank's purview is documented from its inception.

By registering the model early, Sarah ensures that all subsequent risk assessments and control implementations are tied to a specific, well-defined AI asset, providing clear accountability and traceability.

### Your Task:

The form will be pre-filled with details for the "Credit Score Predictor" model. Review the information and then click "Register AI Model".

<aside class="positive">
<b>Centralized documentation</b> for AI models is key. This ensures that from the moment an AI model is conceived, its purpose, ownership, and status are formally recorded, providing a single source of truth for all stakeholders.
</aside>

After registration, observe how the "Credit Score Predictor" model is added to the `AI Models Register` dataframe. Then, click "Proceed to Initial Risk Identification".

## 4. Initial Risk Identification: Potential Hazards for the Credit Score Model
Duration: 01:30

With the Credit Score Predictor registered, Sarah begins the crucial process of identifying potential AI-specific hazards. She draws upon her expertise and the bank's risk taxonomy to foresee issues that could arise from data quality, model behavior, or operational deployment. This proactive identification is key to mitigating future problems and aligns with the "Risk Register: Identification and Categorization" concepts in AI RMFs.

Sarah considers risks like "Data Quality" (poor input data leading to incorrect scores), "Algorithmic Bias" (unfair scoring for certain demographic groups), and "Performance Degradation" (the model's accuracy declining over time). This step is crucial for anticipating challenges and preventing negative impacts on customers and the bank's reputation.

### Your Task:

You will see several checkboxes representing common risks for a credit scoring model. Select each checkbox to add the specified risks to the register. After selecting all of them, click "Confirm Added Risks".

<aside class="info">
Identifying risks early allows for proactive planning. By cataloging potential issues like bias or data quality problems now, Sarah can ensure that mitigation strategies are considered even before the model goes into full production.
</aside>

Observe the `AI Risks Register` dataframe update with the newly identified hazards for the "Credit Score Predictor" model. Then, click "Proceed to Quantify Risks".

## 5. Quantifying Risk: Likelihood and Magnitude Assessment
Duration: 02:00

Identifying risks is only the first step; Sarah now needs to quantify them to understand their potential impact. For each identified risk, she will assess its **likelihood of occurrence** ($P(\text{event}))$ and the **magnitude of potential harm** ($M(\text{consequence}))$. This quantitative and qualitative assessment is fundamental to the AI RMF, as it allows for a standardized way to prioritize risks across the bank's AI portfolio.

The core conceptual formula for this assessment is:
$$ \text{Risk} = P(\text{event}) \times M(\text{consequence}) $$
where $P(\text{event})$ represents the likelihood of a risk event occurring (e.g., how often data drift might happen), and $M(\text{consequence})$ represents the severity of the impact if the event occurs (e.g., financial loss or reputational damage). These scores will typically be qualitative (e.g., Low, Medium, High) mapped to numerical scales (e.g., 1-5).

### Your Task:

For each listed risk, use the sliders to assign a `Likelihood Score` (1=Rarely, 5=Frequently) and a `Magnitude Score` (1=Minor, 5=Catastrophic). After setting scores for all risks, click "Assign All Scores".

<aside class="positive">
<b>Standardized scoring</b> is vital. By giving numerical values to likelihood and magnitude, Sarah can objectively compare different risks, making it easier to decide which ones need the most immediate attention.
</aside>

Review the `AI Risks Register` to see the assigned likelihood and magnitude scores for each risk. Then, click "Proceed to Calculate Composite Scores".

## 6. Calculating the Composite Risk Score
Duration: 01:00

With likelihood and magnitude scores assigned, Sarah can now calculate the **composite risk score** for each hazard. This score, derived from the formula $\text{Risk} = P(\text{event}) \times M(\text{consequence})$, provides a single, aggregated metric for each risk, allowing for easy comparison and prioritization. This calculation is a direct application of the "Quantitative and Qualitative Assessment" mentioned in the AI RMF.

By standardizing risk quantification, Sarah ensures that all stakeholders at QuantFinance Bank can understand and compare the severity of different AI risks, guiding resource allocation for risk mitigation.

### Your Task:

Click the "Calculate All Composite Risk Scores" button.

<aside class="info">
A higher composite score indicates a more critical risk, requiring greater attention and resource allocation for mitigation. This score acts as a common language for discussing risk levels across the organization.
</aside>

Observe the `AI Risks Register` dataframe update to include the `composite_risk_score` for each risk. Then, click "Proceed to Integrating Adversarial Insights".

## 7. Integrating Insights from Adversarial Testing: Uncovering Robustness Risks
Duration: 01:30

QuantFinance Bank's dedicated Red-Teaming unit has just concluded an exercise targeting the Credit Score Predictor. Their findings reveal vulnerabilities to "**Adversarial Attacks**"—subtle manipulations of input data that can cause misclassification (e.g., making a high-risk applicant appear low-risk). Sarah must immediately integrate these critical insights into the risk register. This directly reflects the importance of "Adversarial Testing and Red-Teaming" in the AI RMF for uncovering AI-specific security vulnerabilities like "Deceptive Inputs" and "Data Poisoning Attacks".

By documenting these specific threats, Sarah ensures the bank can develop targeted defenses, preventing malicious actors from exploiting the model and protecting the integrity of loan decisions.

### Your Task:

The details for an adversarial attack risk are pre-filled. Click "Add Adversarial Risk & Score" to add this new, high-priority risk based on the red-teaming report.

<aside class="negative">
Adversarial attacks are a serious concern for AI models, especially in high-stakes environments like finance. Uncovering these vulnerabilities through red-teaming exercises is crucial for building resilient AI systems.
</aside>

Observe the `AI Risks Register` dataframe to see the newly added adversarial attack risk with its calculated composite score. Then, click "Proceed to Supply Chain & Data Provenance Risks".

## 8. Addressing Supply Chain and Data Provenance Risks
Duration: 02:00

Beyond direct model vulnerabilities, Sarah also considers the broader "**AI Supply Chain**". A recent internal review highlighted potential data provenance issues for a separate "Fraud Detection System" and its reliance on a critical third-party feature engineering library. Sarah needs to register these "Data Provenance" and "Third-Party Dependency" risks. This is critical for understanding risks related to data quality, integrity, and external components, concepts that are central to maintaining the trustworthiness of AI systems.

Ensuring the quality and origin of data, as well as vetting third-party components, helps Sarah manage cascading vulnerabilities and maintain the overall security of QuantFinance Bank's AI portfolio.

### Your Task:

First, the system will automatically register the "Fraud Detection System" if it's not already present. Then, you will be prompted to add two new risks:
1.  **Data Provenance Risk:** Click "Add Data Provenance Risk".
2.  **Third-Party Dependency Risk:** Click "Add Third-Party Dependency Risk".

<aside class="info">
AI systems often rely on external data sources and third-party software. Understanding the risks associated with these dependencies (their origin, quality, and potential vulnerabilities) is essential for a holistic risk assessment.
</aside>

Review the `AI Models Register` and the `AI Risks Register` to see the new model and its associated risks. Then, click "Proceed to Define Controls".

## 9. Defining Controls and Mitigation Strategies
Duration: 02:00

Having identified and quantified several risks, Sarah's next crucial step is to define and propose specific **controls to mitigate them**. This involves designing defenses tailored to each identified risk, from technical measures like input sanitization to procedural controls like regular model retraining. This directly applies the "Risk Controls and Mitigation Strategies" concept from the AI RMF, emphasizing "Mapping Controls to Risks" and "Hierarchical Control Design."

By establishing clear controls, Sarah ensures that QuantFinance Bank has concrete plans to reduce the likelihood or impact of identified risks, thereby strengthening the overall resilience of its AI systems against threats like adversarial attacks and data quality issues.

### Your Task:

For each of the identified risks (Algorithmic Bias, Adversarial Attack, Data Provenance), click the corresponding "Add Control" button. This will add a recommended mitigation strategy to the `AI Controls Register`.

<aside class="positive">
Controls are the backbone of risk management. They are specific actions or mechanisms put in place to reduce the identified risks. Without effective controls, even well-identified risks can lead to significant harm.
</aside>

Observe the `AI Controls Register` dataframe update with the newly defined controls. Once all specified controls are added (or acknowledged as existing), click "Proceed to Assign Risk Response Options".

## 10. Assigning Risk Response Options
Duration: 02:00

For each identified risk with its proposed controls, Sarah must now formalize the bank's "**Risk Response Option**". This involves deciding whether to mitigate, transfer, avoid, or accept the risk based on the severity of the residual risk (the risk remaining after controls are in place) and the bank's overall risk tolerance. This strategic decision-making is a core part of the AI RMF, ensuring that every risk has a clear management plan.

This step helps Sarah communicate to stakeholders exactly how each AI risk will be handled, ensuring alignment with the bank's broader risk appetite and regulatory requirements.

### Your Task:

For each control, use the slider to specify its expected `Effectiveness Score` (1=Ineffective, 5=Highly Effective) and select the appropriate `Risk Response` from the dropdown (Mitigate, Transfer, Avoid, or Accept). After assigning responses for all controls, click "Assign All Responses".

<aside class="info">
"Mitigate" aims to reduce the risk. "Transfer" shifts the risk to a third party (e.g., insurance). "Avoid" eliminates the risk entirely (e.g., by not using the AI model). "Accept" acknowledges the risk and its potential impact without further action. Sarah's goal is usually to mitigate.
</aside>

Review the `AI Controls Register` to see the assigned effectiveness scores and risk responses. Then, click "Proceed to Review Risk Register".

## 11. Reviewing the Comprehensive AI Model Risk Register
Duration: 01:00

At this stage, Sarah needs to review the entire AI Model Risk Register to get a holistic view of the bank's AI risk landscape. This comprehensive display, integrating models, risks, assessments, and controls, is the "Centralized Repository" described in the AI RMF. It allows Sarah to verify that all necessary information is captured and interconnected.

This unified view is essential for Sarah to present to internal audit and senior management, demonstrating transparent and systematic AI risk governance across QuantFinance Bank.

### Your Task:

Click the "Generate Comprehensive AI Model Risk Register" button.

<aside class="positive">
This comprehensive register acts as a vital communication tool. It provides a single, unified source of truth for all AI-related risks, fostering transparency and accountability across the organization.
</aside>

Observe the generated dataframe, which merges information from the models, risks, and controls registers into a single, detailed view. Then, click "Proceed to Analyze Top Risks".

## 12. Analyzing and Prioritizing High-Scoring Risks
Duration: 01:30

With a growing number of AI models and associated risks, Sarah needs an efficient way to identify and prioritize the most critical threats. Analyzing risks by their `composite_risk_score` allows her to pinpoint the highest-scoring hazards, ensuring that resources and attention are directed where they are most needed. This aligns with the AI RMF's principle of "**Risk-based**" decision-making.

This analysis helps Sarah focus on the "top risks" that pose the greatest potential harm to QuantFinance Bank, enabling proactive resource allocation and strategic risk mitigation.

### Your Task:

You can adjust the "Number of Top Risks to Display" if you wish. Then, click "Identify Top Risks".

<aside class="info">
Prioritization is key in risk management. By focusing on the highest-scoring risks, Sarah ensures that limited resources are allocated effectively to address the most impactful threats first.
</aside>

Observe the `Top N AI Risks by Composite Score` dataframe, showcasing the most critical risks identified. Then, click "Proceed to Visualize Risk Distribution".

## 13. Visualizing Risk Distribution by Type
Duration: 01:00

To provide an executive overview of the bank's overall AI risk posture, Sarah wants to visualize how identified risks are distributed across the different categories defined in the AI Risk Taxonomy (e.g., Data, Model, System). This aggregation helps in understanding systemic weaknesses and informs strategic investments in risk management capabilities. This type of visualization supports the "MEASURE" function of the AI RMF and provides an aggregated view of risks.

By visualizing the distribution, Sarah can identify if a particular risk category (e.g., "Model Risk") is disproportionately high, indicating a need for more robust controls or new policies in that area.

### Your Task:

Click the "Generate Risk Distribution Chart" button.

<aside class="positive">
Visualizations help translate complex data into actionable insights. This chart allows Sarah to quickly grasp where QuantFinance Bank's AI risks are concentrated, aiding strategic decision-making.
</aside>

Observe the bar chart illustrating the distribution of AI risks by their broad categories. Then, click "Proceed to Simulate Operational Monitoring".

## 14. Simulating Operational Monitoring Feedback: Detecting Data Drift
Duration: 01:30

AI risk management is not a one-time activity; it requires continuous vigilance. Sarah receives an alert from the bank's model monitoring system for the Credit Score Predictor, indicating a significant "**Data Drift**" in the input features. This operational feedback is a critical trigger for re-evaluating the associated risks and exemplifies the "Continuous Validation" aspect of the AI RMF.

This scenario demonstrates the necessity of an "Adaptive Cycle" or "outer loop," where operational data constantly informs risk assessment, prompting Sarah to re-evaluate and update the risk register to maintain trust and performance.

### Your Task:

The details for the data drift alert are pre-filled. Click "Simulate Data Drift & Update Risk" to record this new information and update the risk assessment for the Credit Score Predictor.

<aside class="negative">
Data drift can silently erode model performance and lead to incorrect decisions. Continuous monitoring is crucial to detect these changes and adapt risk assessments in real-time.
</aside>

Observe the `AI Risks Register` dataframe update to reflect the new "Data Drift" risk for the Credit Score Predictor, including its likelihood, magnitude, and composite score. Then, click "Proceed to Update Risk Assessment".

## 15. Updating Risk Assessment based on Monitoring Feedback
Duration: 01:00

Following the data drift alert, Sarah must now formally update the risk assessment for the "Credit Score Predictor". This involves adjusting the likelihood and/or magnitude scores for relevant risks, such as "Performance Degradation" or the newly identified "Data Drift," to reflect the new operational reality. This exemplifies "Continuous Validation" and "Post-Deployment Monitoring," which are essential for maintaining the trustworthiness of adaptive AI systems.

By continuously refining risk assessments based on real-time monitoring, Sarah ensures that the risk register remains a living document that accurately reflects the current state of AI risks at QuantFinance Bank, supporting agile risk management.

### Your Task:

Click "Formally Update Performance Degradation Risk" to adjust its scores based on the new data drift information.

<aside class="info">
Risk management is an ongoing process. Real-time feedback from monitoring systems must be integrated into the risk register to ensure it always reflects the most current risk landscape.
</aside>

Observe the `AI Risks Register` for the Credit Score Predictor, noting the updated scores for "Performance Degradation". Then, click "Proceed to Final Summary".

## 16. Workflow Summary
Duration: 01:30

Congratulations! Sarah has successfully navigated the complex landscape of AI risk management. From initial system setup and model registration to identifying, assessing, mitigating, and continuously monitoring risks—she has built a comprehensive and adaptive AI risk posture for QuantFinance Bank.

This continuous feedback loop ensures that the bank's AI models remain trustworthy and perform reliably in evolving environments. You have experienced a full cycle of proactive and reactive AI risk management, demonstrating the critical steps required for responsible AI deployment in the financial sector.

### Your Task:

Review the final comprehensive risk register, the identified top risks, and the overall risk distribution chart, which summarize Sarah's complete workflow.

<aside class="positive">
<b>You've done it!</b> By following Sarah's workflow, you've gained a practical understanding of key AI Risk Management Framework concepts and how to apply them to ensure the safe and ethical deployment of AI.
</aside>

If you wish to explore the workflow again or experiment with different inputs, you can click "Restart Workflow".
