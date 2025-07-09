import pdfkit

caminho_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # ajuste para o seu caminho
config = pdfkit.configuration(wkhtmltopdf=caminho_wkhtmltopdf)

# ------------------------------------------------------------------------------------------------------


# pdfkit.from_url('http://micropyramid.com', 'micron.pdf', configuration=config)

pdfkit.from_file("../templates/budget.html", 'teste.pdf',configuration=config)
print("PDF gerado como test.pdf")

