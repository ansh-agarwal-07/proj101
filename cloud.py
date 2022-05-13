import dropbox 
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root,dirs,files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root,filename)
                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,relative_path)
                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))
                
       
        
    
def main():
    access_token = "sl.BHgvaq4hGKWN6UY3e07p7plfzhuNMwLaq7muAgA9x28KpWC9hDzlrqvv_qxxd66f67Nx3S_gLFTHi0rFham8T4K30bTzM4bxVAF2Ss__lumcRAf-WnKtcL_f_eChrvdpKp7iqfSzrAh3"
    transferData = TransferData(access_token)
    file_from = str(input("enter the file path to transfer "))
    file_to = input("full path to upload to dropbox ")
    transferData.upload_file(file_from,file_to)
    print("file has been moved ")

main()

