#City name converter

`City name converter` is a simple application written in Python with web layer written in Flask.
In order to launch it in your browser, follow these steps:
1. Make sure you have Python 3 installed, as well as `pip`
2. Run `pip install -r requirements.txt`
3. Set `FLASK_APP` local variable to `simple.py` 

    `export FLASK_APP=simple.py` on Linux\Unix
    
    `set FLASK_APP=simple.py` on Windows
4. Run `flask run` - this starts local server with application, that you can access on `localhost:8000`

Besides you can run `python -m converter <city-name>` or `python -m decryptor <city-number>` in your command shell

##How does it work
Converter generates unique number for given city name. Process is reversible, so
it can be decoded using the Decryptor.
The Converter uses quite naive approach:
   1. Convert all letters to corresponding ascii numbers
   2. Since only lowercase letters are handled, most of the letters have 3-digit representation. Two 
   digit letters are handled by adding prefixes in the following manner:
   
           add '-' if letter is at the beginning,
           
           add '0' if letter is in the middle
   3. Concatenate the resulting string of numbers

This ensures that each unique name will have it's unique representation.
Decrypting such number is just the above process reversed.

##Why flask?
Django is too heavy for such a simple one-page application, I just wanted to provide simple routing and 
requests handling.

##Unittests
In order to run tests run `python -m unittest test.py`
