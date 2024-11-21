from data.create_dataset import CreateDataset
from torch.utils.data import DataLoader
from data.dataset import Dataset
from training.train import TrainModel
from training.predict import PredictModel
from preprocessing.disassembler import Disassembler
import torch
from models.classifier import MalBERTClassifier
from transformers import BertTokenizer, BertModel, AdamW, get_linear_schedule_with_warmup
from sklearn.model_selection import train_test_split
import training
import os
import shutil

binary_filepath = ""
# Set up parameters
bert_model_name = 'bert-base-uncased'
num_classes = 2
max_length = 128
batch_size = 16
num_epochs = 1
learning_rate = 2e-5

os.chdir("data/samples")


# CreateDataset = CreateDataset()
# TrainModel = TrainModel()
# Disassembler = Disassembler()

# Disassembler.loop_malware_samples()
# CreateDataset.create_training_dataset_csv(100)
# texts, labels = CreateDataset.create_training_dataset()

# train_texts, val_texts, train_labels, val_labels = train_test_split(texts, labels, test_size=0.2, random_state=42)

# tokenizer = BertTokenizer.from_pretrained(bert_model_name)
# train_dataset = Dataset(train_texts, train_labels, tokenizer, max_length)
# val_dataset = Dataset(val_texts, val_labels, tokenizer, max_length)
# train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
# val_dataloader = DataLoader(val_dataset, batch_size=batch_size)

# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# model = MalBERTClassifier(bert_model_name, num_classes).to(device)
# model
# optimizer = AdamW(model.parameters(), lr=learning_rate)
# total_steps = len(train_dataloader) * num_epochs
# scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=0, num_training_steps=total_steps)

# TrainModel.train(model, train_dataloader, val_dataloader, optimizer, scheduler, device, 50, "test.pth")
Disassembler = Disassembler()

shutil.copy(binary_filepath, os.getcwd())
binary_filepath = os.path.basename(binary_filepath)
print(binary_filepath)


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = BertTokenizer.from_pretrained(bert_model_name)
binary_filepath_no_ext, _ = os.path.splitext(binary_filepath)
model = MalBERTClassifier(bert_model_name, num_classes).to(device)
model.load_state_dict(torch.load("bert_classifier.pth"))

data = ""
with open("18e1a9142a9f6b7a601ff64074a7a59e370d5bc8270ef5aa17277ef4531b05bc6.txt", 'r', encoding="utf-8") as sample:
    data = sample.read().replace("\n", " ")
PredictModel = PredictModel()
type, prohability = PredictModel.predict_sentiment(data, model, tokenizer, device)
print("This sample is " + str(round(prohability * 100)) + "% " + str(type))
