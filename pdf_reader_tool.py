from crewai_tools import tool
import PyPDF2


@tool
def read_pdf(path: str) -> str:
    """
    Read and extract text from a PDF file.

    Args:
        path (str): The file path to the PDF document.

    Returns:
        str: The extracted text from the PDF document. Each page's text is concatenated into a single string.
    
    Example:
        >>> text = read_pdf('example.pdf')
        >>> print(text)
    """
    with open(path, 'rb') as file:
        pdf = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf.pages)):
            text += pdf.pages[page_num].extract_text()
    return text