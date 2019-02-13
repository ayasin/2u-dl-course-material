# 2u-dl-course-material

# Session 4

### Getting Set up

To run locally you need the following software installed:

* Anaconda
* AI Gym
* PyTorch

You can get Anaconda from [here](https://www.anaconda.com/download/).

Once Anaconda is installed, you'll need to install PyTorch.  You can do so by going to the [PyTorch website](https://pytorch.org) and following the instructions appropriate to what you're trying to install.

**PyTorch tl;dr for Mac**: run `conda install pytorch-cpu torchvision-cpu -c pytorch`

After installing PyTorch you'll need Gym.  Unfortunately there's no conda package for Gym, so it's a few extra steps.

* run `conda install libgcc`
* run `pip install gym`
* run `pip install box2d-py`

To create animations you'll need install the following:

* run `pip install git+https://github.com/jakevdp/JSAnimation.git`
* run `pip install pyglet==1.2.4` (this will downgrade pyglet to work with JSAnimation)

**For Mac**
* run `brew install ffmpeg`

**For Debian Based Linux/Ubuntu**
* run `apt install ffmpeg`

Once you're all done, you can go to the directory where you cloned the project and type:

`jupyter notebook`

If Anaconda is installed properly this should run the Jupyter notebook server.  Open a browser window and navigate to `localhost:8888`.  Once there, click on the `Session 4.ipynb` link.