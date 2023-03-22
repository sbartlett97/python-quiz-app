import os

def clear() -> None:
    """
    clears the terminal screen
    """
    os.system('cls' if os.name=='nt' else 'clear')
