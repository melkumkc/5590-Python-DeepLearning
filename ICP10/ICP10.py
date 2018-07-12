# # Word2Vec

# The code for this lecture is based off the great tutorial example from tensorflow!
# Walk through:
# https://www.tensorflow.org/tutorials/word2vec
# Raw Code: https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/tutorials/word2vec/word2vec_basic.py

# # Step 0: Imports
import collections
import math
import os
import errno
import random
import zipfile

import numpy as np
from six.moves import urllib
from six.moves import xrange
from collections import Counter
import tensorflow as tf
from tensorflow.contrib.tensorboard.plugins import projector

# # Step 1: The data.
data_dir = "data"
data_url = 'http://mattmahoney.net/dc/text8.zip'


def fetch_words_data(url=data_url, words_data=data_dir):
    # Make the Dir if it does not exist
    os.makedirs(words_data, exist_ok=True)

    # Path to zip file
    zip_path = os.path.join(words_data, "words.zip")

    # If the zip file isn't there, download it from the data url
    if not os.path.exists(zip_path):
        urllib.request.urlretrieve(url, zip_path)

    # Now that the zip file is there, get the data from it
    with zipfile.ZipFile(zip_path) as f:
        data = f.read(f.namelist()[0])

    # Return a list of all the words in the data source.
    return data.decode("ascii").split()


# Use Defaults (this make take awhile!!)
words = fetch_words_data()

# Total words
print("Total length of words is: ", len(words))

for w in words[9000:9040]:
    print(w, end=' ')


## Build Word Counts and Create Word Data and Vocab
#******************************************************************** Changed vocablary size to 100 to reduce processing time
def create_counts(vocab_size=100):
    # Begin adding vocab counts with Counter
    vocab = [] + Counter(words).most_common(vocab_size)

    # Turn into a numpy array
    vocab = np.array([word for word, _ in vocab])

    dictionary = {word: code for code, word in enumerate(vocab)}
    data = np.array([dictionary.get(word, 0) for word in words])
    return data, vocab


vocab_size = 100

# This may take awhile
data, vocabulary = create_counts(vocab_size=vocab_size)


# ## Function for Batches

