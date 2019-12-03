# spacy-poc
An attemp to use spacy module with conda distribution 

### steps MacOS
 Install Homewbrew
 From Homepage of home brew find a linke similar to following or just paste the following link in terminal
 ```bash
 /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

 ```

 Test these commands to check if brew is installed successfully
 ```bash
 brew update 
 brew --help
 brew doctor 
 ```
 ### Install Conda using homebrew 
 MacOS ships with python 2.7** as of Dec 2019 you can install new version using homebrew
 ```bash
 # Test using 
 which python 
 # OR see what version by running
 python -V 
 # Finally install new one as 
 brew install python
 ```
### Install Anaconda for python 
```bash 
brew cask install anaconda
# test 
conda --help 
# or just run 
conda 

```

### python ships with pip which is a useful tool for python 
### install spacy using pip
```bash
pip install -U spacy
```
### install jupyter notebook with pip 
```bash
pip install jupyterlab
```

### Create a workspace directory 
gather data for testing any text content should be good source for raw data 

### Run 
```bash
# activate conda environment
conda activate <workspace>
# after activation run jupyter notebook 
cd workspace 
jupyter notebook 
# this should open the notebook server  and automatically open the brower for you if not 
# check console log and manually try to access notebook server 
``` 

### shutdown notebook just 

CTRL + C 




 



