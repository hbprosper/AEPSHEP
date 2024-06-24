# Asia-Europe-Pacific School of HEP (AEPSHEP)
## Introduction
This repository contains tutorials (as jupyter notebooks) on
statistics and machine learning associated with the lectures at this
school. 


## Dependencies
The notebooks in this package depend on several well-known
well-engineered and free Python modules.

| __modules__   | __description__     |
| :---          | :---        |
| pandas        | data table manipulation, often with data loaded from csv files |
| numpy         | array manipulation and numerical analysis      |
| matplotlib    | a widely used plotting module for producing high quality plots |
| imageio.v3      | photo-quality image display module |
| scikit-learn  | easy to use machine learning toolkit |
| pytorch       | a powerful, flexible, research-level machine learning toolkit |
| scipy         | scientific computing    |
| sympy        | an excellent symbolic mathematics module |
| iminuit | an elegant wrapper around the venerable CERN minimizer Minuit |
| emcee | one of many, many, Markov chain Monte Carlo modules |
| tqdm         | progress bar |
| joblib | module to save and load Python objects |
| importlib | importing and re-importing modules |


##  Installation
The simplest way to install these Python modules is first to install miniconda (a slim version of Anaconda) on your laptop by following the instructions at:

https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

I recommend installing miniconda3, which comes pre-packaged with Python 3.

Software release systems such as Anaconda (__conda__ for short) make
it possible to have several separate self-consistent named
*environments* on a single machine, say your laptop. For example, you
may need to use Python 3.7.5 and an associated set of compatible
packages and at other times you may need to use Python 3.9.13 with
packages that require that particular version of Python.  If you install software without using *environments* there is
the danger that the software on your laptop will eventually become
inconsistent. Anaconda (and its lightweight companion miniconda)
provide a way, for example, to create a software *environment*
consistent with Python 3.7.5 and another that is consistent with
Python 3.9.13.  For example,
one package may work only with a given version of numpy, while another
requires a different version. In principle, having different versions of numpy on
your machine, just
like having different versions of Python, is not a problem if one uses
environments.

Of course, like anything human beings make, miniconda3 is not
perfect. There are times when the only solution is to delete an
environment and rebuild by reinstalling the desired packages.

### Miniconda3

After installing miniconda3, It is a good idea to update conda using the command
```bash
conda update conda
```
#### Step 1 
Assuming conda is properly installed and initialized on your laptop, you can create an environment, here called *aepshep*. 
```bash
conda create --name aepshep
```
and activate it by doing
```bash
conda activate aepshep
```
You need create the environment only once, but you must activate the desired environment whenever you create a new terminal window.

#### Step 2 
Install root, python, numpy, … (Tip: search the web for **conda install** and the
module name to get the exact syntax just in case it has changed.)
```
	conda install –c conda-forge root
```
If all goes well, this will install a recent version of the [ROOT](https://root.cern.ch) package from CERN as well as *Python* and several Python modules including *numpy*.

#### Step 3
Install *pytorch*, *matplotlib*, *scikit-learn*, etc.
```bash
	conda install –c conda-forge pytorch
	conda install –c conda-forge matplotlib
	conda install –c conda-forge scikit-learn
	conda install –c conda-forge pandas
	conda install –c conda-forge sympy
	conda install –c conda-forge imageio.v3
	conda install –c conda-forge jupyter
```
Again be sure to check the exact syntax. This does change from time to time!

#### Step 4
Install __git__ if it is not yet on your system, then download the AEPSHEP package.
```bash
	conda install –c conda-forge git
	mkdir tutorials
	cd tutorials
	git clone https://github.com/hbprosper/AEPSHEP
```
In the above the package AEPSHEP has been downloaded into a directory called *tutorials*.

#### Step 5

Open a new terminal window, navigate to the directory (folder) that contains AEPSHEP, and run  **jupyter lab** in that window (in blocking mode).
```bash
	jupyter lab
```
If all goes well, the jupyter lab environment will appear in your default browser. 
Navigate to the AEPSHEP directory and under the *Files* menu item, click on the notebook *test.ipynb* and execute it. This notebook tries to import several Python modules. If it does so without error messages, you are ready to try out the other notebooks.


## Tutorials

### Statistics
| __notebook__   | __description__     |
| :---          | :---        |
| 01_rootn         | coverage of root(N) upper limits     |
| 02_wilks    | Wilks' theorem |
| 03_atlas_opendata_4l_fit | Bayesian fit to ATLAS 4-lepton open data |
|04_cms_diphoton_fit | fit to the CMS 7 and 8 TeV di-photon (Higgs boson discovery) data |
| 05_profile_likelihood | simple example of construction of profile likelihood |


### Machine Learning
| __notebook__   | __description__     |
| :---          | :---        |
| 01_hzz4l_sklearn | classification (with AdaBoost BDT) of VBF/ggF production of Higgs boson |
| 02_hzz4l_pytorch| classification (with feed-forward NN) of VBF/ggF production of Higgs boson|
| 03_qg_classification | classification (with CNN) of quark/gluon jet images|
| 04_diffusion_model| example of mapping 2D Gaussian noise to a desired distribution|
