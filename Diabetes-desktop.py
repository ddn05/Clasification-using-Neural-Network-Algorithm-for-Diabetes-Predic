#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5.QtWidgets import *
from PyQt5 import uic
import pickle
import numpy as np
import sklearn

with open('NND_pickle', 'rb') as r:
    model = pickle.load(r)
    
def diabetes():
    banyakMelahirkan = float(window.input_melahirkan.text())
    kadarGlukosa     = float(window.input_glukosa.text())
    kadarDarah       = float(window.input_darah.text())
    ketebalanKulit   = float(window.input_kulit.text())
    kadarInsulin     = float(window.input_insulin.text())
    bmi              = float(window.input_bmi.text())
    derajatRiwayat   = float(window.input_riwayat.text())
    umur             = float(window.input_umur.text())
    
    dataPasien = np.array((banyakMelahirkan, kadarGlukosa, kadarDarah, ketebalanKulit, kadarInsulin, bmi, derajatRiwayat, umur))
    data = np.reshape(dataPasien,(1,-1))
                          
    isDiabetes = model.predict(data)
    
    if(isDiabetes == 1):
            window.simpulan.setText('POSITIF DIABETES')
    elif(isDiabetes == 0):
            window.simpulan.setText('NEGATIF DIABETES')

app = QApplication([])
window = QMainWindow()
uic.loadUi('DiabetesDekstop.ui',window)
window.setWindowTitle('Deteksi Diabetes')
window.show()
window.button_prediksi.clicked.connect(diabetes)
        
app.exec_()


# In[ ]:




