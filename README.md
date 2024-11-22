# MalBERT
MalBERT is a project to detect malware with a fine tuned BERT model, trained on disassembled samples of malware and benign binaries.

Currently the Model is trained on around 500 via IDA Pro disassembled benign and malware executables. The benign samples are just copied from the System32 directory and the malware samples are obtained via the MalwareBazaar API. 

> [!WARNING]  
> This repository contains code that is able to download & extract malware. Demanding user attention due to potential risk of being infiltrated.
> Dont run code you don't understand.

## Training

![image](https://github.com/user-attachments/assets/ad0bab11-6cdf-4e58-9786-33f015077803)

## Usage
### Requirements
(These are the specs I use, they are variable)
- Ida Pro (can be replaced with any other command line disassembler)
- Cuda 11.8
- Python 3.12 (environment)
- Transformers
#### Training the model 
- MalwareBazaar API key
### Basic Usage
Locate the root directory of the branch.
#### Creating new samples and dataset (.csv)
This command creates 500 samples of benign and malware files, disassembles them and saves the content inside a dataset.csv-
The samples are deleted afterwards.
```python -m examples.create_samples_and_dataset_csv.py```
#### Training the model
```python -m examples.train_model```
## TODO
- [ ] Create better Documentation
- [ ] Train model on more samples
- [ ] Add PE-info to the dataset (file type, imports, packed, etc.)
- [ ] Train on different file types
- [ ] Clean up code
- [ ] Add Code comments
- [ ] More Logs
- [ ] Run the code on a Server/Website

## Contributing
If you want to contribute to this project, just text me on discord: @hardstuckvini

## References
- Base of the Model : https://medium.com/@khang.pham.exxact/text-classification-with-bert-7afaacc5e49b
- BERT Language Model : https://huggingface.co/docs/transformers/model_doc/bert
- Malware Bazaar API : https://bazaar.abuse.ch/api/
- IDA Pro Disassembler : https://hex-rays.com/ida-pro
