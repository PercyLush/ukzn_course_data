import PyPDF2

path = "C:/Users/Bheki Lushaba/Downloads/college-of-law-and-management-studies-handbook-2020.pdf"

def extract(start_page, end_page):
    with open(path, "rb") as file1:
        data = PyPDF2.PdfReader(file1)
        Text = ""

        for page in range(start_page - 1, end_page):
            pages = data.pages[page]
            text_data = pages.extract_text()
            Text += text_data

    with open("Descriptions(Law).txt", "w", encoding="utf-8") as file:
        file.write(Text)


start = 134
end = 267

extract(start, end)