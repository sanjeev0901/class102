import time,cv2,random,dropbox
from unicodedata import name

startTime=time.time()

def takeSnapshot():
    number=random.randint(0,1000)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while (result):
        ret,frame=videoCaptureObject.read()
        imageName="img"+str(number)+".png"
        cv2.imwrite(imageName,frame)
        startTime=time.time()
        result=False
    print("Image Saved",imageName)
    videoCaptureObject.release()
    #videoCaptureObject.destroyAllWindows()
    return imageName
    

def uploadToDropbox(imageName):
    accessToken="sl.BF9YGtNNhjb0JIJ2JBEa5uGcr5MsOCcQuDhIQaqq4UC7WILPgpYSmo1ETDbV2kQNXX6R7tlUH9JuWgYo63kRR51o5z0YLyWb8EsEgieDAKVkkfZ9HAeSfWb5Lv_R3soTNTb4mFo"
    file=imageName
    fileFrom=file
    fileTo="/class102/"+file
    dbx=dropbox.Dropbox(accessToken)
    with open(fileFrom,"rb") as f:
        dbx.files_upload(f.read(),fileTo,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")
        
def main():
    while True:
        if (time.time()-startTime)>=10:
            name=takeSnapshot()
            uploadToDropbox(name)

if __name__=="__main__":
    main()

    
    

