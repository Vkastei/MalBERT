import csv
from preprocessing import disassembler
from dotenv import load_dotenv
import os
import requests
import json 
import shutil
import pandas
import pyzipper 
import pandas

class CreateDataset:
    headers = {}
    training_size = 50
    
    def __init__(self):
        load_dotenv()

    def _send_api_request(self, data):
        response = requests.post('https://mb-api.abuse.ch/api/v1/', headers=self.headers, data=data)
        return response
    
    def _set_api_header(self):

        print("Setting Malware bazaar API key")
        access_key = os.getenv("ABUSE_CH_AUTH_KEY")

        headers = {"Auth-Key": access_key}
    def _download_sample_and_extract(self, data, hash):
        self._set_api_header()

        script_dir = os.path.dirname(__file__)
        filepath = os.path.join(script_dir, "samples", hash + '.zip')

        if(os.path.isfile(filepath)):
            return
        
        response = requests.post('https://mb-api.abuse.ch/api/v1/',
                           headers=self.headers,
                             data=data, 
                             timeout=15, 
                             allow_redirects=True)
        
        open(filepath, 'wb').write(response.content)

        raw_data_path = os.path.split(filepath)[0]
        with pyzipper.AESZipFile(filepath) as zf:
                pwd = "infected"
                zf.pwd = pwd
                samples = zf.extractall(raw_data_path, pwd = 'infected'.encode('cp850','replace'))  

        # rename sample to .bin so its non executable anymore
        os.chdir(raw_data_path)
        os.rename(hash + '.exe', hash + ".bin")
        os.remove(hash + '.zip')

        print("Successfully downloaded and extracted malware sample: " + hash)
        

    def create_malware_samples(self):
        print("Creating malware samples...")
        print("Downloading 1000 malware samples with tag: exe")

        # Receive last 1000 .exe samples from malwarebazaar
        data = {
            'query' : 'get_taginfo',
            'tag' : 'exe',
            'limit' : 20
        }
        response = self._send_api_request(data).json()

        samples_hashes = [item["sha256_hash"] for item in response["data"]]

        # Download the samples to /raw/ and extract them
        for hash in samples_hashes:
            data = {
                'query' : 'get_file',
                'sha256_hash': hash
            }
            print("Downloading sample: " + str(hash))
            file = self._download_sample_and_extract(data, hash)


    def create_benign_samples(self):
        print("Creating benign samples...")
        os.chdir("data/samples")
        system32_dir = "C:/Windows/System32"
        i = 0
        for filename in os.listdir(system32_dir):
            if(filename.endswith(".exe")):
                i += 1
                file_path = system32_dir + "/" + filename
                script_path = os.getcwd()
                print(script_path)
                shutil.copy(file_path, script_path)    
        print("Successfully received " + str(i) + " benign .exe samples from C:/Windows/System32")

    def create_training_dataset_csv(self, size):
        i = 0
        with open('dataset.csv', 'w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            field = ["label", "text"]
            writer.writerow(field)
            for filename in os.listdir(os.getcwd()):
                if(filename.endswith(".txt")):
                    i+=1
                    data = ""
                    with open(filename, 'r', encoding="utf-8") as sample:
                        data = sample.read().replace("\n", " ")
                    sample_type = ""
                    if(filename[0] == "0"):
                        sample_type = "malware"
                    elif (filename[0] == "1"):
                        sample_type = "benign"
                    if(sample_type != ""):
                        writer.writerow([sample_type, data])

        if(i < size):
            print("Not enough samples found, reduce size or create new samples by running Datasets.create_benign_samples or Datasets.create_malware_samples")
        else:
            print("Successfully created new dataset.csv containing benign & malware samples")

    def create_training_dataset(self):
        data_file = "dataset.csv"
        df = pandas.read_csv(data_file, encoding='ISO-8859-1')
        texts = df['text'].tolist()
        labels = [1 if label  == "benign" else 0 for label in df['label'].tolist()]
        return texts, labels

    


    