def generate_batch(batch_size, num_skips, skip_window):
    global data_index
    assert batch_size % num_skips == 0
    assert num_skips <= 2 * skip_window
    batch = np.ndarray(shape=(batch_size), dtype=np.int32)
    labels = np.ndarray(shape=(batch_size, 1), dtype=np.int32)
    span = 2 * skip_window + 1  # [ skip_window target skip_window ]
    buffer = collections.deque(maxlen=span)
    if data_index + span > len(data):
        data_index = 0
    buffer.extend(data[data_index:data_index + span])
    data_index += span
    for i in range(batch_size // num_skips):
        target = skip_window  # target label at the center of the buffer
        targets_to_avoid = [skip_window]
        for j in range(num_skips):
            while target in targets_to_avoid:
                target = random.randint(0, span - 1)
            targets_to_avoid.append(target)
            batch[i * num_skips + j] = buffer[skip_window]
            labels[i * num_skips + j, 0] = buffer[target]
    if data_index == len(data):
        buffer[:] = data[:span]
        data_index = span
    else:
        buffer.append(data[data_index])
        data_index += 1
    # Backtrack a little bit to avoid skipping words in the end of a batch
    data_index = (data_index + len(data) - span) % len(data)
    return batch, labels


data_index = 0
batch, labels = generate_batch(8, 2, 1)

# Size of the bath
batch_size = 128
#.....................................  Embading size
                                        # #how many dimensions the embeding vector will have
                                        # the higher dimension the higher accuracy of nearby words
                                        # the higher dimension the higher training time
# Dimension of embedding vector
embedding_size = 10

# How many words to consider left and right (the bigger, the longer the training)
#..........................................................................Context window, the higher context window the higher accuracy
skip_window = 1

# How many times to reuse an input to generate a label
num_skips = 2

# We pick a random validation set to sample nearest neighbors. Here we limit the
# validation samples to the words that have a low numeric ID, which by
# construction are also the most frequent.

# Random set of words to evaluate similarity on.
valid_size = 16

# Only pick dev samples in the head of the distribution.
valid_window = 100
valid_examples = np.random.choice(valid_window, valid_size, replace=False)

# Number of negative examples to sample.
num_sampled = 64

# Model Learning Rate
#..................................... Learning rate
                                        # On the optimization curve the length of each step on the optimization curve
                                        # The higher the lerning rate the higher the step length, this gives low optimization result
                                        #B /c there will be hiher probability of missing the optimal point
                                        # The higher the learning rate the longer the training time
                                        # The higher the learning rate the higher the accuracy
learning_rate = 1.0

# How many words in vocab
#************************************* The vocabulary_size was reduced in order to reduce the running time
vocabulary_size = 100

# ## TensorFlow Placeholders and Constants

tf.reset_default_graph()

# Input data.
train_inputs = tf.placeholder(tf.int32, shape=[None])
train_labels = tf.placeholder(tf.int32, shape=[batch_size, 1])
valid_dataset = tf.constant(valid_examples, dtype=tf.int32)

# ### Variables

# Look up embeddings for inputs.
init_embeds = tf.random_uniform([vocabulary_size, embedding_size], -1.0, 1.0)
embeddings = tf.Variable(init_embeds)

embed = tf.nn.embedding_lookup(embeddings, train_inputs)

# ### NCE Loss

# Construct the variables for the NCE loss
nce_weights = tf.Variable(tf.truncated_normal([vocabulary_size, embedding_size], stddev=1.0 / np.sqrt(embedding_size)))
nce_biases = tf.Variable(tf.zeros([vocabulary_size]))

# Compute the average NCE loss for the batch.
# tf.nce_loss automatically draws a new sample of the negative labels each
# time we evaluate the loss.
loss = tf.reduce_mean(
    tf.nn.nce_loss(nce_weights, nce_biases, train_labels, embed,
                   num_sampled, vocabulary_size))

# ### Optimizer

# Construct the Adam optimizer
optimizer = tf.train.AdamOptimizer(learning_rate=1.0)
trainer = optimizer.minimize(loss)

# Compute the cosine similarity between minibatch examples and all embeddings.
norm = tf.sqrt(tf.reduce_sum(tf.square(embeddings), axis=1, keepdims=True))
normalized_embeddings = embeddings / norm
valid_embeddings = tf.nn.embedding_lookup(normalized_embeddings, valid_dataset)
similarity = tf.matmul(valid_embeddings, normalized_embeddings, transpose_b=True)

# Add variable initializer.
init = tf.global_variables_initializer()

# # Session
# Usually needs to be quite large to get good results,
# training takes a long time!
#...........................................num_steps
                                            # the number of iteration that we will do in order to find the optimam point on the curve
                                            # the higher the num_steps the larger the num_steps we take
                                            # the higher the num_steps the higher accuracy
num_steps = 10000
config = projector.ProjectorConfig()
embedding = config.embeddings.add()
dimensions = [100,100]
embedding.sprite.single_image_dim.extend (dimensions)


with tf.Session() as sess:
    writer = tf.summary.FileWriter('./graphs/linear_reg', sess.graph)
    projector.visualize_embeddings(writer,config)
    sess.run(init)
    average_loss = 0
    for step in range(num_steps):

        batch_inputs, batch_labels = generate_batch(batch_size, num_skips, skip_window)
        feed_dict = {train_inputs: batch_inputs, train_labels: batch_labels}

        # We perform one update step by evaluating the training op (including it
        # in the list of returned values for session.run()
        empty, loss_val = sess.run([trainer, loss], feed_dict=feed_dict)
        average_loss += loss_val

        if step % 1000 == 0:
            if step > 0:
                average_loss /= 1000
            # The average loss is an estimate of the loss over the last 1000 batches.
            print("Average loss at step ", step, ": ", average_loss)
            average_loss = 0

    final_embeddings = normalized_embeddings.eval()
    writer.close()

# # Visualizing Results

import matplotlib.pyplot as plt


def plot_with_labels(low_dim_embs, labels):
    assert low_dim_embs.shape[0] >= len(labels), "More labels than embeddings"
    plt.figure(figsize=(18, 18))  # in inches
    for i, label in enumerate(labels):
        x, y = low_dim_embs[i, :]
        plt.scatter(x, y)
        plt.annotate(label,
                     xy=(x, y),
                     xytext=(5, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')


# ## TSNE
# * https://lvdmaaten.github.io/tsne/
# * https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding
# Dimensionality reduction to 2-D vectors (down from 150), this takes awhile.

from sklearn.manifold import TSNE

tsne = TSNE(perplexity=30, n_components=2, init='pca', n_iter=250)
plot_only =100
low_dim_embs = tsne.fit_transform(final_embeddings[:plot_only, :])

labels = [vocabulary[i] for i in range(plot_only)]

plot_with_labels(low_dim_embs, labels)
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.show()

## Great Job!