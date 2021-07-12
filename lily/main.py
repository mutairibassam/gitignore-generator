import sys
import os
from enum import Enum
from lily.doc import Doc

class Languages(Enum):
    PYTHON = 1


def create_gitignore(lang):

    obj = Doc()
    val = Doc.python(obj)

    f_path = os.path.dirname(os.path.abspath(__file__))
    ignore_file = os.path.join(f_path, '.gitignore')

    f = open(ignore_file, 'w')
    f.write(val)
    f.close()


def main():

    global SELECTED_LANG
    SELECTED_LANG = ""

    if len(sys.argv) > 1:
        print(sys.argv[1])
        if sys.argv[1].upper()[2:] == Languages.PYTHON.name:
            SELECTED_LANG = Languages.PYTHON.value
            create_gitignore(SELECTED_LANG)

    
if __name__ == "__main__":
   """ 
    main function 

   """ 
   main()
