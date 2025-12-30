
# wk_7_AI_Ethics_Assignment

This assignment demonstrates the application of AI ethics principles through a bias audit of the COMPAS Recidivism dataset using Python and IBM's AI Fairness 360 toolkit.

## Contents
- `compas_bias_audit.py`: Python code to analyze and visualize racial bias in COMPAS risk scores.
- `compas_bias_report.md`: 300-word report summarizing findings and remediation steps.
- `compas_score_distribution.png`, `compas_fpr_by_race.png`: Visualizations of risk score and false positive rate disparities.
- Ethical reflection (see below).

## Steps
1. **Bias Audit**: Used AIF360 to analyze racial bias in COMPAS risk scores, focusing on statistical parity, disparate impact, and false positive rates.
2. **Visualization**: Generated plots to illustrate disparities between African-American and Caucasian groups.
3. **Remediation**: Applied reweighing to mitigate bias and measured improvement.
4. **Ethical Reflection**: Reflected on ensuring ethical AI in personal projects, covering fairness, transparency, privacy, accountability, and monitoring.

## How to Run
1. Install dependencies: `pip install -r requirements.txt` (or see code for package list).
2. Run the audit: `python compas_bias_audit.py`
3. Review generated images and report.

## Ethical Reflection
To ensure a personal AI project adheres to ethical principles, I would:
- Audit for bias and use fairness-aware algorithms.
- Communicate model purpose, limitations, and logic.
- Protect privacy and comply with data regulations.
- Establish accountability and error-handling processes.
- Continuously monitor for fairness and unintended consequences.

By integrating these practices, I would help ensure my AI project aligns with ethical principles and serves its intended purpose responsibly.
