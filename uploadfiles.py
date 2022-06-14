import dropbox

class TransferData:

    def __init__(self,access_token):
        self.access_token = access_token
    
    def upload_file(self,filefrom,fileto):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(filefrom,'rb')
        dbx.files_upload(f.read(),fileto)
    
def main():
    access_token = "sl.BJXDH1AxY1ItOvJtEtZi6YypcJ54ByJjQtbzaFsexSPh5xOORmSmTMzchz_ygkJqSAUtBhFKUwgkGzPXlw505UiS_syLD3rMVu818gDfwRsGNjx8xdDZlY1FwuEzonzYungPVaF2HHcvsl.BJXDH1AxY1ItOvJtEtZi6YypcJ54ByJjQtbzaFsexSPh5xOORmSmTMzchz_ygkJqSAUtBhFKUwgkGzPXlw505UiS_syLD3rMVu818gDfwRsGNjx8xdDZlY1FwuEzonzYungPVaF2HHcsl.BJXDH1AxY1ItOvJtEtZi6YypcJ54ByJjQtbzaFsexSPh5xOORmSmTMzchz_ygkJqSAUtBhFKUwgkGzPXlw505UiS_syLD3rMVu818gDfwRsGNjx8xdDZlY1FwuEzonzYungPVaF2HHc"
    transferData = TransferData(access_token)
    filefrom = input("Enter the file path to transfer: ")
    fileto = input("Enter the file path to upload to dropbox: ")
    transferData.upload_file(filefrom,fileto)
    print("File has been moved.")

main()