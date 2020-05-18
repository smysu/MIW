class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        x = open(self.file_name)
        tekst = x.read()
        print(tekst)

    def update_file(self, text_data):
        x = open(self.file_name, "a")
        x.write(text_data)


