from tap import Tap

class SplitterArgs(Tap):
    filepath: str 
    """The path to the file. The file must be a text file of some sort (.txt, .gjf, .csv, .com, .sdf etc) but not binary."""
    split_chars: str
    """Splits the file at the first instance when the given 'split_character' str was found. Splits the file at all occuring intances."""
    savepath: str
    """Path to save the files. If the path does not exist, it will give an error. The default is: ./"""
    filetype: str
    """Type of the text file to write from and to (.txt, .gjf, .com etc)"""

class JobCreatorArgs(Tap):
    filepath: str 
    """The path to the file. The file must be a text file of some sort (.txt, .gjf, .csv, .com, .sdf etc) but not binary."""
    savepath: str
    """Path to save the files. If the path does not exist, it will give an error. The default is: ./"""
    filetype: str
    """Type of the text file to write from and to (.txt, .gjf, .com etc)"""
    id: str
    """The name of the out file."""

