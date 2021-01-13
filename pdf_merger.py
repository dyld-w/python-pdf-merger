import os
import sys

from pikepdf import Pdf


def merger():
    # input path to folder in command line
    #  num_args = len(arguments)
    #  if num_args =
    #  directory = arguments[1]
    #  new_name = arguments[2]
    #  print(directory)
    # https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python

    valid_directory = False

    while not valid_directory:
        directory = input(
            "Path to directory with the PDFs to be merged or 'cwd' for your current working directory: "
        )

        if directory == "cwd":
            directory = os.getcwd()
            valid_directory = True
        elif os.path.isdir(directory):
            valid_directory = True
        else:
            print("Invalid input. Directory not found.")

    new_name = input("Name for the merged PDF: ")

    if directory[len(directory) - 1] != "/":
        directory += "/"

    print(directory)

    if os.path.isdir(directory):
        print("Directory found. Merging .pdf files")
        dir_list = os.listdir(directory)
        dir_list.sort()
        pdf = Pdf.new()
        version = pdf.pdf_version

        for file in dir_list:
            if file.endswith(".pdf"):
                print("appending", file)
                inp_PDF = Pdf.open(directory + file)
                version = max(version, inp_PDF.pdf_version)
                pdf.pages.extend(inp_PDF.pages)
        pdf.remove_unreferenced_resources()
        pdf.save(directory + new_name + ".pdf", min_version=version)
        print("Merged pdf should now be in " + directory)
    else:
        print("Directory not found")


if __name__ == "__main__":
    #  print(len(sys.argv))
    merger()
