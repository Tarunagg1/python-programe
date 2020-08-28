import os

def createfolder(folder):
  if not os.path.exists(folder):
    os.makedirs(folder) 

files = os.listdir()
files.remove("cleaner.py")
print(files)

createfolder("docs")    
createfolder("html")    

imgext = [".img",".png",".jpg",".jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgext]

docstext = [".txt",".doc",".docx",".pdf"]
doc = [file for file in files if os.path.splitext(file)[1].lower() in docstext]
print(images)
print(doc)
