import random
import dropbox
import time
import os


start_time = time.time()



access_token = "fRhj7mPtPagAAAAAAAAAASeTXJfQ0o5I-fN8jYHQ5q7F5Pajc8JArs3srMlzpn2s"

"""file_from = "D:/WhiteHat/Projects/Python/txt/test.txt"
file_to="/AUTOMATION-P102/"+"file1.txt"
dbx = dropbox.Dropbox(access_token)

with open(file_from, 'rb') as f:
      dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
      print("file uploaded")"""
while True:
  if ((start_time - time.time()) <= 60 ):
     number = random.randint(0,100)
     name = "file"+ str(number)+".txt"
    
     if not os.path.exists(name):
            open(name,'a').close()

     file = name
     file_to = "/AUTOMATION-P102/"+name


     dbx = dropbox.Dropbox(access_token)

     with open(file, 'rb') as f:
            dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
            print(name+" uploaded")

"""elif ((start_time - time.time()) >= 300 ):

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


   



