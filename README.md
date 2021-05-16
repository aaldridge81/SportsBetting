# SportsBetting


## Setup

Clone or download repo from https://github.com/wpp5/robo-advisor onto your desktop

Nagivate from command line:
```sh
cd Desktop/SportsBetting
```

Obtain a unique API key from AlphaVantage: 
https://the-odds-api.com/#get-access

Create a file called .env within the local repo:

Within .env file, assign your unique API to the enviroment variable API_KEY

```sh 
API_KEY="abc123"
```
Substitute your unique API Key for "abc123"


Once the program is cloned, the user should enter 
```sh
cd ~/Desktop/shopping-cart
```
into their command line, if they cloned it to their desktop, to navigate to the program.


## Environment Setup

Use Anaconda to create and activate a new virtual environment, called "shopping-env": 
```sh
conda create -n betting-env python=3.8
conda activate betting-env 
```

from inside virtual environment, install package dependencies:
```sh
pip install -r requirements.text
```

> NOTE: If installation causes an error message, make sure you are navigating within the repository's root directiory, where the requirements.txt file exists 



## Usage
To run the program, in the command line:

```py
python legality.py
```

