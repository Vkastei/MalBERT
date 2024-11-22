import os 

IDA_PATH = ""

class Disassembler:
    
    def __init__(self):
        self.disassemble_ida = "disassemble_ida.py"
        
    def loop_malware_samples(self):
        os.chdir("data/samples")
        script_dir = os.getcwd()
        print(script_dir)
        for filename in os.listdir(script_dir):
            if(os.path.isfile(filename) and filename != self.disassemble_ida and not filename.endswith(".txt") and filename != "dataset.csv"):
                self._disassemble_binary(filename, 0)

    def loop_benign_samples(self):
        os.chdir("data/samples")
        script_dir = os.getcwd()
        for filename in os.listdir(script_dir):
            if(os.path.isfile(filename) and filename.endswith(".exe")):
                self._disassemble_binary(filename, 1)
    def _disassemble_binary(self, filename, file_type):
        
        # disassemble the binary using ida pro 
        ida_cmd = IDA_PATH + " -A -S\"" + self.disassemble_ida + "\" " + filename
        print(ida_cmd)
        os.system(ida_cmd)

        self.clear_binaries(filename, file_type)

    def disassemble_binary(self, filename):
        ida_cmd = IDA_PATH + " -A -S\"" + self.disassemble_ida + "\" " + filename
        os.system(ida_cmd)
        self.clear_binaries(filename,1)
    def clear_binaries(self, filename, file_type):
        file_name, file_extension = os.path.splitext(filename)
        # file_type 0 = malware, file_type 1 = benign
        if(file_type == 0):
            os.rename("output_instructions_temp.txt", "0" + file_name + ".txt")
            os.remove((file_name + ".bin"))
            os.remove((file_name + ".bin.i64"))
        if(file_type == 1):
            os.rename("output_instructions_temp.txt", "1" + file_name + ".txt")
            os.remove((file_name + ".exe"))
            os.remove((file_name + ".exe.i64"))
    def add_disassemble_to_csv(self):
        pass
