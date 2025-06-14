import argparse
import shutil
from pathlib import Path

def parse_arguments():
    """
    Parses command-line arguments for source and destination directories.
    """
    parser = argparse.ArgumentParser(description="Recursively copy and sort files by extension.")
    parser.add_argument("source_dir", type=str, help="Path to the source directory.")
    parser.add_argument("dest_dir", type=str, nargs='?', default="dist", 
                        help="Path to the destination directory (default: 'dist').")
    return parser.parse_args()

def copy_file_to_extension_subdir(file_path: Path, dest_base_dir: Path):
    """
    Copies a single file to a subdirectory in the destination, named after its extension.
    """
    try:
        extension = file_path.suffix[1:].lower() if file_path.suffix else "no_extension"
        
        target_subdir = dest_base_dir / extension
        
        target_subdir.mkdir(parents=True, exist_ok=True)
        
        shutil.copy2(file_path, target_subdir / file_path.name)
    except OSError as e:
        print(f"Error copying file {file_path}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while copying {file_path}: {e}")

def recursive_process_directory(source_dir: Path, dest_dir: Path):
    """
    Recursively processes a directory: copies files to sorted subdirectories in dest_dir
    and recursively calls itself for subdirectories found in source_dir.
    """
    try:
        for item in source_dir.iterdir():
            if item.is_dir():
                # If item is a directory, recurse into it
                # The destination base directory remains the same for sorting
                recursive_process_directory(item, dest_dir)
            elif item.is_file():
                # If item is a file, copy it to the appropriate extension subdirectory
                copy_file_to_extension_subdir(item, dest_dir)
    except FileNotFoundError:
        print(f"Error: Source directory {source_dir} not found.")
    except PermissionError:
        print(f"Error: Permission denied for accessing {source_dir}.")
    except Exception as e:
        print(f"An unexpected error occurred while processing directory {source_dir}: {e}")

def main_task1():
    """
    Main function for Task 1: File Sorter.
    """
    args = parse_arguments()
    
    source_path = Path(args.source_dir)
    dest_path = Path(args.dest_dir)

    print(f"Source directory: {source_path.resolve()}")
    print(f"Destination directory: {dest_path.resolve()}")

    if not source_path.is_dir():
        print(f"Error: Source path '{source_path}' is not a valid directory or does not exist.")
        return

    try:
        # The destination path itself doesn't need to exist initially,
        # subdirectories will be created within it.
        # If dest_path itself needs creation, it would be:
        # dest_path.mkdir(parents=True, exist_ok=True) 
        # But copy_file_to_extension_subdir handles subdir creation.

        print(f"Starting file sorting process...")
        recursive_process_directory(source_path, dest_path)
        print("File sorting process completed.")
        print(f"Files have been sorted into: {dest_path.resolve()}")

    except Exception as e:
        print(f"A critical error occurred: {e}")

# --- Helper for testing Task 1 ---
def create_test_source_dir_for_task1(base_path_str="temp_source_task1"):
    source = Path(base_path_str)
    if source.exists():
        shutil.rmtree(source) # Clean up previous test
    source.mkdir(parents=True, exist_ok=True)

    (source / "file1.txt").write_text("text content 1")
    (source / "image_alpha.JPG").write_text("jpeg image data") # Test uppercase extension
    (source / "archive.zip").write_text("zip archive data")
    (source / "document_final").write_text("file with no extension") # Test no extension

    sub_dir1 = source / "documents"
    sub_dir1.mkdir()
    (sub_dir1 / "report.pdf").write_text("pdf content")
    (sub_dir1 / "notes.txt").write_text("more text content")

    sub_dir2 = source / "media"
    sub_dir2.mkdir()
    (sub_dir2 / "song.mp3").write_text("audio data")
    
    sub_sub_dir = sub_dir2 / "photos"
    sub_sub_dir.mkdir()
    (sub_sub_dir / "holiday.jpeg").write_text("another jpeg")
    (sub_sub_dir / "script.py").write_text("print('hello')")
    (sub_sub_dir / ".config_hidden").write_text("hidden file content") # Test hidden file

    print(f"Test source directory for Task 1 created at {source.resolve()}")
    return source.name # Return the name for command line usage


if __name__ == "__main__":
    main_task1()