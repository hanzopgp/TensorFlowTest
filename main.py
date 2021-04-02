import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np


def get_dataset():

    # Numbers of row per class
    row_per_class = 100

    # Generate rows
    sick = np.random.randn(row_per_class, 2) + np.array([-2, -2])
    sick_2 = np.random.randn(row_per_class, 2) + np.array([2, 2])

    healthy = np.random.randn(row_per_class, 2) + np.array([-2, 2])
    healthy_2 = np.random.randn(row_per_class, 2) + np.array([2, -2])

    features = np.vstack([sick, sick_2, healthy, healthy_2])
    targets = np.concatenate((np.zeros(row_per_class * 2), np.zeros(row_per_class * 2) + 1))

    targets = targets.reshape(-1, 1)

    return features, targets


if __name__ == '__main__':
    features, targets = get_dataset()

    plt.scatter(features[:, 0], features[:, 1], s=40, c=targets, cmap=plt.cm.Spectral)
    plt.show()

    tf_features = tf.placeholder(tf.float32, shape=[None, 2]);  # None in case we want to change values
    tf_targets = tf.placeholder(tf.float32, shape=[None, 1]);

    w = tf.Variable(tf.random_normal([2, 1]));

    session = tf.Session();

    print(w);