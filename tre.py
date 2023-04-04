from flask import Flask, request, render_template
import math
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('tre_3.html')

@app.route('/AreaRettangolo')
def areaRettangolo():
    base = int(request.args.get('base'))
    altezza = int(request.args.get('altezza'))
    area = base * altezza
    Errore0 = msg= 'Errore'
    if base == 0 or altezza == 0: 
        return(Errore0)
    else:
        return render_template('risultato_uno_1.html', base = base, altezza = altezza, area = area)

@app.route('/AreaRettangolo/Diagonale')
def AreaRettangolo_Diagonale():
  if scelta == 'Area': 
    area = base * altezza
    return('area.html', area)
  else: 
    diagonale = math.sqrt(base ** 2 + altezza ** 2)
  return render_template('tre_3.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)