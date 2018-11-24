import PyPDF2.pdf as pd
pdf = pd.PdfFileReader(open('(2001-2018) Domestic-Fuel-Cost-Archives.pdf', "rb"))
f = open("(2001-2018) Domestic-Fuel-Cost-Archives.pdf.csv","w+")
for page in pdf.pages:
    f.write(page.extractText())
f.close()
