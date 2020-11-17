class FplError(Exception):
    """Base exception class for all internal errors."""
    def __init__(self, message):
        """
        :param message:
            Error string for this exception.
        """
        super().__init__(message)


class FetchError(FplError):
    """Error fetching JSON data via HTTP."""
    def __init__(self, message):
        """
        :param message:
            Error string for this exception.
        """
        super().__init__(message)


class JSONError(FplError):
    """Error with the structure of the downloaded JSON."""
    def __init__(self, message):
        """
        :param message:
            Error string for this exception.
        """
        super().__init__(message)
