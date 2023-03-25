import zipfile
import os

path_to_zip_file = os.path.join("data", 'kagglecatsanddogs_5340.zip')
directory_to_extract_to = os.path.join("data")

def unzip():

    print("Zipfile: ", path_to_zip_file)
    print("destination: ", directory_to_extract_to)
    print("Unzipping....")

    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)

    print("Unzipping COMPLETE!")
