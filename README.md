# Fintech Bootcamp - Project 3

By Daniel Case, Jacob Steen, Richard Rosenthal

## Summary

In this project, we've assumed the role of a large tech company looking for an acquisition target.  The goal of this project is to use an unsupervised learning model to identify potential companies for acquisition, and then run a discounted cash flow (DCF) model on those companies to select one to acquire.  This project has several components:

1) Select a group of potential acquisition targets (mid-cap tech companies)
2) Use the FinanceToolkit API to collect balance sheet and income statement information about those companies
3) Identify a group of companies in the past that were good acquisition targets
4) Use the FinanceToolkit API to collect the same information about those companies
5) Use an unsupervised learning model to cluster the potential acqusition targets with the good acquisition targets
6) Identify a cluster where the number of good acquisition targets is relatively high
7) Run a discounted cash flow (DCF) model on the potential acquisition targets in the same cluster looking for a "cheap" company to acquire
8) The DCF shows sensitivity to interest rate and tax environments so proper analysis could be used to evaluate possible mergers

### Primary Code

The primary code can be found in the following files:

- Data_Acquisition.ipynb (Uses the FinanceToolkit API to collect data on potential and historical acquisition targets, and creates a CSV of the relevant information)
- Unsupervised_Model.ipynb (Reads the CSV created by the Data Acquisition file, prepares the data for analysis, runs KMeans and DBSCAN analyses on both the original data and PCA data)
- FinanceToolKit.ipynb(Using the API it pulls balance/income statements for the list of 49 potential targets)
- TargetModel.py(set target criteria from a list of three tickers) determined which one met the target criteria. 

### Data Files

The CSV files created by Data_Acquisition.ipynb can be found in the Data_Files folder.

### Saved Plots

The saved plots created by Unsupervised_Model.ipynb can be found in the Saved_Plots folder.
