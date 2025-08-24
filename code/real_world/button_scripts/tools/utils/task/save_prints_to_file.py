import sys

def save_prints_to_file(filepath):
    sys.stdout = open(filepath, 'w')