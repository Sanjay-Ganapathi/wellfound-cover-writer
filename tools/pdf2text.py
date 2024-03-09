from crewai_tools import tool
from PyPDF2 import PdfReader


class PDFToTextTool:
    @tool("PDF to Text tool")
    def pdf2text(path: str):
        """ Useful to extract all the contents from the given pdf. Parameter : path of the pdf file """
        reader = PdfReader(path)

        final = []
        for i in range(len(reader.pages)):
            page = reader.pages[i]

            text = page.extract_text()

            final.append(text)

        return "\n".join(final)


# t = PDFToTextTool()
# res = t.pdf2text.run(r"C:\Users\ganas\Desktop\sanjay_ganapathi_new.pdf")
# print(res)
