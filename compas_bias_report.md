# COMPAS Recidivism Dataset Bias Audit Report

## Introduction
This report analyzes racial bias in the COMPAS Recidivism dataset using IBM’s AI Fairness 360 toolkit. The focus is on the disparity in risk scores and false positive rates between African-American and Caucasian defendants.

## Findings
The analysis revealed significant racial disparities:
- **Statistical Parity Difference**: The difference in favorable outcomes between African-American and Caucasian groups was negative, indicating African-Americans were less likely to receive favorable risk scores.
- **Disparate Impact**: The ratio of favorable outcomes for African-Americans to Caucasians was below the fairness threshold (typically 0.8), suggesting potential bias.
- **False Positive Rate (FPR)**: African-Americans had a higher FPR compared to Caucasians, meaning they were more likely to be incorrectly labeled as high risk when they did not reoffend. Visualizations confirmed this disparity.

## Remediation
To address these issues, the Reweighing algorithm from AIF360 was applied. This preprocessing technique adjusts instance weights to reduce bias. After reweighing, both statistical parity difference and disparate impact metrics improved, indicating a reduction in bias.

## Recommendations
- **Use Fairness-Aware Models**: Incorporate bias mitigation techniques, such as reweighing or adversarial debiasing, in predictive modeling pipelines.
- **Continuous Monitoring**: Regularly audit models for fairness, especially when deployed in high-stakes domains like criminal justice.
- **Transparency**: Clearly communicate model limitations and fairness metrics to stakeholders.

## Conclusion
The COMPAS dataset exhibits measurable racial bias in risk assessment scores. Applying fairness interventions can reduce, but not entirely eliminate, these disparities. Ongoing vigilance and ethical oversight are essential when using such tools in practice.
