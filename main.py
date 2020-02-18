from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('sakums.html')
  
@app.route('/viens')
def viens():
  return render_template('viens.html')

@app.route('/divi')
def divi():
  return render_template('divi.html')

@app.route('/tris')
def tris():
  return render_template('tris.html')

@app.route('/sakums')
def sakums():
  return render_template('sakums.html')

app.run(host='0.0.0.0',port=8020)