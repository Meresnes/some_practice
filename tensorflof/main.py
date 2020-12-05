# TensorFlow
import tensorflow as tf

from tensorflow import keras

# Вспомогательные библиотеки
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()


# Каждому изображению соответствует единственная метка.
# Так как названия классов не включены в датасет, сохраним их тут
# для дальнейшего использования при построении изображений:

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Данные должны быть предобработаны перед обучением нейросети.
# Если вы посмотрите на первое изображение в тренировочном сете вы увидите,
# что значения пикселей находятся в диапазоне от 0 до 255:
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

# Мы масштабируем эти значения к диапазону от 0 до 1 перед тем как скормить их нейросети.
# Для этого мы поделим значения на 255.
# Важно, чтобы тренировочный сет и проверочный сет были предобработаны одинаково:

train_images = train_images / 255.0

test_images = test_images / 255.0

# Чтобы убедиться, что данные в правильном формате и мы готовы построить и обучить нейросеть,
# выведем на экран первые 25 изображений из тренировочного сета и отобразим под ними наименования их классов.

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()