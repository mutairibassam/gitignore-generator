import sys
import os
from enum import Enum
from lily.doc import Doc

class Languages(Enum):
    PYTHON = 1
    NODE = 2
    ANDROID = 3
    ANDROID_STUDIO = 4

def create_gitignore(lang):
    FILE_NAME = ".gitignore"
    obj = Doc()

    f_path = os.path.dirname(os.path.abspath(__file__))
    ignore_file = os.path.join(f_path, FILE_NAME)

    def add_value(val):
        f = open(ignore_file, 'a')
        f.write(val)
        f.close()

    try:
        for i in lang:
            if i == Languages.PYTHON.name:
                val = Doc.python(obj)
                add_value(val)

            if i == Languages.NODE.name:
                val = Doc.node(obj)
                add_value(val)

            if i == Languages.ANDROID.name:
                val = Doc.android(obj)
                add_value(val)

            if i == Languages.ANDROID_STUDIO.name:
                val = Doc.android_studio(obj)
                add_value(val)

    except:
        print("Invalid input, please try again.")

def main():

    global SELECTED_LANG
    SELECTED_LANG = []

    if len(sys.argv) > 1:
        for i in sys.argv[1:]:
            SELECTED_LANG.append(i.upper())
            
    create_gitignore(SELECTED_LANG)

    
if __name__ == "__main__":
   """ 
    main function 

   """ 
   main()
