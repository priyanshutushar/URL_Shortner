import pyshorteners
import pyperclip
from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("URL Shortner")

url = StringVar()
url_address = StringVar()

def url_shortner():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)
    
def copy_url():
    url_short = url_address.get()
    pyperclip.copy(url_short)
    

Label(root,text="URL Shortner Tool").pack(pady=10)
Entry(root,textvariable=url).pack(pady=10)
Button(root,text="Generate Short URL",command=url_shortner).pack(pady=7)
Entry(root,textvariable=url_address).pack(pady=10)
Button(root,text="Copy URL",command=copy_url).pack(pady=5)

root.mainloop()
