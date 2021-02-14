import pyttsx3
import PyPDF2

book = open('oop.pdf', 'rb')
reader = PyPDF2.PdfFileReader(book)
pages = reader.numPages
print(pages)
speaker = pyttsx3.init()
for i in range(7, pages):
    page = reader.getPage(i)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

