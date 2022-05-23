from flask import Flask, request, render_template
import pickle
import numpy as np 

app = Flask(__name__, template_folder="templates")

model_file = open('model/stockingblitz.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    # return "success"
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    Tanggal=float(request.form['Tanggal'])
    
    Jumlah=float(request.form['Jumlah'])

    Bahan=float(request.form['Bahan'])

    Permintaan=float(request.form['Permintaan'])

    Prediksi=float(request.form['Prediksi'])

    X=np.array([[Prediksi,Tanggal,Jumlah,Bahan,Permintaan]])
    
    prediction = model.predict(X)

    output = round(prediction[0],0)
    if (output==0):
        Penjual="Mempertahankan Stock"
    elif (output==1):
        Penjual="Menambah Stock"

    return render_template('index.html',Penjual=Penjual, Tanggal=Tanggal, Jumlah=Jumlah, Bahan=Bahan, Permintaan=Permintaan)


if __name__ == '__main__':
    app.run(debug=True)