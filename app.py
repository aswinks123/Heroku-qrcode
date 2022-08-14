#Created By Aswin KS
#This project uses Python,Pywebio,Flask and other modules to Generate QR codes.
#Feel free to clone the code.


#Importing Modules
import argparse
from pywebio.input import *
from pywebio.output import *
from flask import  Flask
from pywebio.session import *
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
import qrcode
from PIL import Image
import re
import time
from pywebio.session import run_js
from pywebio import start_server
#-----------------------------------------------------------------------------------------------------------------------

#Creating  a flask app

app=Flask(__name__)

#Main function that creates the QR code
def QR():
    c=0 #for like count


    set_env(title="QR-Code Generator") #For setting the window title bar text(tab text)

    put_html(r"""<h1  align="center"><strong>Color QR-Code Generator</strong></h1>""") #App Name in Main screen
    img = open('logo.png', 'rb').read()  #logo
    put_image(img, width='100px')#size of image


    x=input("Enter the URL or Text to Create QR-code",type="text",required=True)#Accepting url or data

    # Adding Progress bar
    put_processbar('bar')
    for i in range(1, 3):
        set_processbar('bar', i / 2)
        time.sleep(0.2)

    #getting foreground color
    foreground = select("Choose Foreground Color", options=['Black', 'Red', 'Blue', 'White','Yellow','Cyan','Magenta'], required=True)

    # Adding Progress bar
    put_processbar('bar')
    for i in range(1, 3):
        set_processbar('bar', i / 2)
        time.sleep(0.2)

    #getting background color
    background = select("Choose Background Color", options=['White', 'Red', 'Black', 'Blue','Yellow','Cyan','Magenta'], required=True)

    #Creating QR code using the provided data
    feature = qrcode.QRCode(version=1, box_size=40, border=3)
    feature.add_data(x)
    feature.make(fit=True)
    img = feature.make_image(fill_color=foreground, back_color=background)
    img.save("qr-image.jpg")

    #Adding Progress bar
    put_processbar('bar')
    for i in range(1, 8):
        set_processbar('bar', i /7)
        time.sleep(0.1)

    #outputing the text and image
    #put_text("Your QR Code is Created.")
    put_html(r"""<h3  align="center"><strong>Your QR Code is Created</strong></h3>""")
    img = open('qr-image.jpg', 'rb').read()
    put_image(img, width='150px')

    content = open('qr-image.jpg', 'rb').read()
    put_file('qr-image.jpg', content, 'Download QR code')


    #To show About sessiono
    def clicked():
        popup('About Us', [
            put_html('<h2>Created by Aswin Ks</h2>'),
            put_html('<h3>This Project is created using Python, Pywebio and Flask</h3>'),
            'Find More @ https://github.com/aswinks1995',  # equal to put_text('plain html: <br/>')
            put_buttons(['close'], onclick=lambda _: close_popup())
        ])

    global like
    like = 0

    #To register the like count(in beta stage)
    def liked():
        global like
        like += 1
        put_info("Thanks For your Feedback!")



    def btn_click(btn_val): #To do function of the 3 buttons

        if btn_val=='About':  #btn_val contain the text of button
            clicked()
        elif btn_val=='Generate new QR Code':
            run_js('window.location.reload()')
        elif btn_val=='Like':
            liked()


    put_buttons(['Generate new QR Code', 'About', 'Like'], onclick=btn_click)#Buttons


#To allow reloading of web browser and mentioning the port
app.add_url_rule('/qr','webio_view',webio_view(QR),methods=['GET','POST','OPTIONS'])
# app.run(port=44556 ,debug=True)
if __name__ =='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument("-p","--port",type=int,default=8080)
    args=parser.parse_args()

    start_server(QR,port=args.port,debug=True)
#calling our main function.Program start here
# QR()

