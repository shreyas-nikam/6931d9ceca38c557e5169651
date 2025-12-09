import streamlit as st


def main():
    st.subheader("2. Defining Our AI Risk Taxonomy")
    st.markdown("""
        To ensure a consistent and comprehensive identification of AI-specific risks, Sarah needs a standardized taxonomy. This taxonomy categorizes risks across different dimensions—Data, Model, System, Human, and Organizational—providing a structured framework for assessment. This aligns with the "Risk Taxonomy" concept in the AI RMF, ensuring that all potential vulnerabilities are considered.

        A well-defined taxonomy helps Sarah and her team systematically identify potential AI-specific hazards, such as data drift, adversarial attacks, algorithmic bias, or privacy breaches, ensuring comprehensive coverage and facilitating communication across different departments within QuantFinance Bank.
    """)

    # Display taxonomy in a visually appealing way
    st.markdown("### 📊 AI Risk Taxonomy Framework")

    # Define colors for each category
    category_colors = {
        "Data Risk": "#FF6B6B",
        "Model Risk": "#4ECDC4",
        "System Risk": "#FFE66D",
        "Human Risk": "#A8DADC",
        "Organizational Risk": "#C77DFF"
    }

    # Create columns for better layout
    col1, col2 = st.columns(2)

    taxonomy = st.session_state.AI_RISK_TAXONOMY
    categories = list(taxonomy.keys())

    # Display first column categories
    with col1:
        for category in categories[:3]:
            with st.container(border=True):
                st.markdown(f"### 🎯 {category}")
                risks = taxonomy[category]
                for risk in risks:
                    st.markdown(f"• **{risk}**")

    # Display second column categories
    with col2:
        for category in categories[3:]:
            with st.container(border=True):
                st.markdown(f"### 🎯 {category}")
                risks = taxonomy[category]
                for risk in risks:
                    st.markdown(f"• **{risk}**")

    st.info("This taxonomy will serve as a checklist and classification system for Sarah and her team. By having predefined categories like 'Data Risk' and 'Model Risk' with specific types, Sarah ensures no critical area of AI risk is overlooked when assessing new models. This structured approach underpins the systematic identification required for effective risk management.")

    st.markdown("---")
    st.markdown("### 🎯 Test Your Understanding: Risk Taxonomy Quiz")
    st.markdown("Let's test your understanding of the AI Risk Taxonomy. Answer these questions to ensure you grasp the different risk categories.")

    # Initialize quiz state
    if 'quiz_completed' not in st.session_state:
        st.session_state.quiz_completed = False
    if 'quiz_answers_submitted' not in st.session_state:
        st.session_state.quiz_answers_submitted = {
            'q1': False,
            'q2': False,
            'q3': False,
            'q4': False
        }
    if 'quiz_submitted_answers' not in st.session_state:
        st.session_state.quiz_submitted_answers = {
            'q1': None,
            'q2': None,
            'q3': None,
            'q4': None
        }
    if 'quiz_score' not in st.session_state:
        st.session_state.quiz_score = 0

    # Question 1
    st.markdown("**Question 1:** A model's predictions become less accurate over time as customer behavior patterns change. Which risk category does this belong to?")
    q1_answer = st.radio(
        "Select your answer:",
        ["Data Risk", "Model Risk", "System Risk",
            "Human Risk", "Organizational Risk"],
        key="q1",
        index=None
    )

    # Re-enable button if answer changed
    q1_changed = q1_answer != st.session_state.quiz_submitted_answers[
        'q1'] and q1_answer is not None

    if st.button("Submit Answer for Question 1", key="submit_q1", disabled=(not q1_changed and st.session_state.quiz_answers_submitted['q1'])):
        if q1_answer:
            st.session_state.quiz_answers_submitted['q1'] = True
            st.session_state.quiz_submitted_answers['q1'] = q1_answer
            st.rerun()

    if st.session_state.quiz_answers_submitted['q1'] and q1_answer:
        if q1_answer == "Model Risk":
            st.success("✅ Correct! This is **Performance Degradation** under Model Risk. The model's accuracy declining over time due to changing patterns is a classic Model Risk.")
            st.info("💡 **Explanation:** Performance Degradation occurs when a model's effectiveness decreases over time, often due to concept drift or changes in the underlying data distribution.")
        else:
            st.error(f"❌ Incorrect. You selected {q1_answer}.")
            if q1_answer == "Data Risk":
                st.warning(
                    "💭 **Hint:** While data changes are involved, this specifically relates to the model's inability to adapt to those changes, making it a model-level issue.")
            else:
                st.warning("💭 **Hint:** Think about what component is failing to maintain accuracy. It's not about the data itself, the system infrastructure, people, or organizational processes—it's about the model's performance.")

    # Question 2
    st.markdown("---")
    st.markdown("**Question 2:** Training data contains historical biases that lead to unfair loan decisions for certain demographic groups. Which risk type is this?")
    q2_answer = st.radio(
        "Select your answer:",
        ["Data Bias", "Algorithmic Bias", "Fairness",
            "Data Quality", "Ethical Misalignment"],
        key="q2",
        index=None
    )

    # Re-enable button if answer changed
    q2_changed = q2_answer != st.session_state.quiz_submitted_answers[
        'q2'] and q2_answer is not None

    if st.button("Submit Answer for Question 2", key="submit_q2", disabled=(not q2_changed and st.session_state.quiz_answers_submitted['q2'])):
        if q2_answer:
            st.session_state.quiz_answers_submitted['q2'] = True
            st.session_state.quiz_submitted_answers['q2'] = q2_answer
            st.rerun()

    if st.session_state.quiz_answers_submitted['q2'] and q2_answer:
        if q2_answer in ["Data Bias", "Algorithmic Bias"]:
            st.success(
                f"✅ Correct! This could be classified as both **Data Bias** (Data Risk) and **Algorithmic Bias** (Model Risk).")
            st.info("💡 **Explanation:** When historical training data contains biases, it falls under **Data Bias**. When the model learns and perpetuates these biases in its predictions, it becomes **Algorithmic Bias**. Both are correct perspectives on this problem!")
        elif q2_answer == "Fairness":
            st.warning(
                "⚠️ Partially correct! While this is a **Fairness** concern (Model Risk), the root cause is actually biased training data.")
            st.info("💭 **Hint:** Look for the more specific risk types that directly address bias in data or model outputs: Data Bias or Algorithmic Bias.")
        else:
            st.error(f"❌ Incorrect. You selected {q2_answer}.")
            st.warning("💭 **Hint:** This scenario involves bias in the data that leads to unfair outcomes. Look for risk types that specifically mention 'bias' in the taxonomy.")

    # Question 3
    st.markdown("---")
    st.markdown("**Question 3:** A third-party library used for feature engineering has unknown vulnerabilities. Which category does this belong to?")
    q3_answer = st.radio(
        "Select your answer:",
        ["System Risk - Security Vulnerability", "Organizational Risk - Third-Party Dependency",
            "System Risk - Integration Issues", "Data Risk - Data Provenance"],
        key="q3",
        index=None
    )

    # Re-enable button if answer changed
    q3_changed = q3_answer != st.session_state.quiz_submitted_answers[
        'q3'] and q3_answer is not None

    if st.button("Submit Answer for Question 3", key="submit_q3", disabled=(not q3_changed and st.session_state.quiz_answers_submitted['q3'])):
        if q3_answer:
            st.session_state.quiz_answers_submitted['q3'] = True
            st.session_state.quiz_submitted_answers['q3'] = q3_answer
            st.rerun()

    if st.session_state.quiz_answers_submitted['q3'] and q3_answer:
        if q3_answer == "Organizational Risk - Third-Party Dependency":
            st.success(
                "✅ Correct! This is **Third-Party Dependency** under Organizational Risk.")
            st.info("💡 **Explanation:** Reliance on external components or vendors with unknown vulnerabilities or insufficient documentation falls under Third-Party Dependency, which is an organizational-level concern about vendor management and supply chain security.")
        else:
            st.error(f"❌ Incorrect. You selected {q3_answer}.")
            if "System Risk" in q3_answer:
                st.warning("💭 **Hint:** While there may be security concerns, the key issue is the **dependency on an external third party**. This is more about organizational vendor management than system-level technical security.")
            elif "Data Risk" in q3_answer:
                st.warning(
                    "💭 **Hint:** Data Provenance is about tracking data sources and lineage. This question is about a third-party **library/component**, not data itself.")
            else:
                st.warning(
                    "💭 **Hint:** Think about the organizational aspect of relying on external vendors or libraries. Check the Organizational Risk category.")

    # Question 4
    st.markdown("---")
    st.markdown("**Question 4:** An attacker crafts malicious inputs designed to fool the model into making incorrect predictions. What is this?")
    q4_answer = st.radio(
        "Select your answer:",
        ["Data Poisoning", "Adversarial Attacks",
            "Deceptive Inputs", "Security Vulnerability", "Misuse"],
        key="q4",
        index=None
    )

    # Re-enable button if answer changed
    q4_changed = q4_answer != st.session_state.quiz_submitted_answers[
        'q4'] and q4_answer is not None

    if st.button("Submit Answer for Question 4", key="submit_q4", disabled=(not q4_changed and st.session_state.quiz_answers_submitted['q4'])):
        if q4_answer:
            st.session_state.quiz_answers_submitted['q4'] = True
            st.session_state.quiz_submitted_answers['q4'] = q4_answer
            st.rerun()

    if st.session_state.quiz_answers_submitted['q4'] and q4_answer:
        if q4_answer == "Adversarial Attacks":
            st.success(
                "✅ Correct! This is **Adversarial Attacks** under Model Risk.")
            st.info("💡 **Explanation:** Adversarial Attacks involve crafting malicious inputs at inference time to deceive the model. These attacks exploit the model's learned patterns to cause misclassifications.")
        elif q4_answer == "Data Poisoning":
            st.warning("⚠️ Close! But not quite.")
            st.info("💭 **Hint:** Data Poisoning occurs during the **training phase** by corrupting the training data. This question describes attacks during **inference/prediction time**. The correct answer is Adversarial Attacks.")
        else:
            st.error(f"❌ Incorrect. You selected {q4_answer}.")
            st.warning("💭 **Hint:** This is about crafting specific inputs to fool an already-trained model. Look for a Model Risk type that specifically mentions attacks designed to deceive the model.")

    # Calculate score and show results when all questions are submitted
    all_submitted = all(st.session_state.quiz_answers_submitted.values())

    if all_submitted:
        correct_count = 0
        if q1_answer == "Model Risk":
            correct_count += 1
        if q2_answer in ["Data Bias", "Algorithmic Bias"]:
            correct_count += 1
        if q3_answer == "Organizational Risk - Third-Party Dependency":
            correct_count += 1
        if q4_answer == "Adversarial Attacks":
            correct_count += 1
        st.markdown("---")

        st.success("✅ Quiz completed! Proceed to Model Registration.")
        st.session_state.current_step = 3
