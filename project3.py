import reportlab
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
    writer=PdfWriter(file)
    text = input("Text you want to add:\n ")
    writer.add_text(text)
def merger():
    file=input("Enter the file name: ")
    pass
    
if choice == 2:
    read()
elif choice==1:
    write()
elif choice==3:
    merger()
else:
    print("Invalid choice")