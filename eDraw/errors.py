class eDrawError(Exception):
    """Base class for exceptions in eDraw."""
    pass

class AddError(eDrawError):
    """
    Raised when attempting to add object to wrong class.
    """
    def __init__(self, msg):
        self.msg = msg

class FormatError(eDrawError):
    """
    Raised when attempting to save in an unsupported format.
    """
    def __init__(self, msg):
        self.formats=["ely", "svg"]
        self.msg = msg
