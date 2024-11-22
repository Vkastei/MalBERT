import torch
import torch.nn.functional as F

class PredictModel:

    def __init__(self):
         pass
    def predict_sentiment(self, text, model, tokenizer, device, max_length=128):
        model.eval()
        encoding = tokenizer(text, return_tensors='pt', max_length=max_length, padding='max_length', truncation=True)
        input_ids = encoding['input_ids'].to(device)
        attention_mask = encoding['attention_mask'].to(device)

        with torch.no_grad():
            outputs = model(input_ids=input_ids, attention_mask=attention_mask)

            probabilities = F.softmax(outputs, dim=1)

            predicted_class = torch.argmax(probabilities, dim=1).item()
            predicted_probability = probabilities[0, predicted_class].item()
            
        label = "benign" if predicted_class == 1 else "malware"
        return label, predicted_probability
