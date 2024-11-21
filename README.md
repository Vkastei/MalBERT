# MalBERT
> [!WARNING]  
> This repository contains code that is able to download & extract malware. Demanding user attention due to potential risk of being infiltrated.
MalBERT is a project to detect malware with a fine tuned BERT model, trained on disassembled samples of malware and benign binaries.

Currently the Model is trained on around 500 benign executables, and 500 malware executables. The benign samples are just copied from the System32 directory and the malware samples are obtained via the MalwareBazaar API. 
## Usage
### Requirements
#### Checking a binary
(These are the specs I use, they are variable)
- Ida Pro (can be replaced with any other command line disassembler)
- Cuda 11.8
- Python 3.12 (environment)
- Transformers
#### Training the model 
- MalwareBazaar API key
### Basic Usage
You can use the code inside the main.py for a basic usage guide
### Examples
You can find examples to create a new dataset, get new samples etc. inside the examples folder.

## TODO
- [ ] Create better Documentation
- [ ] Train model on more samples
- [ ] Add PE-info to the dataset (file type, imports, packed, etc.)
- [ ] Train on different file types
- [ ] Clean up code
- [ ] Add Code comments
- [ ] More Logs
- [ ] Run the code on a Server/Website
