class InvalidOutputFile(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class FileDirectoryDoesNotExist(InvalidOutputFile):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class FileAlreadyExists(InvalidOutputFile):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NoDesiredExtention(InvalidOutputFile):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

