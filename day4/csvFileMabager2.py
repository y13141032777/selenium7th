import  csv

class   CsvFileManager2:

    @classmethod
    def read(self):
        path = r"C:\Users\51Testing\PycharmProjects\selenium7th\data\tsetdata.csv"
        file = open(path,"r")
        data_table= csv.reader(file)
        for item in data_table:
            print(item)

if __name__ == '__main__':
    # csvread = CsvFileManager2()
    # csvread.read()
    CsvFileManager2().read()
