import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path=os.path.join(root,filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path, mode=WriteMode('overwrite'))
def main():
    access_token = "sl.A_t1pPo1ahceJaNh3IdAA1TLJS4kb2T75Uf6kTufKn3rGXoMSLuq09ywbkjTmH3pwVNBVTUzexG1P-gGPORxabevHBLzeV9PNObxXWPXog3hrxG1gfs4vFVheBAneb7RjNvEfuOq"
    transferdata = TransferData(access_token)
    file_from = input("Enter the folder path to upload:")
    file_to = input("Enter the full path to upload:")
    transferdata.upload_file(file_from,file_to)
    print("The folder has been uploaded")
main()