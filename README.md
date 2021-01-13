# python-pdf-merger

Merges all .pdf files in a specified directory.
A simple pdf merger I wrote in python to help compile various school notes and assignments and such.

When called it prompts the user first for the directory containing the PDFs to be merged. The user can either type out the path to the directory or input 'cwd' to specify the current working directory. The program will only accept 'cwd' or a valid path to a directory. The user will then be prompted to input the name of the merged pdf file. The program will tell you when the directory has been found, sort the found PDFs alphabetically, and merge the found PDFs into a new PDF if there is more
than 1 PDF in the specified directory.
