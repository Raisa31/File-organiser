import shutil, os

root = 'C:\\Users\\Raisa Arief\\Desktop\\SEMICOLON\\Software dev\\Sample folder'
if not os.path.exists(root + '\\Images'):
    os.makedirs(root + '\\Images')
if not os.path.exists(root + '\\Videos'):
    os.makedirs(root + '\\Videos')
if not os.path.exists(root + '\\Text'):
    os.makedirs(root + '\\Text')
if not os.path.exists(root + '\\Office'):
    os.makedirs(root + '\\Office')
    


for filename in os.listdir(root):
    if filename.endswith('.txt'): 
        shutil.move(root + '\\' + filename, root + '\\Text')
    if filename.endswith('.rtf') or filename.endswith('.docx') or filename.endswith('.doc') or filename.endswith('.pptx') or filename.endswith('.xlsx'):
        shutil.move(root + '\\' + filename, root + '\\Office')
    if filename.endswith('.JPG') or filename.endswith('JPEG') or filename.endswith('PNG'):
        shutil.move(root + '\\' + filename, root + '\\Images')
    if filename.endswith('.MP4') or filename.endswith('mkv') or filename.endswith('MOV'):
        shutil.move(root + '\\' + filename, root + '\\Videos')


'''
for filename in os.listdir('C:\\Users\\Raisa Arief\\Desktop\\SEMICOLON\\Software dev\\Sample folder'):
    if filename.charAt(0) == 'a'
        shutil.move('C:\\Users\\Raisa Arief\\Desktop\\SEMICOLON\\Software dev\\Sample folder\\' + filename, 'C:\\Users\\Raisa Arief\\Desktop\\SEMICOLON\\Software dev\\Sample folder\\Text')
'''

