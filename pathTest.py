import os
import Tkinter
import tkFileDialog

def main():

    Tkinter.Tk().withdraw() # Close the root window
    in_path = tkFileDialog.askopenfilename()
    print in_path


    dirPathList = in_path.split('/')
    print dirPathList

    print os.path.dirname(in_path)

if __name__ == "__main__":
    main()