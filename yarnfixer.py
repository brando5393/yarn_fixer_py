#!/usr/bin/env python3
import re
import os
import platform

# check host OS
OPERATING_SYSTEM = platform.system()
# create regex var
yarn_regex = re.compile(r"yarn | Yarn+")
# based on OS provide correctly formatted default filepath
if OPERATING_SYSTEM == "Windows":
    default_path = os.getcwd()+"\package.json"
else:
    default_path = os.getcwd()+"/package.json"
# create start func


def start():
    print("""

                    __     __                ______ _               
                    \ \   / /               |  ____(_)              
                     \ \_/ /_ _ _ __ _ __   | |__   ___  _____ _ __ 
                      \   / _` | '__| '_ \  |  __| | \ \/ / _ \ '__|
                       | | (_| | |  | | | | | |    | |>  <  __/ |   
                       |_|\__,_|_|  |_| |_| |_|    |_/_/\_\___|_|   
                                                                    
    """)
    print("Please enter the full path to the package.json file that you would like to \nconvert, if no path is given Yarn Fixer will look in the current directory.")
    file_path = input("Enter File Path: ")
    if file_path == "" or None:
        find_yarn()
    else:
        find_yarn(file_path)
# create find_yarn func


def find_yarn(filename=default_path):
    print(f"Searching for package.json")
    yarn_regex = re.compile(r"yarn | Yarn+")
    try:
        file = open(filename)
        file_text = file.read()
        match_obj = yarn_regex.findall(file_text)
        if match_obj == []:
            print(
                "No instances of yarn are being used in your package.json, happy coding!")
        else:
            print(
                f"Yarn Fixer found {len(match_obj)} matches, attempting to fix now...")
            file.close()
            fix_yarn(filename, file_text, yarn_regex)
    except FileNotFoundError:
        print(
            f"Sorry, but a package.json file could not be found at this location:\n{filename}\nPlease verify the correct path and try again.")
    finally:
        print("Thank you for using Yarn Fixer.")

# create fix_yarn func


def fix_yarn(filename, file_text, regex):
    try:
        file = open(filename, "w")
        new_text = regex.sub("npm ", file_text)
        file.write(new_text)
        file.close()
        print(f"Fixed package.json located at {filename}")
    except:
        print("Fatal error in fix_yarn, exiting")


# call start func
start()
