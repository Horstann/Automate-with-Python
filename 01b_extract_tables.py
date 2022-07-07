#import ghostscript
#import tkinter
import camelot

# extract PDFs
tables = camelot.read_pdf('foo.pdf', pages='1')

# export PDF to csv
tables.export('foo.csv', f='csv', compress=True)
tables[0].to_csv('foo.csv') # to csv
display(tables[0].df) # to df