import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from aif360.datasets import CompasDataset
from aif360.metrics import BinaryLabelDatasetMetric, ClassificationMetric
from aif360.algorithms.preprocessing import Reweighing

# Load COMPAS dataset (AIF360 provides a loader)
data = CompasDataset()

# Define privileged and unprivileged groups
privileged_groups = [{'race': 1}]  # Caucasian
unprivileged_groups = [{'race': 0}]  # African-American

# Bias metrics
metric = BinaryLabelDatasetMetric(data, unprivileged_groups=unprivileged_groups, privileged_groups=privileged_groups)

print('Statistical parity difference:', metric.statistical_parity_difference())
print('Disparate impact:', metric.disparate_impact())

# Visualize distribution of predicted scores by race
scores = pd.DataFrame({'race': data.features[:, data.feature_names.index('race')],
                      'score': data.scores})
sns.histplot(data=scores, x='score', hue='race', bins=20, kde=True, stat='density')
plt.title('Distribution of COMPAS Scores by Race')
plt.xlabel('Risk Score')
plt.ylabel('Density')
plt.legend(['African-American', 'Caucasian'])
plt.tight_layout()
plt.savefig('compas_score_distribution.png')
plt.close()

# Example: Calculate false positive rates by race
# Assume 'predicted' is the predicted label (for demonstration, use ground truth)
preds = data.labels
labels = data.labels
races = data.features[:, data.feature_names.index('race')]

fpr = {}
for group, name in zip([0, 1], ['African-American', 'Caucasian']):
    idx = (races == group)
    fp = ((preds == 1) & (labels == 0) & idx).sum()
    tn = ((preds == 0) & (labels == 0) & idx).sum()
    fpr[name] = fp / (fp + tn)

print('False Positive Rate (African-American):', fpr['African-American'])
print('False Positive Rate (Caucasian):', fpr['Caucasian'])

# Bar plot for FPR
plt.bar(fpr.keys(), fpr.values(), color=['red', 'blue'])
plt.title('False Positive Rate by Race')
plt.ylabel('False Positive Rate')
plt.tight_layout()
plt.savefig('compas_fpr_by_race.png')
plt.close()

# Remediation: Reweighing
rw = Reweighing(unprivileged_groups=unprivileged_groups, privileged_groups=privileged_groups)
data_transf = rw.fit_transform(data)
metric_transf = BinaryLabelDatasetMetric(data_transf, unprivileged_groups=unprivileged_groups, privileged_groups=privileged_groups)
print('Statistical parity difference after reweighing:', metric_transf.statistical_parity_difference())
print('Disparate impact after reweighing:', metric_transf.disparate_impact())
