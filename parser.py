import requests
from bs4 import BeautifulSoup
import textblob
import tkinter as tk

def printtitle():
    content.insert(tk.END, soup.find('h1').getText())
def printcontent():
    content.insert(tk.END, soup.find('body').getText())

window = tk.Tk()
window.resizable(True, True)
window.title('Window')

button = tk.Button(text = 'Print Title', command = printtitle)
button.pack()
button1 = tk.Button(text = 'Print Content', command = printcontent)
button1.pack()
content = tk.Text()
content.pack()
url = 'http://localhost/siteone/site.php'
site = requests.get(url)
soup = BeautifulSoup(site.text, 'html.parser')

window.mainloop()