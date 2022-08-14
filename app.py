# Import following modules
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
import re
from flask import  Flask
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
import  time


app=Flask(__name__)

set_env(title="App")

global like


def liked():





            popup('Likes', ['Find More @ https://github.com/aswinks1995',  # equal to put_text('plain html: <br/>')

                put_buttons(['close'], onclick=lambda _: close_popup())
            ])

put_button("Like", onclick=lambda: liked())

app.run(debug=True)


