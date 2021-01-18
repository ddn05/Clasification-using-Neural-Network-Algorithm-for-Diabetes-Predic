from flask import Flask, render_template, request, redirect
import pickle
import sklearn
import numpy as np                        # numpy==1.19.3
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':

        with open('NND_pickle', 'rb') as r:
            model = pickle.load(r)

        melahirkan = float(request.form['melahirkan'])
        glukosa = float(request.form['glukosa'])
        darah = float(request.form['darah'])
        kulit = float(request.form['kulit'])
        insulin = float(request.form['insulin'])
        bmi = float(request.form['bmi'])
        riwayat = float(request.form['riwayat'])
        umur = float(request.form['umur'])
        
        datas = np.array((melahirkan,glukosa,darah,kulit,insulin,bmi,riwayat,umur))
        train = MinMaxScaler().fit_transform(datas)
        hasil = np.reshape(datas, (1, -1))
        

        isDiabetes = model.predict(hasil)

        return render_template('hasil.html', finalData=isDiabetes)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
