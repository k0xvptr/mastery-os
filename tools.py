from pathlib import Path
import os

base_dir = Path("Data")


# common tools

def read_file(name: str) -> str:
    """Return file content. If not exist, return error message.
    """
    print(f"(read_file {name})")
    try:
        with open(base_dir / name, "r", encoding='utf-8') as f:
            content = f.read()
        return content
    except Exception as e:
        return f"An error occurred: {e}"


def list_files() -> list[str]:
    """
    return: File name availble in Data
    """
    print("(list_file)")
    file_list = []
    for item in base_dir.rglob("*"):
        if item.is_file():
            file_list.append(str(item.relative_to(base_dir)))
    return file_list


def rename_file(name: str, new_name: str) -> str:
    """
    Simply chaneg a file's name
    :param name: The file name to change from
    :param new_name: The goal name
    """

    print(f"(rename_file {name} -> {new_name})")
    try:
        new_path = base_dir / new_name
        if not str(new_path).startswith(str(base_dir)):
            return "Error: new_name is outside base_dir."

        os.makedirs(new_path.parent, exist_ok=True)
        os.rename(base_dir / name, new_path)
        return f"File '{name}' successfully renamed to '{new_name}'."
    except Exception as e:
        return f"An error occurred: {e}"


def make_file(name: str, content: str = "") -> str:
    """Create a new file with the given name and content.
    Returns success message or error.
    """
    print(f"(make_file {name})")
    try:
        file_path = base_dir / name
        if not str(file_path).startswith(str(base_dir)):
            return "Error: filename is outside base_dir."

        # Create parent directories if they don't exist
        os.makedirs(file_path.parent, exist_ok=True)

        with open(file_path, "w", encoding='utf-8') as f:
            f.write(content)

        return f"File '{name}' successfully created."
    except Exception as e:
        return f"An error occurred: {e}"


def change_file(name: str, new_content: str) -> str:
    """Replace the entire content of an existing file with new content.
    Returns success message or error.
    """
    print(f"(change_file {name})")
    try:
        file_path = base_dir / name
        if not file_path.exists():
            return f"Error: File '{name}' does not exist."

        if not str(file_path).startswith(str(base_dir)):
            return "Error: filename is outside base_dir."

        with open(file_path, "w", encoding='utf-8') as f:
            f.write(new_content)

        return f"File '{name}' successfully updated with new content."
    except Exception as e:
        return f"An error occurred: {e}"


#Query Tools
def get_chunks(file_name) -> list[str]:
    '''
    Split the file infomation given the location into chucks of materials
    :param file_name: The file location
    :return: Information after proccess
    '''
    try:
        content = read_file(file_name)
    except Exception as e:
        return f"An error occurred: {e}"
    chunks = content.split('\n\n')

    result = []
    header = ""
    for c in chunks:
        if c.startswith("#"):
            header += f"{c}\n"
        else:
            result.append(f"{header}{c}")
            header = ""

    return result