from pathlib import Path
import os
import shutil
import re 


# Directory paths
HOME_FOLDER = Path.home()

DOWNLOADS = HOME_FOLDER / Path('Downloads')
DOWNLOADS_DOCS = DOWNLOADS / Path('Documents')
DESKTOP = HOME_FOLDER / Path('Desktop')
DOCUMENTS = HOME_FOLDER / Path('Documents')

# Checks whether a directory for download docs already exists. If not, creates the directory
if os.path.isdir(DOWNLOADS_DOCS):
    pass
else:
    DOWNLOADS_DOCS.mkdir()


# Create designated directories for specific type of files
def create_directory(path, dir_name, regex):
    directory = path / dir_name

    # Check if the directory already exists
    if os.path.isdir(directory):
        check_inside(path, directory, regex)
    else:
        directory.mkdir()
        check_inside(path, directory, regex)


# Check the files inside the directory
def check_inside(curr_dir, des_dir, regex):
    for filename in os.listdir(curr_dir):
       if regex.search(filename):
            move_file(curr_dir, des_dir, filename)


# Move the files
def move_file(curr_dir, des_dir, file_name):
    current_dir = curr_dir / file_name
    destination_dir = des_dir / file_name

    shutil.move(current_dir, destination_dir)



# Main function
def main():
    # Regular Expressions
    image_ext_regex = re.compile(r'\.jpeg$|\.jpg$|\.JPG$|\.png$|\.tiff$|\.svg$|\.gif$|\.jfif$')
    vids_ext_regex = re.compile(r'\.mp4$|\.mov$|\.MOV$')
    audio_ext_regex = re.compile(r'\.mp3$')
    code_ext_regex = re.compile(r'\.py$|\.php$|\.html$|\.sql$|\.js$|\.css$|\.java$|\.txt$')
    shortc_ext_regex = re.compile(r'\.lnk$')
    fonts_ext_regex = re.compile(r'\.ttf$')
    apps_ext_regex = re.compile(r'\.exe$|\.msi$|\.zip$')

    pdfs_regex = re.compile(r'\.pdf$')
    docs_regex = re.compile(r'\.doc$|\.docx$')
    ppts_regex = re.compile(r'\.ppt$|\.pptx$')
    excel_regex = re.compile(r'\.xls$|\.xlsx$|\.csv$')
    other_regex = re.compile(r'\.odt$|\.ods$')

    any = re.compile(r'\.[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)?$')

    # For Downloads
    create_directory(DOWNLOADS, 'Images', image_ext_regex)
    create_directory(DOWNLOADS, 'Fonts', fonts_ext_regex)
    create_directory(DOWNLOADS, 'Videos', vids_ext_regex)
    create_directory(DOWNLOADS, 'Audios', audio_ext_regex)
    create_directory(DOWNLOADS, 'Codes', code_ext_regex)
    create_directory(DOWNLOADS, 'Installables', apps_ext_regex)
    create_directory(DOWNLOADS, 'Others', any)

    # For Downloads/Documents
    create_directory(DOWNLOADS, 'Documents/PDF', pdfs_regex)
    create_directory(DOWNLOADS, 'Documents/DOCS', docs_regex)
    create_directory(DOWNLOADS, 'Documents/PPT', ppts_regex)
    create_directory(DOWNLOADS, 'Documents/EXCEL', excel_regex)
    create_directory(DOWNLOADS, 'Documents/Other File Format', other_regex)

    # For Desktop
    create_directory(DESKTOP, 'Shortcuts', shortc_ext_regex)
    create_directory(DESKTOP, 'PDF', pdfs_regex)
    create_directory(DESKTOP, 'DOCS', docs_regex)
    create_directory(DESKTOP, 'PPT', ppts_regex)
    create_directory(DESKTOP, 'EXCEL', excel_regex)
    create_directory(DESKTOP, 'Other File Format', other_regex)
    create_directory(DESKTOP, 'Images', image_ext_regex)
    create_directory(DESKTOP, 'Others', any)

    # For Documents
    create_directory(DOCUMENTS, 'PDF', pdfs_regex)
    create_directory(DOCUMENTS, 'DOCS', docs_regex)
    create_directory(DOCUMENTS, 'PPT', ppts_regex)
    create_directory(DOCUMENTS, 'EXCEL', excel_regex)
    create_directory(DOCUMENTS, 'Other File Format', other_regex)


if __name__ == "__main__":
    main()