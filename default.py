from .. import app
from flask import render_template


hobbies = [
    "Програмування",
    "Читання (інколи)",
    "Велоспорт",
    "електроніка",
    "математика",
    "Риболовля",
]


@app.route('/')
def display_hobbies():
    return render_template('_helpers.html', hobbies=hobbies)


