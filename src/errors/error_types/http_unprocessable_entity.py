class HttpUnprocessableEntiyError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.staus_code = 422
        self.name = 'UnprocessableEntiy'
        self.message = message
