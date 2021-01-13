import os
import sys

from pikepdf import Pdf


def merger():

    valid_directory = False

    while not valid_directory:
        directory = input("Path to directory with the PDFs to be merged "
                          "or 'cwd' for your current working directory: ")

        if directory == "cwd":
            directory = os.getcwd()
            valid_directory = True
        elif os.path.isdir(directory):
            valid_directory = True
        else:
            print("Invalid input. Directory not found.")

    print("Directory found:", directory)

    if directory[len(directory) - 1] != "/":
        directory += "/"

    dir_list = os.listdir(directory)
    pdf_list = []

    for file in dir_list:
        name, ext = os.path.splitext(file)

        if ext == '.pdf':
            pdf_list.append(file)

    pdf_list.sort()
    len_pdf_list = len(pdf_list)
    pdf = Pdf.new()
    version = pdf.pdf_version

    if len_pdf_list < 2:
        print("Only", len_pdf_list,
              ".pdf files in this directory. Not merging")
    else:
        new_name = input("Name for the merged PDF: ")
        print("Merging", len_pdf_list,
              "files into a file called " + new_name + ".pdf")

        for file in pdf_list:
            print("appending", file)
            inp_PDF = Pdf.open(directory + file)
            version = max(version, inp_PDF.pdf_version)
            pdf.pages.extend(inp_PDF.pages)
        pdf.remove_unreferenced_resources()
        pdf.save(directory + new_name + ".pdf", min_version=version)
        print("Merged pdf should now be in " + directory)


if __name__ == "__main__":
    merger()
