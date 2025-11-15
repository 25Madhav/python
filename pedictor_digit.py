import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
# We still need a minimal use of numpy internally for argmax in visualization

# 1. Load and prepare data (simplest way)
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize pixel values from 0-255 to 0-1
x_train, x_test = x_train / 255.0, x_test / 255.0

# 2. Build a simple fully-connected model (MLP)
model = models.Sequential([
    # Input layer: Flattens the 28x28 image into a single row of 784 pixels
    layers.Flatten(input_shape=(28, 28)),
    # Hidden layer with 128 neurons
    layers.Dense(128, activation='relu'),
    # Output layer with 10 neurons (one for each digit 0-9)
    layers.Dense(10, activation='softmax')
])

# 3. Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy', # Handles integer labels easily
              metrics=['accuracy'])

# 4. Train the model
print("Training the model...")
model.fit(x_train, y_train, epochs=3, validation_split=0.1) # Train for fewer epochs

# 5. Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
print(f"\nTest accuracy: {test_acc*100:.2f}%")

# 6. Make and display a single prediction
predictions = model.predict(x_test[:1]) # Predict just the first image

# The 'argmax' function finds the index (digit) with the highest probability
predicted_label = tf.argmax(predictions[0]).numpy()
actual_label = y_test[0]

plt.imshow(x_test[0], cmap='gray')
plt.title(f"Actual: {actual_label}, Predicted: {predicted_label}")
plt.axis('off')
plt.show()