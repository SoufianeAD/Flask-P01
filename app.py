from flask import Flask, render_template, request, session

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/cdp',  methods=['POST'])
def cdp():
    var1 = request.form['select1']
    #session['select1'] = 'test'
    if var1 == 'test1':
        print('inserted value : ' + var1)
        return render_template('input.html')
    else:
        print('inserted value : ' + var1)
        return render_template('input2.html')

@app.route('/parameters1',  methods=['POST'])
def parameters1():
    var1 = request.form['input1']
    var2 = request.form['input2']
    #print('checking session: ' + session['select1'])
    print('parameter 1: ' + var1)
    #session.pop('select1', None)
    #appel business
    result = {'produit 1': 10.09, 'produit 2': 66.23, 'produit 3': 456.20}
    return render_template("result.html",result = result)
