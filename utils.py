from fpdf import FPDF # type: ignore

def save_as_pdf(text, filename="story.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    for line in text.split('\n'):
        clean_line = line.encode("latin-1", "replace").decode("latin-1")
        pdf.multi_cell(0, 10, clean_line)
    pdf.output(filename)

def save_as_txt(text, filename="story.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
