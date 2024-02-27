import os
# traversing files in Python
# https://pieriantraining.com/iterate-over-files-in-directory-using-python/#:~:text=The%20most%20common%20way%20to,all%20files%20in%20the%20directory.

directory = '/Users/jasongyamfi/Desktop/Comp_Sci_203/exemplarproject-gyamfi01/data/corpus'
for filename in os.listdir(directory):
    if filename.endswith('.xml'):
        with open(os.path.join(directory, filename)) as f:
            print(f.read())