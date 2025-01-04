# from reportlab.pdfgen import canvas
from pypdf import PdfReader , PdfWriter
choice=int(input("MERGE(0), WRITE(1) OR EXRACT(2): "))

writer = PdfWriter()
# reader = PdfReader()
def read():
    file=input("Enter the file name: ")
    i = int(input("Page you want to extract: "))
    reader = PdfReader(file)
    for index,page in enumerate(reader.pages,start=1):
        i=i-1
        no=reader.pages[i]
        print(no.extract_text())
        break
def write():
    file=input("Enter the file name: ")
    # writer=PdfWriter(file)
    pass

def merger():
    file=input("Enter the file name: ")
    writer = PdfWriter(file)
    file1=input("File you want to merge: ")
    reader=PdfReader(file1)
    output_file="merged.pdf"
    for page in reader.pages:
        writer.add_page(page)
    with open(output_file,"wb") as output_pdf:
        writer.write(output_pdf)
    print(f"Merged file saved as {output_file}")
    
if choice == 2:
    read()
elif choice==1:
    write()
elif choice==0:
    merger()
else:
    print("Invalid choice")