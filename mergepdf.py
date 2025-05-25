# Method 1
from glob import glob #list all the files in the curr directory
from pikepdf import Pdf

new_pdf = Pdf.new() #create new pdf

for i in glob("*.pdf"): # list all the files in the curr directory with the extension pdf
    # pehle open then extend means add
    old_pdf = Pdf.open(i) # Opens the current PDF file (`i`) for reading and stores it in the variable `old_pdf`.
    new_pdf.pages.extend(old_pdf.pages) # merges all the pages from evry  file to the new_pdf

new_pdf.save("Merged Pdf.pdf") 




# Method 2
import os
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_filename):
    merger = PdfMerger() #creates obj
    
    for pdf in pdf_list:
        if os.path.exists(pdf): #check if the file exists
            merger.append(pdf) #appending the pdf to another
        else:
            print(f"File not found: {pdf}") #throwing an error if it doesn't exists
    
    merger.write(output_filename) #writing the content in the merged file i.e. saving it
    merger.close()
    print(f"Merged PDF saved as '{output_filename}'.")


pdf_files = ['Content Writing Internship.pdf', 'Digital Marketing Internship.pdf']  # Files to be merged
output_file = 'merged_output.pdf' # name of the merged file

merge_pdfs(pdf_files, output_file) # method call to merge pdfs
