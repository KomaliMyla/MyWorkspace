import pyttsx3

book= open(r"C:\Users\mylak\Documents\book.txt")
book_text = book.readlines()
engine = pyttsx3.init()
for i in book_text:
    engine.say(i)
    engine.runAndWait()
