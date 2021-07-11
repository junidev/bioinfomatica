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
        os.system('python3 algoritmos/global.py '+valor_1+' '+valor_2+' '+valor_3+' '+valor_4+' '+valor_5+' '+'static/input/'+filename+' >> /home/junior/UNSA/noveno/bio/examen/static/output/global.txt')
    if operador=='global2':    
        os.system('python3 algoritmos/global2.py static/input/'+fasta1+' static/input/'+fasta2+' '+valor_1+' '+valor_2+' '+valor_3+' >> /home/junior/UNSA/noveno/bio/examen/static/output/global2.txt')
    elif operador=='local':
        os.system('python3 algoritmos/local.py '+valor_1+' '+valor_2+' '+valor_3+' '+valor_4+' '+valor_5+' >> /home/junior/UNSA/noveno/bio/examen/static/output/local.txt')
    elif operador=='blast':
        os.system("./blast 'Dataset' static/input/"+filename+" > /home/junior/UNSA/noveno/bio/examen/static/output/blast.txt")
    elif operador=='muscle':    
        #os.system('python algoritmos/raizC.py static/images/'+filename+' '+valor_1)
        os.system('muscle -in /home/junior/UNSA/noveno/bio/examen/static/input/'+fasta1+' -out /home/junior/UNSA/noveno/bio/examen/static/output/muscle.txt')
    elif operador=='jukes':    
        os.system('python3 algoritmos/jukes.py '+valor_1+' '+valor_2+' >> /home/junior/UNSA/noveno/bio/examen/static/output/jukes.txt')
    elif operador=='kimura':    
        os.system('python3 algoritmos/kimura.py static/input/'+fasta1+' static/input/'+fasta2+' >> /home/junior/UNSA/noveno/bio/examen/static/output/kimura.txt')
    elif operador=='upgma':    
        os.system('python3 algoritmos/upgma.py static/input/'+filename+' '+valor_1+' >> /home/junior/UNSA/noveno/bio/examen/static/output/upgma.txt')
    elif operador=='neighbor':    
        os.system('python2 algoritmos/neighbor.py static/input/'+filename+' >> /home/junior/UNSA/noveno/bio/examen/static/output/neighbor.txt')
    else:    
        os.system('python2 algoritmos/neighbor.py static/input/'+filename+' >> /home/junior/UNSA/noveno/bio/examen/static/output/muscle.txt')



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