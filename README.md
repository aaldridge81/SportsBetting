# SportsBetting

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

## Setup

In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to your API Key:

    API_KEY = 'APIKEY'

## Usage
To run the program, in the command line:

```py
python legality.py
```

