"""Core file organization logic."""

import os
import shutil


def create_directory_if_not_exists(directory):
    """Create a directory if it does not exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)


def organize_files(source_directory, type_mappings):
    """
    Organize files in source_directory based on type_mappings.
    
    Args:
        source_directory (str): Path to the directory containing files to organize.
        type_mappings (dict): Dictionary mapping file extensions to destination directories.
    
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        for filename in os.listdir(source_directory):
            file_path = os.path.join(source_directory, filename)
            if os.path.isfile(file_path):
                file_extension = filename.split('.')[-1].lower()

                if file_extension in type_mappings:
                    destination_directory = type_mappings[file_extension]
                else:
                    destination_directory = type_mappings.get('other', os.path.join(source_directory, 'other_files'))

                create_directory_if_not_exists(destination_directory)
                shutil.move(file_path, os.path.join(destination_directory, filename))

        return True, "Files organized successfully!"
    except Exception as e:
        return False, f"An error occurred: {str(e)}"
