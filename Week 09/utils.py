import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

def visualize_decision_boundary(x, y, model, ax=None, title="Decision boundary"):
    # define bounds of the domain
    additional_space = 0.1
    precision = 0.001
    min1, max1 = x[:, 0].min()-additional_space, x[:, 0].max()+additional_space
    min2, max2 = x[:, 1].min()-additional_space, x[:, 1].max()+additional_space
    # define the x and y scale
    x1grid = np.arange(min1, max1, precision)
    x2grid = np.arange(min2, max2, precision)
    # create all of the lines and rows of the grid
    xx, yy = np.meshgrid(x1grid, x2grid)
    # flatten each grid to a vector
    r1, r2 = xx.flatten(), yy.flatten()
    r1, r2 = r1.reshape((len(r1), 1)), r2.reshape((len(r2), 1))
    # horizontal stack vectors to create x1,x2 input for the model
    grid = np.hstack((r1,r2))
    # make predictions for the grid
    yhat = model.predict(grid)
    # reshape the predictions back into a grid
    zz = yhat.reshape(xx.shape)
    # plot the grid of x, y and z values as a surface
    if ax is None:
      plt.title(title)
      plt.contourf(xx, yy, zz, cmap='Paired')
      # create scatter plot for samples from each class
      for class_value in range(2):
          # get row indexes for samples with this class
          row_ix = np.where(y == class_value)
          # create scatter of these samples
          plt.scatter(x[row_ix, 0], x[row_ix, 1])
    else:
      ax.set_title(title)
      ax.contourf(xx, yy, zz, cmap='Paired')
      # create scatter plot for samples from each class
      for class_value in range(2):
          # get row indexes for samples with this class
          row_ix = np.where(y == class_value)
          # create scatter of these samples
          ax.scatter(x[row_ix, 0], x[row_ix, 1]) 

def sample_gaussian(mean,cov):
  w,v=np.linalg.eig(cov)
  z=np.random.normal(0,1,mean.shape[0])
  return mean+v.dot(w*z)

def get_n_samples(n,mean,cov):
  samples=[]
  for i in range(n):
    samples.append(sample_gaussian(mean,cov))
  return np.array(samples)

def create_filter(arr, x_min, x_max, y_min, y_max):
  return (arr[:,0] >= x_min) & (arr[:,0] <= x_max) & (arr[:,1] >= y_min) & (arr[:,1] <= y_max)

def create_dataset(mean1, cov1, mean2, cov2, n1, n2, bounds):
  assert type(mean1) == list and type(mean2) == list and type(cov1) == list and type(cov2) == list \
         and type(n1) == list and type(n2) == list and type(bounds) == list
  x1_list = [get_n_samples(n1[i], mean1[i], cov1[i]) for i in range(len(mean1))] 
  x2_list = [get_n_samples(n2[i], mean2[i], cov2[i]) for i in range(len(mean2))]
  x1 = np.concatenate(x1_list)
  x2 = np.concatenate(x2_list)
  y1 = np.zeros(len(x1))
  y2 = np.ones(len(x2))
  x = np.concatenate((x1, x2))
  y = np.concatenate((y1, y2))
  filter = create_filter(x, bounds[0], bounds[1], bounds[2], bounds[3])
  x = x[filter]
  y = y[filter]
  return x, y

def get_linearly_separable_syntetic_dataset():
    num_samples_class1 = [100]
    mean_class1 = [np.array([0.2, 0.2])]
    cov_class1 = [np.array([[0.25, 0],[0, 0.25]])]
    num_sample_class2 = [100]
    mean_class2 = [np.array([0.8, 0.8])]
    cov_class2 = [np.array([[0.25, 0],[0, 0.25]])]
    bounds = [0, 1, 0, 1]
    return create_dataset(mean_class1, cov_class1, mean_class2, cov_class2, num_samples_class1, num_sample_class2, bounds)

def get_non_linearly_separable_syntetic_dataset():
    num_samples_class1 = [20, 20, 20, 30, 20, 20, 10, 20]
    mean_class1 = [np.array([0.2, 0.1]), np.array([0.1, 0.3]), np.array([0.4, 0.4]), np.array([0.8, 0.1]), np.array([0.7, 0.4]), np.array([0.1, 0.7]), np.array([0.2, 0.83]), np.array([0.4, 0.2])]
    cov_class1 = [np.array([[0.2, 0],[0, 0.2]]), np.array([[0.05, 0],[0, 0.1]]), np.array([[0.12, 0],[0, 0.07]]), np.array([[0.15, 0],[0, 0.1]]), np.array([[0.05, 0.15],[0.15, 0.05]]), np.array([[0.05, 0],[0, 0.15]]), np.array([[0.1, 0],[0, 0.05]]), np.array([[0.2, 0],[0, 0.1]])]
    num_sample_class2 = [20, 10, 20, 20, 30, 20, 10, 10]
    mean_class2 = [np.array([0.8, 0.9]), np.array([0.4, 0.6]), np.array([0.4, 0.8]), np.array([0.9, 0.85]), np.array([0.95, 0.35]), np.array([0.53, 0.87]), np.array([0.22, 0.53]), np.array([0.55, 0.8])]
    cov_class2 = [np.array([[0.2, 0],[0, 0.2]]), np.array([[0.08, 0],[0, 0.05]]), np.array([[0.1, -0.07],[-0.07, 0.15]]), np.array([[0.15, 0],[0, 0.1]]), np.array([[0.07, 0],[0, 0.2]]), np.array([[0.15, -0.1],[-0.1, 0.15]]), np.array([[0.07, 0],[0, 0.05]]), np.array([[0.15, 0],[0, 0.15]])]  
    bounds = [0, 1, 0, 1]
    return create_dataset(mean_class1, cov_class1, mean_class2, cov_class2, num_samples_class1, num_sample_class2, bounds)

def get_test_dataset():
    num_samples_class1 = [20]
    mean_class1 = [np.array([0.55, 0.35])]
    cov_class1 = [np.array([[0.05, 0.1],[0.1, 0.05]])]
    num_sample_class2 = [20]
    mean_class2 = [np.array([0.5, 0.83])]
    cov_class2 = [np.array([[0.1, -0.1],[-0.1, 0.1]])]
    bounds = [0, 1, 0, 1]
    return create_dataset(mean_class1, cov_class1, mean_class2, cov_class2, num_samples_class1, num_sample_class2, bounds)


