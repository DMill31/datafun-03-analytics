"""
Process a text file to count occurrences of the phrase "Great Scott" and save the result.
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "data"
processed_folder_name: str = "data_processed"

#####################################
# Define Functions
#####################################

def count_phrase_occurrences(file_path: pathlib.Path, phrase: str) -> int:
    """Count the occurrences of a specific word in a text file (case-insensitive)."""
    try:
        with file_path.open('r') as file:
            content: str = file.read()
            return content.lower().count(phrase.lower())
    except Exception as e:
        logger.error(f"Error reading text file: {e}")
        return 0

def process_text_file():
    """Read a text file, count occurrences of 'Great Scott', and save the result."""
    input_file = pathlib.Path(fetched_folder_name, "BTTF.txt")
    output_file = pathlib.Path(processed_folder_name, "text_great_scott_count.txt")
    phrase_to_count: str = "Great Scott"
    phrase_count: int = count_phrase_occurrences(input_file, phrase_to_count)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open('w') as file:
        file.write(f"Occurrences of '{phrase_to_count}': {phrase_count}\n")
    logger.info(f"Processed text file: {input_file}, Word count saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting text processing...")
    process_text_file()
    logger.info("Text processing complete.")