from data.create_dataset import CreateDataset
from preprocessing.disassembler import Disassembler
import os

print(os.getcwd())
os.chdir("data/samples")
CreateDataset = CreateDataset()
Disassembler = Disassembler()

# # Creates 100 benign samples, disassembles them
CreateDataset.create_benign_samples(100)
Disassembler.disassemble_samples(1)
# Creates 100 malware samples, disassembles them
CreateDataset.create_malware_samples(100)
Disassembler.disassemble_samples(0)

# creates a datset.csv inside data/samples containing the samples
CreateDataset.create_training_dataset_csv(200)

