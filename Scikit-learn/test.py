from sklearn.metrics import roc_auc_score

y_true = [1, 1, 0, 1, 0, 0, 0, 0, 0, 0]
y_pred = [0.75, 0.95, 0.85, 0.35, 0.55, 0.65, 0.25, 0.15, 0.45, 0.05]

db = 0.55

print(roc_auc_score(y_true, y_pred))
