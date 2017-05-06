#IUU Fishing Models Environment setup instructions using Bash
##Python
In terminal, enter "python -V"

If no values are returned, install Python 2.7

If the version is Python 3.x, install Python 2.7. Consider naming path Python2, and using Python2 instead of Python for all future instruction.


##VirtualEnv & VirtualEnvWrapper
In terminal, enter "virtualenv virtualenvwrapper virtualenvwrapper.sh"

If virtualenv isn't installed, install virtualenv

See <a href="http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/">VirtualEnv Documentation</a>

If virtualenvwrapper(.sh) isn't installed, install virtualenvwrapper(.sh)

See https://virtualenvwrapper.readthedocs.io/en/latest/


Make a virtual environment using Python 2.7 as the default env path.

mkvirtualenv -p {path to Python 2.7} iuu_fishing_detection


##Pip
In terminal, enter "pip -V"

If no values are returned, install pip

If pip defaults to pip for python 3.x, find command to run pip using python 2.7


##git & git-lfs
In terminal, enter "which git git-lfs"

If no path is returned for git, install git

If no path is returned for git-lfs, install git-lfs


Make a directory for the project if it doesn't already exist,
and change to that directory from the command line


##Get necessary repositories
git-lfs clone git@github.com:GlobalFishingWatch/training-data.git

git-lfs clone
 git@github.com:GlobalFishingWatch/vessel-scoring.git

git-lfs clone git@github.com:jgessert/iuu-fishing-modelss.git


##Download Geos
For Mac, download Homebrew, then run
brew install geos


For Ubuntu, run

sudo apt-get install libgeos-dev


##Download necessary Python packages
pip install -r iuu-fishing-models/requirements.txt


cd training-data

sh prepare.sh

sh iuu-fishing-models/setup.sh


##Derive data (1 - 3 hours)
sh iuu-fishing-models/derive_data.sh
