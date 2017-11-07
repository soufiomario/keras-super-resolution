import os
import numpy as np
from argparse import ArgumentParser
from keras.models import model_from_json
from PIL import Image


def load_image(name, size):
    """
    画像を読み込み配列に格納する
    # 引数
        name : String, 保存場所
        size : List, 画像サイズ
    # 戻り値
        image : Numpy array, 画像データ
    """
    image = Image.open(name)
    image = image.resize((size[0]//2, size[1]//2))
    image = image.resize(size, Image.BICUBIC)
    image.show()
    image = np.array(image)
    image = image / 255
    # モデルの入力次元にあわせる
    image = np.array([image])
    return image


def load_model(name):
    """
    任意のJSONファイルを参照し、モデルに変換する
    # 引数
        name : String, 保存先ファイル名
    # 戻り値
        Keras model
    """
    with open(name) as f:
        json = f.read()
    model = model_from_json(json)
    return model


def show(image):
    """
    画像データを生成
    # 引数
        image : Numpy array
    """
    image = image[0] * 255
    image = image.astype(np.uint8)
    image = Image.fromarray(image)
    image.show()


def main():
    model = load_model('model-b.json')
    model.load_weights('weights-b.hdf5')
    print('Enter the file name (*.jpg)')
    while True:
        values = input('>> ').rstrip()
        if os.path.isfile(values) == False:
            print('File not exist')
            continue
        image = load_image(name=values, size=(128, 128))
        prediction = model.predict(image)
        show(prediction)


if __name__ == '__main__':
    main()