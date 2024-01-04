import os
import shutil

# Function to classify files
def classify_files(folder_path):
    # Get the list of files in the download folder
    files = os.listdir(folder_path)

    # Create folders for different file types if they don't exist
    image_folder = os.path.join(folder_path, 'Images')
    pdf_folder = os.path.join(folder_path, 'PDFs')
    msoffice_folder = os.path.join(folder_path, 'MSOffice')
    video_folder = os.path.join(folder_path, 'Videos')
    other_folder = os.path.join(folder_path, 'Other')

    for file in files:
        file_path = os.path.join(folder_path, file)

        # Check if the file is an image
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            if not os.path.exists(image_folder):
                os.makedirs(image_folder)
            shutil.move(file_path, os.path.join(image_folder, file))
            print(f"Moved {file} to Images folder")

        # Check if the file is a PDF
        elif file.lower().endswith('.pdf'):
            if not os.path.exists(pdf_folder):
                os.makedirs(pdf_folder)
            shutil.move(file_path, os.path.join(pdf_folder, file))
            print(f"Moved {file} to PDFs folder")

        # Check if the file is an MS Office file
        elif file.lower().endswith(('.docx', '.xlsx', '.pptx')):
            if not os.path.exists(msoffice_folder):
                os.makedirs(msoffice_folder)
            shutil.move(file_path, os.path.join(msoffice_folder, file))
            print(f"Moved {file} to MSOffice folder")

        # Check if the file is a video file
        elif file.lower().endswith(('.mp4', '.avi', '.mkv', '.mov')):
            if not os.path.exists(video_folder):
                os.makedirs(video_folder)
            shutil.move(file_path, os.path.join(video_folder, file))
            print(f"Moved {file} to Videos folder")

        # Move files that are not in the specified categories to the 'Other' folder
        else:
            if os.path.isdir(file_path):
                # Skip if it's an existing folder
                continue
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(file_path, os.path.join(other_folder, file))
            print(f"Moved {file} to Other folder")

# Folder path
download_folder = r'C:\Users\arshi\Downloads\File_Serparation_Project'

classify_files(download_folder)
