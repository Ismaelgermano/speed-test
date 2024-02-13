# Importando pillow
from PIL import Image, ImageTk
# Importanto tkinter
from tkinter import *
#importando speedtest
import speedtest

# Design colors:
co0 = "#f0f3f5"  # gray
co1 = "#feffff"  # white
co2 = "#3fb5a3"  # green
co3 = "#fc766d"  # red
co4 = "#403d3d"  # black
co5 = "#4a88e8"  # blue

# Project window:
window = Tk()
window.title('INTERNET SPEED TEST GERMANO')
window.geometry('350x200')
window.configure(background=co1)
window.resizable(width=False, height=False)

# Splitting the window into two frames:
frame_logo = Frame(window, width=350, height=60, bg=co1)
frame_logo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_body = Frame(window, width=350, height=140, bg=co1)
frame_body.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Setting up the frame logo:
image = Image.open('img\\speed.png') # -> criando imagem pillow
image = image.resize((55,55))
image = ImageTk.PhotoImage(image) # -> convertendo imagem pillow para Tkinter (para aparecer na janela tkinter)

label_logo_image = Label(frame_logo, height=60, image=image, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), bg=co1, fg=co3)
label_logo_image.place(x=20, y=0)

label_logo_name = Label(frame_logo, text= 'Internet Speed Test', padx=10, anchor=NE, font=('arial 16 bold'), bg=co1, fg=co4)
label_logo_name.place(x=100, y=16)

label_logo_line = Label(frame_logo, width=350,anchor=NE, font=('Arial 1'), bg=co2)
label_logo_line.place(x=0, y=59)

# Setting up the frame body:
def main():
    speed = speedtest.Speedtest()
    download = f"{'{:.2f}'.format(speed.download() / 1024 / 1024)}"
    upload = f"{'{:.2f}'.format(speed.upload() / 1024 / 1024)}"

    label_download['text'] = download
    label_upload['text'] = upload

    btn_test['text'] = ' Testar novamente'
    btn_test.place(x=90, y=85)

label_download = Label(frame_body,text= '', anchor=NW, font=('Arial 28'), bg=co1, fg=co4)
label_download.place(x=20, y=10)

label_download_t = Label(frame_body,text= 'Download Mbps', anchor=NW, font=('Arial 10'), bg=co1, fg=co4)
label_download_t.place(x=30, y=50)

image_down_up = Image.open('img\\up_down_colored.png') # -> criando imagem pillow
image_down_up = image_down_up.resize((55,55))
image_down_up = ImageTk.PhotoImage(image_down_up) # -> convertendo imagem pillow para Tkinter (para aparecer na janela tkinter)
label_logo_image = Label(frame_body, height=60, image=image_down_up, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), bg=co1, fg=co3)
label_logo_image.place(x=145, y=10)

label_upload = Label(frame_body,text= '', anchor=NW, font=('Arial 28'), bg=co1, fg=co4)
label_upload.place(x=210, y=10)

label_upload_t = Label(frame_body,text= 'Upload Mbps', anchor=NW, font=('Arial 10'), bg=co1, fg=co4)
label_upload_t.place(x=230, y=50)

# Botão teste:
btn_test = Button(frame_body, command=main, text= ' Iniciar teste', anchor=NW, font=('Arial 14'),relief=RAISED, overrelief=RIDGE, bg=co2, fg=co1)
btn_test.place(x=115, y=85)

window.mainloop()