import shutil, os

root = 'C:'
if not os.path.exists(root + '\\Images'):
    os.makedirs(root + '\\Images')
if not os.path.exists(root + '\\Videos'):
    os.makedirs(root + '\\Videos')
if not os.path.exists(root + '\\Text'):
    os.makedirs(root + '\\Text')

img = ['.JPG', '.JPEG', '.PNG', '.jpg', '.jpeg']
vid = ['.MP4', '.mkv', '.MOV']
txt = ['.rtf', '.txt', '.doc', '.docx', '.ppt', '.pptx', '.xlsx', '.xls', '.pdf']

try:
    for folders, subfolders, filenames in os.walk(root):
        for filename in filenames :
            for i in img:
                if filename.endswith(i):
                    shutil.move(root + '\\' + filename, root + '\\Images')
            for j in vid:
                if filename.endswith(j):
                    shutil.move(root + '\\' + filename, root + '\\Videos')
            for k in txt:
                if filename.endswith(k):
                     shutil.move(root + '\\' + filename, root + '\\Text')        

except:
    None



