#IUU Fishing Models Environment setup instructions using Bash
##Python
<p>In terminal, enter "python -V"</p>
<p>If no values are returned, install Python 2.7</p>
<p>If the version is Python 3.x, install Python 2.7. Consider naming path Python2, and using Python2 instead of Python for all future instruction.</p>

##VirtualEnv & VirtualEnvWrapper
<p>In terminal, enter "virtualenv virtualenvwrapper virtualenvwrapper.sh"</p>
<p>If virtualenv isn't installed, install virtualenv</p>
<p>See <a href="http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/">VirtualEnv Documentation</a></p>
<p>If virtualenvwrapper(.sh) isn't installed, install virtualenvwrapper(.sh)</p>
<p>See https://virtualenvwrapper.readthedocs.io/en/latest/</p>

<p>Make a virtual environment using Python 2.7 as the default env path.</p>
<p>mkvirtualenv -p {path to Python 2.7} iuu_fishing_detection</p>

##Pip
<p>In terminal, enter "pip -V"</p>
<p>If no values are returned, install pip</p>
<p>If pip defaults to pip for python 3.x, find command to run pip using python 2.7</p>

##git & git-lfs
<p>In terminal, enter "which git git-lfs"</p>
<p>If no path is returned for git, install git</p>
<p>If no path is returned for git-lfs, install git-lfs</p>

<p>Make a directory for the project if it doesn't already exist,
and change to that directory from the command line</p>

##Get necessary repositories
<p>git-lfs clone git@github.com:GlobalFishingWatch/training-data.git</p>
<p>git-lfs clone</p> git@github.com:GlobalFishingWatch/vessel-scoring.git</p>
<p>git-lfs clone git@github.com:jgessert/iuu-fishing-modelss.git</p>

##Download Geos
<p>For Mac, download Homebrew, then run
brew install geos</p>

<p>For Ubuntu, run</p>
<p>sudo apt-get install libgeos-dev</p>

##Download necessary Python packages
<p>pip install -r iuu-fishing-models/requirements.txt</p>

<p>cd training-data</p>
<p>sh prepare.sh</p>
<p>sh iuu-fishing-models/setup.sh</p>

##Derive data (1 - 3 hours)
<p>sh iuu-fishing-models/derive_data.sh</p>
