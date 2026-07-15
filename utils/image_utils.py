import numpy as np

from tensorflow.keras.preprocessing import image


IMAGE_SIZE = (224,224)


def preprocess_image(image_path):

    img = image.load_img(
        image_path,
        target_size=IMAGE_SIZE
    )

    img = image.img_to_array(img)

    img = img / 255

    img = np.expand_dims(img, axis=0)

    return img