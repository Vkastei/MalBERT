from data.create_dataset import CreateDataset
from torch.utils.data import DataLoader
from data.dataset import Dataset
from training.train import TrainModel
import torch
from models.classifier import MalBERTClassifier
from transformers import BertTokenizer, get_linear_schedule_with_warmup
from sklearn.model_selection import train_test_split
import os

# save model filename
model_save = "samples_model.pth"

# model training params
bert_model_name = 'bert-base-uncased'
num_classes = 2
max_length = 128
batch_size = 16
num_epochs = 5
learning_rate = 2e-5

# change directory to samples folder to access dataset.csv
os.chdir("data/samples")

# initialize classes
CreateDataset = CreateDataset()
TrainModel = TrainModel()

# load data from dataset.csv 
texts, labels = CreateDataset.create_training_dataset()

# split dataset into training and validation sets
train_texts, val_texts, train_labels, val_labels = train_test_split(texts, labels, test_size=0.2, random_state=42)

# tokenizer
tokenizer = BertTokenizer.from_pretrained(bert_model_name)

# create training and validation datasets 
train_dataset = Dataset(train_texts, train_labels, tokenizer, max_length)
val_dataset = Dataset(val_texts, val_labels, tokenizer, max_length)
train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_dataloader = DataLoader(val_dataset, batch_size=batch_size)

# create classifier model and device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = MalBERTClassifier(bert_model_name, num_classes).to(device)

# optimizer
optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)

total_steps = len(train_dataloader) * num_epochs
scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=0, num_training_steps=total_steps)

# train model with params 
TrainModel.train(model, train_dataloader, val_dataloader, optimizer, scheduler, device, num_epochs, model_save)
