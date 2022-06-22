from datetime import datetime
import zipfile

# The compress_zip function gives us a name to the file using the current date, and compresses the file in the path /files_compress
def compress_zip(response):
    date = datetime.now()
    name_file = f"data{str(date)}.zip"
    with zipfile.ZipFile(f"./files_compress/{name_file}", "a") as zfp:
        zfp.writestr("data.txt", str(response))
