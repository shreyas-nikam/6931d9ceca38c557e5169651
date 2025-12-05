# QuLab: QuantFinance AI Model Risk Manager (Sarah's Workflow)

![QuantUniversity Logo](https://www.quantuniversity.com/assets/img/logo5.jpg)

## Project Title and Description

**QuLab: QuantFinance AI Model Risk Manager** is an interactive Streamlit application designed as a lab project to simulate an end-to-end AI risk management workflow. The application puts the user in the shoes of **Sarah, a Senior Risk Manager at QuantFinance Bank**, tasked with establishing a robust framework for managing the unique risks posed by Artificial Intelligence (AI) models in the financial sector.

The project addresses the core challenge that while AI offers powerful capabilities for critical operations like credit assessment and fraud detection, it also introduces novel risks such as algorithmic bias, adversarial attacks, and data drift. This application provides a practical, guided experience to identify, assess, mitigate, and continuously monitor these AI-specific risks, aligning with industry best practices and regulatory frameworks like the NIST AI Risk Management Framework (AI RMF).

Through a series of guided steps, Sarah (the user) will navigate real-world tasks, moving beyond theoretical concepts to build a proactive and adaptive system to manage AI risks effectively at QuantFinance Bank.

## Features

This application guides Sarah through a comprehensive AI risk management lifecycle, demonstrating the following key features:

1.  **System Initialization**: Set up the foundational data structures for managing AI models, risks, and controls in a centralized repository.
2.  **AI Risk Taxonomy Definition**: Introduce and leverage a structured AI risk taxonomy (Data, Model, System, Human, Organizational risks) for consistent risk identification.
3.  **AI Model Registration**: Formally register new AI models (e.g., Credit Score Predictor, Fraud Detection System) with essential details.
4.  **Initial Risk Identification**: Systematically identify potential AI-specific hazards for registered models using the defined taxonomy.
5.  **Risk Quantification**: Assess the likelihood and magnitude of identified risks using a numerical scoring system (1-5).
6.  **Composite Risk Score Calculation**: Compute an aggregated risk score for each hazard ($P(\text{event}) \times M(\text{consequence})$) to enable prioritization.
7.  **Integrating Adversarial Insights**: Incorporate findings from adversarial testing and red-teaming exercises to identify robustness risks.
8.  **Addressing Supply Chain & Data Provenance Risks**: Identify and assess risks related to data origin, quality, and third-party dependencies within the AI supply chain.
9.  **Defining Controls and Mitigation Strategies**: Design specific controls (technical and procedural) to mitigate identified risks.
10. **Assigning Risk Response Options**: Determine strategic risk responses (e.g., Mitigate, Transfer, Avoid, Accept) for each risk and control pair.
11. **Comprehensive AI Model Risk Register**: Generate and review a holistic risk register, integrating all model, risk, and control information.
12. **Analyzing and Prioritizing High-Scoring Risks**: Identify and display top risks based on their composite scores to focus mitigation efforts.
13. **Visualizing Risk Distribution**: Generate a bar chart showing the distribution of AI risks across broad categories for an executive overview.
14. **Simulating Operational Monitoring Feedback**: Simulate real-time alerts, such as data drift, to demonstrate continuous validation.
15. **Updating Risk Assessment**: Adjust risk scores based on simulated operational monitoring feedback, showcasing an adaptive risk management cycle.
16. **Interactive Workflow Navigation**: Sidebar buttons allow for navigating between different steps of the guided workflow.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need Python 3.8+ installed on your system.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/qu-lab-ai-risk-manager.git
    cd qu-lab-ai-risk-manager
    ```
    *(Note: Replace `your-username/qu-lab-ai-risk-manager` with the actual repository path if this project is hosted.)*

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    *   **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    *   **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required dependencies:**
    Create a `requirements.txt` file in the project root with the following content:
    ```
    streamlit
    pandas
    matplotlib
    seaborn
    ```
    Then, install them:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the Streamlit application:**
    Ensure your virtual environment is activated and you are in the project's root directory (where `app.py` is located).
    ```bash
    streamlit run app.py
    ```

2.  **Access the application:**
    After running the command, your default web browser should automatically open to `http://localhost:8501`. If not, navigate to this URL manually.

3.  **Follow the Guided Workflow:**
    The application is designed as a sequential lab project. Interact with the forms, buttons, and sliders on each page to progress through Sarah's AI risk management workflow. The sidebar also provides navigation buttons for quick access to different steps.

## Project Structure

The project has a simple structure, ideal for a lab environment:

```
qu-lab-ai-risk-manager/
├── app.py              # Main Streamlit application script
├── requirements.txt    # List of Python dependencies
└── README.md           # This README file
```

## Technology Stack

*   **Python**: The core programming language.
*   **Streamlit**: For creating interactive web applications with Python.
*   **Pandas**: For data manipulation and management of AI models, risks, and controls in DataFrames.
*   **Matplotlib**: For static, embeddable visualizations.
*   **Seaborn**: For enhancing data visualizations with a high-level interface.

## Contributing

This is a lab project, primarily for educational purposes. However, contributions are welcome!

1.  **Fork the repository.**
2.  **Create a new branch** for your feature or bug fix (`git checkout -b feature/AmazingFeature`).
3.  **Commit your changes** (`git commit -m 'Add some AmazingFeature'`).
4.  **Push to the branch** (`git push origin feature/AmazingFeature`).
5.  **Open a Pull Request.**

Please ensure your code adheres to a clean, readable style and includes necessary comments.

## License

This project is licensed under the MIT License - see the LICENSE.md file (or assume MIT if no file exists) for details.

## Contact

For any questions or feedback regarding this project, please contact:

*   **QuantUniversity** (as the educational institution)
*   **[Your Name/Email/GitHub Profile]** (if this is your personal fork/project)
