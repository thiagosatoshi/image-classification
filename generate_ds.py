import os
import tensorflow as tf

image_size = (180, 180)
batch_size = 128


def generate_dataset():
    """
    """
    folder_path = os.path.join("data", "PetImages")

    train_ds, val_ds = tf.keras.utils.image_dataset_from_directory(
        folder_path,
        validation_split=0.2,
        subset="both",
        seed=1337,
        image_size=image_size,
        batch_size=batch_size,
    )
    return train_ds, val_ds
