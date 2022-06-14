import dropbox
class TransferData :
    def __init__(self,acess_token):
        self.acess_token = acess_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.acess_token)
        f=open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)
def main():
    acess_token = "sl.BJiUs2bFRKFwZ-6tRSp2H70NbhMOQJ46O-loApVjnzHlDbLPpWnis24JzYxFeHZ9tgklY8TqLmamlkjsR0-9NcuyTUoPiIwOqY4S8MgOIa9spV6SE_q_2rah8f4aeshd3qw_RkSM2K65"
    transferData=TransferData(acess_token)
    file_from=input("ENTER THE FILE PATH TO TRANSFER.....")
    file_to=input("ENTER THE FULL PATH TO UPLOAD TO DROPBOX......")
    transferData.upload_file(file_from,file_to)
    print("THE FILE HAVE BEEN MOVED :)")
main()