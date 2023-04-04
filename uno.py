from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('uno_1.html')

@app.route('/AreaRettangolo')
def areaRettangolo():
    base = int(request.args.get('base'))
    altezza = int(request.args.get('altezza'))
    area = base * altezza
    return render_template('risultato_uno_1.html', base = base, altezza = altezza, area = area)
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)