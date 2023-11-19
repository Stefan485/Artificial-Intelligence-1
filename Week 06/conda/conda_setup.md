
# Conda Package Manager

Package, dependency and environment management for any language—Python, R, Ruby, Lua, Scala, Java, JavaScript, C/ C++, Fortran, and more.

Visit [Conda](https://docs.conda.io/en/latest/) for more information.

We will use conda to organize out python packages for this course.

Miniconda is a free minimal installer for conda. It is a small, bootstrap version of Anaconda that includes only conda, Python, the packages they depend on, and a small number of other useful packages, including pip, zlib and a few others. Use the conda install command to install 720+ additional conda packages from the Anaconda repository.

Miniconda is installed in our classroom and it will be enough for this course.
Install [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/).

You can also install [Anaconda](https://www.anaconda.com/) instead of Miniconda if you prefer.

Check out most important conda commands in cheat sheet downloaded from conda website
`conda-cheatsheet.pdf` or visit their official documentation [here](https://docs.conda.io/en/latest/).

## Conda environments

Conda environments are isolated from each other and allow us to have different versions of Python and/or packages installed in each environment. This is useful when we need to use different versions of packages for different projects.

We can create a new environment with a specific version of Python and activate it with the following commands:

```bash
conda create -n ENVNAME python=3.6
conda activate ENVNAME
```
You do not need to specify the version of Python if you want to use the default version.

To list all the environments we can use the following command:

```bash
conda env list
```

## Conda packages

To install a package (for example numpy) in the environment we can use the following command:

```bash
conda install numpy
```

FOr installation of the packages you can also use pip. However, it is recommended to use conda for installation of the packages.

```bash
pip install numpy
```

To list all the packages installed in the environment we can use the following command:

```bash
conda list
```

To export the list of packages installed in the environment to a file we can use the following command:

```bash
conda env export --from-history>env.yml
```

This command will create a file `env.yml` with the list of packages installed in the environment.

To create an environment from the file `env.yml` we can use the following command:

```bash
conda env create -n ENVNAME --file env.yml
```

## Setup

To setup the environment for this course we will use the file `env.yml` from this directory. This environment contains almost all the packages we will need for this course.

```bash
conda env create -n vi1 --file env.yml
```

Do not forget to activate the environment before you start working on the assignments.

```bash
conda activate vi1
```


