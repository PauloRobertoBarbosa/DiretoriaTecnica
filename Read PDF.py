from tabula import read_pdf
import os
os.chdir(r'C:/Users/paulo.roberto/Documents')

file = "A320.pdf"
tables = read_pdf(file)