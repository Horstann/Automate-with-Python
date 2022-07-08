#import ghostscript
#import tkinter
import camelot

# extract PDFs
tables = camelot.read_pdf('01b_foo.pdf', pages='1')

# export PDF to csv
tables.export('01b_foo1.csv', f='csv', compress=True) # to csv in zip
tables[0].to_csv('01b_foo2.csv') # to csv
print(tables[0].df) # to df