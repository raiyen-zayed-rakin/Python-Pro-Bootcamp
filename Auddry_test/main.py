import os
import re


def sanitize_folder_name(folder_name):
    """
    Sanitize folder name to remove invalid characters for Windows.

    Parameters:
    - folder_name: The original folder name.

    Returns:
    - A sanitized folder name.
    """
    invalid_chars = r'[<>:"/\\|?*]'
    sanitized_name = re.sub(invalid_chars, '_', folder_name)
    return sanitized_name


def create_folders_from_text(file_path, base_directory='.'):
    """
    Reads a text file and creates a nested folder structure based on the contents.
    Each sub-question folder (`a`, `b`, `c`, `d`) will be named after the full text of the sub-question.

    Parameters:
    - file_path: Path to the text file containing folder names.
    - base_directory: The directory where the folders will be created. Defaults to current directory.
    """
    if not os.path.exists(base_directory):
        os.makedirs(base_directory)

    try:
        with open(file_path, 'r') as file:
            current_group = None
            current_question = None
            current_sub_question = None
            sub_question_content = {}

            for line in file:
                line = line.strip()

                if line.startswith("Group-"):
                    # Handle group folders
                    current_group = sanitize_folder_name(line)
                    group_path = os.path.join(base_directory, current_group)
                    if not os.path.exists(group_path):
                        os.makedirs(group_path)
                        print(f"Created folder: {group_path}")

                elif line.startswith("Q. N. "):
                    # Handle question folders
                    if current_group is not None:
                        current_question = sanitize_folder_name(line)
                        question_path = os.path.join(base_directory, current_group, current_question)
                        if not os.path.exists(question_path):
                            os.makedirs(question_path)
                            print(f"Created folder: {question_path}")
                        # Initialize dictionary to store sub-question content
                        sub_question_content = {'a': '', 'b': '', 'c': '', 'd': ''}

                elif line and line[0] in 'abcd':
                    # Start collecting content for a new sub-question
                    current_sub_question = line[0]
                    content = line[2:]  # Content after the sub-question label
                    if current_sub_question in sub_question_content:
                        sub_question_content[current_sub_question] = content

                elif current_group and current_question and current_sub_question:
                    # Append content to the current sub-question
                    if current_sub_question in sub_question_content:
                        sub_question_content[current_sub_question] += '\n' + line

            # Create folders for each sub-question with content as folder name
            for group in os.listdir(base_directory):
                group_path = os.path.join(base_directory, group)
                if os.path.isdir(group_path):
                    for question in os.listdir(group_path):
                        question_path = os.path.join(group_path, question)
                        if os.path.isdir(question_path):
                            for sub_question, content in sub_question_content.items():
                                if content:  # Only create folders if there is content
                                    sub_path = os.path.join(question_path, sanitize_folder_name(content))
                                    if not os.path.exists(sub_path):
                                        os.makedirs(sub_path)
                                        print(f"Created folder: {sub_path}")
                                    # Save content to a text file in each sub-question folder
                                    content_file_path = os.path.join(sub_path, f"{sub_question}.txt")
                                    with open(content_file_path, 'w') as content_file:
                                        content_file.write(content)
                                        print(f"Created file with content in: {content_file_path}")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Path to the text file and base directory
    file_path = '2022.txt'  # Change this to the path of your txt file
    base_directory = './2022'  # Change this to your desired base directory

    create_folders_from_text(file_path, base_directory)
