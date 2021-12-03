import dropbox
import time


start_time = time.time()

access_token = 'fRhj7mPtPagAAAAAAAAAASeTXJfQ0o5I-fN8jYHQ5q7F5Pajc8JArs3srMlzpn2s'
         
file_from = "D:/WhiteHat/Projects/Python/txt/test.txt"

file_to = "/AUTOMATION-P102/"     

while True:   


    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to)

    print("uploaded1")


"""if ((start_time - time.time()) >= 3 ):


     file_from = open("file1.txt" , 'w')
     file_from.write("hi this is sai charan")
     file_from.close()       

     file_to = "/AUTOMATION-P102/"


     dbx = dropbox.Dropbox(access_token)

     with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
                
            print("uploaded")

elif ((start_time - time.time()) >= 300 ):

     file_from = open("file2.txt" , 'w')
     file_from.write("hi ")
     file_from.close()

     file_to = "/AUTOMATION-P102/"


     dbx = dropbox.Dropbox(access_token)

     with open(file_from, 'rb') as f:
           dbx.files_upload(f.read(), file_to)
                 
           print("uploaded")

elif ((start_time - time.time()) >= 3600 ):

            file_from = open("file3.txt" , 'w')
            file_from.write("math ")
            file_from.close()

            file_to = "/AUTOMATION-P102/"


            dbx = dropbox.Dropbox(access_token)

            with open(file_from, 'rb') as f:
                 dbx.files_upload(f.read(), file_to)
                 
                 print("uploaded")

elif ((start_time - time.time()) >=7200 ):

            file_from = open("file4.txt" , 'w')
            file_from.write("telugu ")
            file_from.close()

            file_to = "/AUTOMATION-P102/"


            dbx = dropbox.Dropbox(access_token)

            with open(file_from, 'rb') as f:
                 dbx.files_upload(f.read(), file_to)
                 
                 print("uploaded")

elif ((start_time - time.time()) >=10800 ):

            file_from = open("file4.txt" , 'w')
            file_from.write(" AI ")
            file_from.close()

            file_to = "/AUTOMATION-P102/"


            dbx = dropbox.Dropbox(access_token)

            with open(file_from, 'rb') as f:
                 dbx.files_upload(f.read(), file_to)
                 
                 print("uploaded")"""


   



