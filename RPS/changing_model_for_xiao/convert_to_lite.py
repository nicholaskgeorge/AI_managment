import tensorflow as tf
from tensorflow.keras.models import load_model

model_name = "rps2"

# Load the pruned Keras model
model = load_model(f'RPS/pretrained_models/{model_name}.h5')  # Replace with your model path

# Convert the model to TensorFlow Lite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]  # Apply quantization

# Convert the model
tflite_model = converter.convert()

# Save the converted model as a .tflite file
with open(f'RPS/pretrained_models/{model_name}.tflite', 'wb') as f:
    f.write(tflite_model)

print(f"Model converted and saved as '{model_name}.tflite'")

