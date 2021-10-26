import shutil

shutil.make_archive('mydata', 'zip', 'DATA')
shutil.make_archive('mydata', 'tar', 'DATA')
shutil.make_archive('mydata', 'gztar', 'DATA')


