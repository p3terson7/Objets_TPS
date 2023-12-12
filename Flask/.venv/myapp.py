# Run: python -m flask --app myapp run
from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

data=[
   {
      "Temperature":"21.1",
      "Humidity":"54.1",
   }
]

@app.route('/')
def __main__():
   return render_template('index.html', data=data)

if __name__ == '__main__':
   app.run(debug=True)