# Alpaca-ML-CANSLIM-Trader
This repository is an in-progress project. 

This is a stock trading program using the CANSLIM analysis algorithm. We use Alpaca (a python paper trading API) with machine learning algorithms to simulate stock trading. Right now the program is limited and full off errors that need to be debugged but with a little nurturing it can grow to a full-fledged awesome project.

# Motivation Behind the Project
This project was made as a sandbox type of project to become familiar with Machine Learning in Python and explore stock trading with machine learning. 

# Programming Style
For those on the team here are some programming style tips to keep in mind:
1. Use comments and update the read me file when necessary. Documentation is key!
2. Tabs not spaces
3. Use clear variable names and don't change current ones
.... and so on....

# Technology and Concepts Used 

## Alpaca API
Alpaca is an API for stock trading. Although it can be used with other languages, python is the best language to use for our needs. Alpaca can be used for actual trades on the stock market but for our purposes and because of the significant risks associated with just letting an AI trade on the stock market we will use it primarily for paper trading. 

This means we aren't working with real money and instead are using a simulated version of the stock market. 
https://app.alpaca.markets/login

## Python 3
Python 3 is the current version of Python. Its a great language for beginners, for machine learning and just in general for getting really specific projects done. Because python has so many specific libraries you can use with it, we need to use python for our purposes to use the libraries we are using. 

Python can be downloaded here:
https://www.python.org/downloads/

The developers of python made this nice guide for beginners if you are unfamiliar with the language:
https://www.python.org/about/gettingstarted/

## CANSLIM Analysis
CANSLIM is a type of anaylsis used in finance to analyze a specific stocks. For our purposes we need to refine it into data - this means putting it into a .csv file that we can work with in python and populating the columns with information. 

For details about what the acronym stands for see here:
https://www.investopedia.com/terms/c/canslim.asp#:~:text=Understanding%20CANSLIM&text=Each%20letter%20in%20the%20acronym,reported%20in%20the%20prior%20year.

Using CANSLIM in a data analysis context poses several issues, the first is that CANSLIM is a technique meant to be done by a human so the data is not readily accessible for all the columns. Certain columns such as the N for novelty are also subjective. How do we quantify novelty and easily get access to that data in large amounts? Another issue is that CANSLIM anaylsis columns are widely debated. While we know where to find specific data for columns L which uses the Relative Strength Index, other columns are less clear. 

These are just a few of the problems in taking the CANSLIM analysis concept and refining it into a dataset. 

## Tensorflow
Tensorflow is one of the most common python libraries for working with machine learning. For our purposes it will be incredibly useful. 

Instructions on how to install tensorflow with pip can be found here:
https://www.tensorflow.org/install/pip


# Installation
You will need python installed and a paper trading account to connect to. If you are working on the team we have a paper trading account so ask for the up-to-date credentials i.e. api_key, api_secret and base_url. The .csv version of the canslim analysis will also need to be in the same folder as the program or have a connected path. This can be found in the data folder. 

Always specify api_version = 'v2' when connecting to the API

