import webbrowser
import tkinter as tk

def open_website():
    url = 'https://genrandom.com/cats/' #Add the website url you want
    webbrowser.open_new_tab(url)
    
root = tk.Tk()
root.title("Open Random Cat Picker")

button_style = {
    "pady": 15,
    "padx": 40, 
    "font": ("Helvetica", "10"),
    "borderwidth": "0",
    "foreground": "white",
    "background": "#4CAF50",
}

button = tk.Button(root, text="Open", command=open_website) #Creates function to open website
button.pack(pady=20) #Adjust button padding

label = tk.Label(root, text="Open Random Cat.", font=("Helvetica", "10"))
label.pack(pady=(0, 10)) #Padding label and button

root.mainloop() #Tinker event loop
    