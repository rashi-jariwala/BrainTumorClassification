import tensorflow
import cv2
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import (
    Conv2D,
    AveragePooling2D,
    Flatten,
    Dense
)

# ============================================
# Image Size
# ============================================

image_size = (224,224)

# ============================================
# Data Preprocessing
# ============================================

data_generator = ImageDataGenerator(
    rescale=1/255,
    validation_split=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.1
)

# ============================================
# Train Generator
# ============================================

train_generator = data_generator.flow_from_directory(
    "dataset/Training",
    target_size=image_size,
    batch_size=32,
    class_mode="categorical",
    subset="training"
)

# ============================================
# Validation Generator
# ============================================

validation_generator = data_generator.flow_from_directory(
    "dataset/Training",
    target_size=image_size,
    batch_size=32,
    class_mode="categorical",
    subset="validation"
)

print("="*50)
print("Class Indices")
print(train_generator.class_indices)
print("="*50)

print("Training Images :", train_generator.samples)
print("Validation Images :", validation_generator.samples)

# ============================================
# CNN Model
# ============================================

model = Sequential()

# ============================================
# First Convolution Layer
# ============================================

model.add(
    Conv2D(
        filters=32,
        kernel_size=(3,3),
        strides=(1,1),
        activation="relu",
        input_shape=image_size+(3,)
    )
)

model.add(
    AveragePooling2D(
        pool_size=(2,2)
    )
)

# ============================================
# Second Convolution Layer
# ============================================

model.add(
    Conv2D(
        filters=16,
        kernel_size=(3,3),
        strides=(1,1),
        activation="relu"
    )
)

model.add(
    AveragePooling2D(
        pool_size=(2,2)
    )
)

# ============================================
# Third Convolution Layer
# ============================================

model.add(
    Conv2D(
        filters=8,
        kernel_size=(3,3),
        strides=(1,1),
        activation="relu"
    )
)

model.add(
    AveragePooling2D(
        pool_size=(2,2)
    )
)

# ============================================
# Flatten Layer
# ============================================

model.add(Flatten())

# ============================================
# Hidden Layer
# ============================================

model.add(
    Dense(
        units=64,
        activation="relu"
    )
)

model.add(
    Dense(
        units=32,
        activation="relu"
    )
)

# ============================================
# Output Layer
# ============================================

model.add(
    Dense(
        units=4,
        activation="softmax"
    )
)

# ============================================
# Model Summary
# ============================================

model.summary()
# ============================================
# Compile Model
# ============================================

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

print("=" * 60)
print("Model Compiled Successfully")
print("=" * 60)

# ============================================
# Train Model
# ============================================

history = model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=3,
    # epochs=20,
    verbose=1
)

# ============================================
# Evaluate Model
# ============================================

print("\n")
print("=" * 60)
print("Model Evaluation")
print("=" * 60)

train_loss, train_accuracy = model.evaluate(
    train_generator,
    verbose=1
)

validation_loss, validation_accuracy = model.evaluate(
    validation_generator,
    verbose=1
)

print("\n")
print("Training Accuracy :", train_accuracy)
print("Training Loss     :", train_loss)

print("\n")

print("Validation Accuracy :", validation_accuracy)
print("Validation Loss     :", validation_loss)

print("=" * 60)

# ============================================
# Accuracy Graph
# ============================================

plt.figure(figsize=(8,5))

plt.plot(
    history.history["accuracy"],
    label="Training Accuracy",
    linewidth=2
)

plt.plot(
    history.history["val_accuracy"],
    label="Validation Accuracy",
    linewidth=2
)

plt.title("Brain Tumor Classification Accuracy")

plt.xlabel("Epoch")

plt.ylabel("Accuracy")

plt.legend()

plt.grid(True)

plt.show()

# ============================================
# Loss Graph
# ============================================

plt.figure(figsize=(8,5))

plt.plot(
    history.history["loss"],
    label="Training Loss",
    linewidth=2
)

plt.plot(
    history.history["val_loss"],
    label="Validation Loss",
    linewidth=2
)

plt.title("Brain Tumor Classification Loss")

plt.xlabel("Epoch")

plt.ylabel("Loss")

plt.legend()

plt.grid(True)

plt.show()

print("\n")
print("=" * 60)
print("Training Completed Successfully")
print("=" * 60)

# ============================================
# Save Model
# ============================================

import os

os.makedirs("models", exist_ok=True)

model.save("models/brain_tumor.keras")

print("\n")
print("=" * 60)
print("Model Saved Successfully")
print("Location : models/brain_tumor.keras")
print("=" * 60)

# ============================================
# Class Labels
# ============================================

class_names = {
    0: "glioma",
    1: "meningioma",
    2: "notumor",
    3: "pituitary"
}

# ============================================
# Predict Single Image Function
# ============================================

def predict_image(image_path):

    img = image.load_img(
        image_path,
        target_size=(224,224)
    )

    plt.figure(figsize=(5,5))
    plt.imshow(img)
    plt.axis("off")
    plt.show()

    img_array = image.img_to_array(img)

    img_array = img_array / 255.0

    img_array = tensorflow.expand_dims(
        img_array,
        axis=0
    )

    prediction = model.predict(img_array)

    predicted_class = tensorflow.argmax(
        prediction,
        axis=1
    ).numpy()[0]

    confidence = prediction[0][predicted_class] * 100

    print("\n")
    print("=" * 60)
    print("Prediction Result")
    print("=" * 60)
    print("Predicted Class :", class_names[predicted_class])
    print("Confidence      : {:.2f}%".format(confidence))
    print("=" * 60)

# ============================================
# Example Prediction
# ============================================

test_image = "dataset/Testing/glioma/sample.jpg"

if os.path.exists(test_image):

    predict_image(test_image)

else:

    print("\n")
    print("=" * 60)
    print("Prediction Skipped")
    print("Sample image not found.")
    print("Update the path below to test your own image:")
    print(test_image)
    print("=" * 60)

# ============================================
# Training Completed
# ============================================

print("\n")
print("=" * 60)
print("Brain Tumor CNN Training Completed Successfully")
print("=" * 60)

print("Model File : models/brain_tumor.keras")

print("Now you can load the model using:")

print("""
from tensorflow.keras.models import load_model

model = load_model("models/brain_tumor.keras")
""")