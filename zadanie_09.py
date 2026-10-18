# Lekcja 05 - Zadanie 9

cm = [[80, 10], [5, 45]]
TN, FP = cm[0][0], cm[0][1]
FN, TP = cm[1][0], cm[1][1]
accuracy = (TP + TN) / (TP + TN + FP + FN)
precision = TP / (TP + FP)
recall = TP / (TP + FN)
print(f"Accuracy: {accuracy:.2%}")
print(f"Precision: {precision:.2%}")
print(f"Recall: {recall:.2%}")
