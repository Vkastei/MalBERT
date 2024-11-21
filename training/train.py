import torch
from torch import nn
from training.evaluate import EvaluateModel

class TrainModel:

    def __init__(self):
        pass    
    def _save_model(self, model, filename):
        torch.save(model.state_dict(), "bert_classifier.pth")
    def _train_model(self, model, data_loader, optimizer, scheduler, device):
        model.train()
        for batch in data_loader:
            optimizer.zero_grad()
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['label'].to(device)
            outputs = model(input_ids=input_ids, attention_mask=attention_mask)
            loss = nn.CrossEntropyLoss()(outputs, labels)
            loss.backward()
            optimizer.step()
            scheduler.step()

    def train(self, model, train_dataloader, val_dataloader, optimizer, scheduler, device, num_epochs, save_model_name):

        for epoch in range(num_epochs):
            print(f"Epoch {epoch + 1}/{num_epochs}")
            self._train_model(model, train_dataloader, optimizer, scheduler, device)
            accuracy, report = EvaluateModel.evaluate(self, model, val_dataloader, device)
            print(f"Validation Accuracy: {accuracy:.4f}")
            print(report)
        self._save_model(model, save_model_name)