import torch
from sklearn.metrics import accuracy_score, classification_report

class EvaluateModel:

    def __init__(self):
        pass
        
    def evaluate(self, model, data_loader, device):
        model.eval()
        predictions = []
        actual_labels = []
        with torch.no_grad():
            for batch in data_loader:
                input_ids = batch['input_ids'].to(device)
                attention_mask = batch['attention_mask'].to(device)
                labels = batch['label'].to(device)
                outputs = model(input_ids=input_ids, attention_mask=attention_mask)
                _, preds = torch.max(outputs, dim=1)
                predictions.extend(preds.cpu().tolist())
                actual_labels.extend(labels.cpu().tolist())
        return accuracy_score(actual_labels, predictions), classification_report(actual_labels, predictions)