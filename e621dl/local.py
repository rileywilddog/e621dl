# Internal Imports
import datetime
import os

# Personal Imports
from e621dl import constants

# Vendor Imports
import yaml

def make_config():
    with open('config.yaml', 'wt', encoding = 'utf-8') as outfile:
        outfile.write(constants.DEFAULT_CONFIG_TEXT)
        print("[i] New default config file created. Please add tag groups to this file.'")
    raise SystemExit

def get_config():
    if not os.path.isfile('config.yaml'):
        print("[!] No config file found.")
        make_config()

    with open('config.yaml', 'rt', encoding = 'utf-8') as infile:
        config = yaml.load(infile)

    return config

def get_date(days_to_check):
    ordinal_check_date = datetime.date.today().toordinal() - (days_to_check - 1)

    if ordinal_check_date < 1:
        ordinal_check_date = 1
    elif ordinal_check_date > datetime.date.today().toordinal():
        ordinal_check_date = datetime.date.today().toordinal()

    return datetime.date.fromordinal(ordinal_check_date).strftime('%Y-%m-%d')

def substitute_illegals(char):
    illegals = ['\\', ':', '*', '?', '\"', '<', '>', '|', ' ']
    return '_' if char in illegals else char

def make_path(dir_name, filename, ext):
    clean_dir_name = ''.join([substitute_illegals(char) for char in dir_name]).lower()

    if not os.path.isdir(f"downloads/{clean_dir_name}"):
        os.makedirs(f"downloads/{clean_dir_name}")

    return f"downloads/{clean_dir_name}/{filename}.{ext}"
