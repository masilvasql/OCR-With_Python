
import tensorflow
import numpy as np
import zipfile
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
from sklearn.preprocessing import label_binarize
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from tensorflow.keras.datasets import mnist


(train_data, train_labels) , (test_data, test_labels) = mnist.load_data()

digitos_data = np.vstack([train_data, test_data]) #concatena na vertical 'Matriz'
digitos_labels = np.hstack([train_labels, test_labels]) #concatena na vertical 'vetor'

indice = np.random.randint(0, digitos_data.shape[0])

plt.imshow(digitos_data[indice], cmap='gray')
plt.title('Classe ' + str(digitos_labels[indice]))
#plt.show()

sns.countplot(digitos_labels);
#plt.show()