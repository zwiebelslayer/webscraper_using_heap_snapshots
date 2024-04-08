# Purpose
Scrape Website using a heap snapshot created by playwright, then parse the heap snapshot for the desired data 

# How to install
Clone this repo, then cd to the lib dir here and pip install ./parser
this will build the c libraray and install it into your local python env.
Make sure to install playwright afterwards. 
Then you should be able to use the HPScraper Interface :)

# Requirements
- Cmake >= 3.25 (or change the version in the CMake files)
- On Windows: only MSVC compiler > 2017 is supported (this is a pybind11 limitation)
- Playwright (the heap snapshot is created with this)


# Roadmap
- Implement the JSON parser using SMID Instructions.
- Add the setup.py file to make this a self sufficient library
- optimize, by reducing unnecessary copys and start using pass by reference, e.g the json file contents are copied as of now 
- allow to query by value, to make it easier to find the right query params
- Docker
- async playwright implementation and batches