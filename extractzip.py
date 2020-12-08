from zipfile import ZipFile, is_zipfile
from os import path
from tqdm import tqdm

filetoextract = "zip_10MB.zip"

# Begin extracting the file if it exists
if path.exists(filetoextract):
    if is_zipfile(filetoextract):
        print("Valid ZIP file")
        print(f"Extracting: {filetoextract}")
        with ZipFile(filetoextract,"r") as zip_ref:
            for file in tqdm(iterable=zip_ref.namelist(), total=len(zip_ref.namelist())):
                zip_ref.extract(member=file)
    else:
        print("Not valid ZIP file")
else:
    print(f"Cannot find: {filetoextract}")