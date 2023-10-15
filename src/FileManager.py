import os

class FileManager:
    def __init__(self, base_path):
        self.base_path = base_path

    def create_file(self, file_name, content=""):
        file_path = self._get_full_path(file_name)
        try:
            with open(file_path, 'w') as file:
                file.write(content)
            return f'File "{file_name}" created successfully.'
        except IOError as e:
            return f'Error: {e}'

    def read_file(self, file_name):
        file_path = self._get_full_path(file_name)
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except IOError as e:
            return f'Error: {e}'

    def write_file(self, file_name, content):
        file_path = self._get_full_path(file_name)
        try:
            with open(file_path, 'w') as file:
                file.write(content)
            return f'File "{file_name}" updated successfully.'
        except IOError as e:
            return f'Error: {e}'

    def _get_full_path(self, file_name):
        return os.path.join(self.base_path, file_name)

# Example usage:
if __name__ == '__main__':
    file_manager = FileManager('/path/to/your/specified/folder')

    result = file_manager.create_file('example.txt', 'Hello, World!')
    print(result)

    content = file_manager.read_file('example.txt')
    print(f'Read file content: {content}')

    result = file_manager.write_file('example.txt', 'Updated content.')
    print(result)

    content = file_manager.read_file('example.txt')
    print(f'Read updated file content: {content}')
