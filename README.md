# python-pdf-to-xml

pdf to xml: https://towardsdatascience.com/how-to-extract-data-from-pdf-forms-using-python-10b5e5f26f70

python libraries for pdf scraping: https://medium.com/analytics-vidhya/python-packages-for-pdf-data-extraction-d14ec30f0ad0

How to "convert pdf forms to xml"  and "extract fillable data"

1- Pdf forms are various, some forms are already in acroform type. Acroform pdfs have fillable text and easy to extract and convert to xml.  But old pdf types are not acroform and their fillable fields must be recognized.

2- In order to recognize and give label to fillable fields, a third party software "PDFElement by Wondershare"(https://pdf.wondershare.com/) can be used. The free version works fine.

3- In the screenrecording, an example is given how to convert an old formatted pdf to acroform pdf. (https://youtu.be/e52G4mqUluw)

4- Also, visual inspection and some manual changes are needed. Because forms have different layouts, some has images in them. The tool recognizes fillables fields and adds text labels to them, these labels are used in xml files. The auto generated text labels are not very good sometimes and some may be missing. Therefore visual inspection and manual changes are necessary.

