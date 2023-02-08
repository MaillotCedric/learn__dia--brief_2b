def new_model(model, include_top, input_shape, weights="imagenet"):
    return model(
        weights = weights,
        include_top = include_top,
        input_shape = input_shape
    )

def freeze(model, right_hand_limit=0):
    """
    Args:
        right_hand_limit (int, optional): Nombre de couches à ré-entrainer. Defaults to 0.
    """
    limit = -1 * right_hand_limit
    layers = model.layers if limit == 0 else model.layers[:limit]

    for layer in layers: # parcours des différentes couches du modèle
        layer.trainable = False # gel de la couche

from keras.models import Sequential
from keras.layers import Dense
def new_cnn(cnn_model, nb_of_labels=2, new_layers=[]):
    """
    Args:
        new_layers (List, optional): Nouvelles couches de convolution à ajouter (excepté la dernière). Defaults to [].
    """
    last_activation = "sigmoid" if nb_of_labels == 2 else "softmax"
    last_layer = Dense(nb_of_labels, activation=last_activation)
    new_layers.append(last_layer)
    sequence = new_layers.copy()

    sequence.insert(0, cnn_model)

    return Sequential(sequence)

import tensorflow as tf
def get_datasets(folders_path, batch_size=4, validation_split=0.2, seed=1):
    train_dataset = tf.keras.utils.image_dataset_from_directory(
        folders_path,
        color_mode = "rgb",
        batch_size = batch_size,
        image_size = (224, 224),
        shuffle = True,
        validation_split = validation_split,
        subset = "training",
        seed = seed
    )
    validation_dataset = tf.keras.utils.image_dataset_from_directory(
        folders_path,
        color_mode = "rgb",
        batch_size = batch_size,
        image_size = (224, 224),
        shuffle = False,
        validation_split = validation_split,
        subset = "validation",
        seed = seed
    )

    return train_dataset, validation_dataset

from keras.optimizers import Adam
def compile_model(model, loss, metrics, learning_rate, optimizer=Adam):
    model.compile(
        loss = loss,
        optimizer = optimizer(learning_rate=learning_rate),
        metrics = metrics
    )

def train_model(model, train_data, validation_data, nb_of_epochs, callbacks=[]):
    """ 
        Entraine le modèle.
        Retourne l'historique des différentes métriques, enregistrées lors de la phase d'entrainement.
    """
    metrics_history = model.fit(
        train_data,
        epochs = nb_of_epochs,
        validation_data = validation_data,
        callbacks = callbacks
    )

    return metrics_history

from matplotlib import pyplot as plt
def graph(metric, training_metrics):
    plt.plot(training_metrics.history[metric])
    plt.plot(training_metrics.history[f"val_{metric}"])

    plt.title(f"model {metric}")

    plt.ylabel(metric)
    plt.xlabel("epoch")

    plt.legend(["train", "validation"], loc="upper left")

    return plt

def save_model():
    pass
