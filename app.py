import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)
dir = os.path.dirname(os.path.realpath(__file__))
filename = ''
filename2 = ''
fasta1 = ''
fasta2 = ''
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/mostrar", methods=["POST"])
def mostrar(): 
    global filename
    global filename2
                   
    filename2 = filename
    try:
        if 'file' in request.files:
            imageFile = request.files['file']
            filename = secure_filename(imageFile.filename)
            imageFile.save(os.path.join(dir + '/static/input/', filename))


    except Exception as e:
        print(e)

    return jsonify(name = filename)


@app.route("/guardar_fasta1", methods=["POST"])
def guardar_fasta1(): 
    global fasta1
    try:
        if 'file' in request.files:
            imageFile = request.files['file']
            fasta1 = secure_filename(imageFile.filename)
            imageFile.save(os.path.join(dir + '/static/input/', fasta1))


    except Exception as e:
        print(e)

    return jsonify(name = fasta1)

@app.route("/guardar_fasta2", methods=["POST"])
def guardar_fasta2(): 
    global fasta2

    try:
        if 'file' in request.files:
            imageFile = request.files['file']
            fasta2 = secure_filename(imageFile.filename)
            imageFile.save(os.path.join(dir + '/static/input/', fasta2))


    except Exception as e:
        print(e)

    return jsonify(name = fasta2)




@app.route("/calcular", methods=["POST"])        
def calcular():
    global filename
    global fasta1
    global fasta2
    valor_1 = request.form['valor_1']
    valor_2 = request.form['valor_2']
    valor_3 = request.form['valor_3']
    valor_4 = request.form['valor_4']
    valor_5 = request.form['valor_5']

    #valor_r = request.form['valor_r']
    operador = request.form['operador']


    if operador=='global':    
        os.system('python3 algoritmos/global.py '+valor_1+' '+valor_2+' '+valor_3+' '+valor_4+' '+valor_5+' '+'static/input/'+filename)
    if operador=='global2':    
        os.system('python3 algoritmos/global2.py static/input/'+fasta1+' static/input/'+fasta2+' '+valor_1+' '+valor_2+' '+valor_3)
    elif operador=='local':
        os.system('python algoritmos/hist_Equalization.py static/images/'+filename)
    elif operador=='blast':
        os.system('python algoritmos/logaritmo.py static/images/'+filename +' '+ valor_1)
    elif operador=='muscle':    
        os.system('python algoritmos/raizC.py static/images/'+filename+' '+valor_1)
    elif operador=='jukes':    
        os.system('python algoritmos/contrast.py static/images/'+filename+' '+valor_1)
    elif operador=='kimura':    
        os.system('python algoritmos/contrast.py static/images/'+filename+' '+valor_1)
    elif operador=='upgma':    
        os.system('python algoritmos/contrast.py static/images/'+filename+' '+valor_1)
    else:    
        os.system('python3 algoritmos/neighbor.py static/images/'+filename+' '+valor_1+' '+valor_2)



    return jsonify(name = filename, metodo= operador)
    #practica 6
    '''
    elif operador=='adicion':    
        os.system('python algoritmos/adicion.py static/images/'+filename+' static/images/'+filename2)   
    elif operador=='adicion_gris':    
        os.system('python algoritmos/adicion_gris.py static/images/'+filename+' static/images/'+filename2)
    elif operador=='sustraccion_letra':    
        os.system('python algoritmos/sustraccion_letras.py static/images/'+filename+' static/images/'+filename2+' '+valor_1+' '+valor_2)  
    elif operador=='sustraccion_movimiento':    
        os.system('python algoritmos/sustraccion_movimiento.py static/images/'+filename+' static/images/'+filename2+' '+valor_1)   
    #practica 7   
    elif operador=='multiplicacionC':
        os.system('python algoritmos/multiplicacion.py static/images/'+filename+' static/images/'+valor_1)
    elif operador=='division_letra':    
        os.system('python algoritmos/division_letras.py static/images/'+filename+' static/images/'+filename2) 
    elif operador=='division':    
        os.system('python algoritmos/division.py static/images/'+filename+' static/images/'+filename2) 
    elif operador=='blending':    
        os.system('python algoritmos/blending.py static/images/'+filename+' static/images/'+filename2+' '+valor_1)     
    #practica 8   
    elif operador=='operador_and':    
        os.system('python algoritmos/operador_and.py static/images/'+filename+' static/images/'+filename2)
    elif operador=='operador_or':    
        os.system('python algoritmos/operador_or.py static/images/'+filename+' static/images/'+filename2) 
        '''                   


if __name__ == '__main__':
    app.run(debug = True, port=5000)