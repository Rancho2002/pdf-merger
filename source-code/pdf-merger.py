import os
import time
from pypdf import PdfWriter,PdfReader

merger=PdfWriter()

pdfs=[]
pages=[]

for i in os.listdir():
    if(i.endswith(".pdf")):
        pdfs.append(i)
        reader=PdfReader(i)
        page=len(reader.pages)
        pages.append(page)


pdfwithPage=[]
for i,j in enumerate(pdfs):
    pdfwithPage.append(j+f" ({pages[i]} pages) ")

pdfwithPage.sort()

print("\n\n******** PDFs are merged in sorted order, so make sure you rename your pdfs first ********\n")
print("\nAvailable pdfs in this folder: \n\n",pdfwithPage,sep="",end="\n\n")

pdfwithPage.sort()

for i,pdf in enumerate(sorted(pdfs)):

    try:
        print(f"\n********** {pdfwithPage[i]} **********\n")
        print(f"\nEnter start page no (0 for pg-1), end page no, pages to skip i.e 1 for no skip (SEPARATED WITH SPACE) or 'None' to select default:\n")
        print("Note: Here one argument and enter select that particular page\n")
        rng=tuple(map(int,input().split()))
    except:
        rng=None

    merger.merge(None,fileobj=pdf,pages=rng) #position is avoided here

name=int(time.time())
try:

    merger.write(f"{name}.pdf")
    merger.close()
    print("PDF merged successfully!!")
except:
    print("Failed to merge due to some error!")