import sys
import os
import re
import subprocess
import platform
from document_parser import DocumentParser
from docx import Document
from  docx.opc.exceptions import PackageNotFoundError
import joblib
from os.path import dirname, join
from android.os import Environment


class ParserThread():
    print('Starteddddd')
    def __init__(self):
        super(ParserThread, self).__init__()
        self.doc_path = join(dirname(__file__), "1.docx")
        self.document = Document(self.doc_path)
        self.HASHES = join(dirname(__file__), "hashes.pickle")

    def run(self):
        CHARS_PER_LINE = 54
        LINES_PER_PAGE = 30
        with open(self.HASHES, 'rb') as f:
            hashes = joblib.load(f)
        document_parser = DocumentParser(hashes, CHARS_PER_LINE, LINES_PER_PAGE)
        pdf_path = re.sub('docx', 'pdf', self.doc_path)
        d = str(Environment.getExternalStorageDirectory())

        dirs = os.listdir(d)
        for file in dirs:
             print (file)



        try:
            document_parser.parse_document(self.document, join("/storage/emulated/0/Download/", "1.pdf"))

        except KeyError as e:
            self.key_exception.emit(str(e)[1])

    print('Fin')

def main():
    thread = ParserThread()
    thread.run()










