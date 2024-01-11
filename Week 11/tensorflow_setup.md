# Tensorflow Setup

In order to work with neural networks in python, we need to install tensorflow and we will speciffically focus on using tensorflow.keras which is a high level API for training neural networks.

- Tensorflow official cite: https://www.tensorflow.org/
- Tensorflow official documentation: https://www.tensorflow.org/api_docs/python/tf
- Tensorflow.keras official documentation: https://www.tensorflow.org/api_docs/python/tf/keras

Here we will add tensorflow to our already prepared conda enviroment. We will install cpu version of the tensorflow because we will work with small neural networks and we don't need the gpu version.

```bash 
conda activate vi1
pip install tensorflow-cpu
```