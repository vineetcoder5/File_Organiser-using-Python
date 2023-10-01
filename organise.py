import os
import shutil
from datetime import date
import time


# enter the Folder path of the folder
path = "your folder path"



dir = os.listdir(path)
image = "Images"
pdf = "PDF"
docs = "Documents"
imgpath = os.path.join(path,image)
pdfpath = os.path.join(path,pdf)
docpath = os.path.join(path,docs)

#  all files extensions in differnet list

img_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".raw", ".psd", ".svg", ".webp", ".heic", ".heif", ".exif", ".pnm", ".ico", ".cur", ".wmf", ".emf", ".hdr", ".jfif"]
pdf_extensions = [".pdf"]
video_extensions = [".mp4", ".avi", ".mkv", ".wmv", ".mov", ".flv", ".mpg", ".webm", ".3gp", ".ogv", ".flv", ".asf", ".mpg", ".mp2", ".ts", ".m2ts", ".vob", ".divx", ".wav", ".ogv", ".mpv"]
text_document_extensions = [".txt", ".rtf"]
word_document_extensions = [".doc", ".docx", ".odt"]
spreadsheet_extensions = [".xls", ".xlsx", ".ods"]
presentation_extensions = [".ppt", ".pptx", ".odp"]
html_extensions = [".html"]
xml_extensions = [".xml"]
markdown_extensions = [".md"]
csv_extensions = [".csv"]
json_extensions = [".json"]
plain_text_extensions = [".nfo", ".log"]
database_extensions = [".sql", ".db"]
compressed_extensions = [".zip", ".rar", ".7z",".tar.gz"]
executable_extensions = [".exe"]

        

extension_to_category = {
    extension: "Images" for extension in img_extensions
}
extension_to_category.update({extension: "PDF" for extension in pdf_extensions})
extension_to_category.update({extension: "Videos" for extension in video_extensions})
extension_to_category.update({extension: "Text Documents" for extension in text_document_extensions})
extension_to_category.update({extension: "Word Documents" for extension in word_document_extensions})
extension_to_category.update({extension: "Spreadsheets" for extension in spreadsheet_extensions})
extension_to_category.update({extension: "Presentations" for extension in presentation_extensions})
extension_to_category.update({extension: "HTML" for extension in html_extensions})
extension_to_category.update({extension: "XML" for extension in xml_extensions})
extension_to_category.update({extension: "Markdown" for extension in markdown_extensions})
extension_to_category.update({extension: "CSV" for extension in csv_extensions})
extension_to_category.update({extension: "JSON" for extension in json_extensions})
extension_to_category.update({extension: "Plain Text" for extension in plain_text_extensions})
extension_to_category.update({extension: "Databases" for extension in database_extensions})
extension_to_category.update({extension: "Compressed" for extension in compressed_extensions})
extension_to_category.update({extension: "Executables" for extension in executable_extensions})


for i in dir:
    extension = os.path.splitext(i)[1]
    category = extension_to_category.get(extension, "Other")
    file_path = os.path.join(path,i)
    if(category != "Other" ):
        try:
            ext_path = os.path.join(path,category)
            os.mkdir(ext_path)
        except:
            print("already created")
        try:
            shutil.move(file_path, ext_path)
        except:
            print("file not moved")

        
    
