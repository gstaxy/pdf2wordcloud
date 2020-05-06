from tika import parser
import slate3k as slate
import PyPDF2

def tika_parser(pdf_path):
    '''
    Extract words from pdf document using tika
    :param pdf_path: Path to pdf location in the project
    :return: String with content of the pdf
    '''
    # Use tika parser directly
    raw_text = parser.from_file(pdf_path)
    text_content = raw_text['content']

    return text_content

def slate_parser(pdf_path):
    '''
    Extract words from pdf document using slate3k
    :param pdf_path: Path to pdf location in the project
    :return: String with content of the pdf
    '''
    # Open the file to be able to read the content
    with open(pdf_path,'rb') as f:
        text_content = slate.PDF(f)

    return str(text_content[0])

def pypdf2_parser(pdf_path):
    '''
    Extract words from pdf document using pypdf2
    :param pdf_path: Path to pdf location in the project
    :return: String with content of the pdf
    '''

    # Open the file to be able to read the content
    pdfFileObj = open(pdf_path, 'rb')

    # Readable object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Deal with encrypted pdf
    if pdfReader.isEncrypted:
        pdfReader.decrypt('')

    # Get number of pages in pdf file
    num_pages = pdfReader.numPages
    print(num_pages)

    # Predefine variables in the loop
    count_page = 0
    text_content = ""

    # While loop until total number of page is reached
    while count_page < num_pages:
        pageObj = pdfReader.getPage(count_page)
        text_content += pageObj.extractText()
        count_page += 1

    return text_content
