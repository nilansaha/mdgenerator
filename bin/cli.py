import os
import argparse
from mdgenerator import generate_file_structure

parser = argparse.ArgumentParser(description = 'MD Generator')
parser.add_argument('target_dir', help = 'Generate tree of this directory')
args = parser.parse_args()

current_dir = os.getcwd()
generate_file_structure(args.target_dir, current_dir)
