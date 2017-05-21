import glob, os
from shutil import copyfile

dst='destination_dir'
os.chdir('source_dir')
for file in glob.glob("**/*.py", recursive=True):
    
    filename=file.split('/')[-1]
    copyfile(file, os.path.join(dst, filename))
