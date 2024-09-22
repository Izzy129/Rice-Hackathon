import pandas as pd

## Initializes all stock data
# All stocks

allStockPairs = pd.read_csv(r"Stock Data/all_stock_info.csv")
allStockPairs = allStockPairs.drop("Exchange", axis = 1)

nyse = allStockPairs.tail(2717)

nasdaq = allStockPairs.head(3065)

djia = pd.read_csv(r"Stock Data\bluechip_DJIA.csv")
djia = djia[["Symbol", "Company"]]

houston = pd.read_csv(r"Stock Data\houston.csv")

popularTech = pd.read_csv(r"Stock Data\popular_tech.csv")

popular = pd.read_csv(r"Stock Data\popular.csv")

sp500 = pd.read_csv(r"Stock Data\s&p500_stocks.csv")
sp500 = sp500[["Symbol", "Security"]]

## Dictionaries for each set of stocks (symbol --> name)
allStockPairDicts = dict(zip(allStockPairs.Ticker, allStockPairs.Name))
nyseDict = dict(zip(nyse.Ticker, nyse.Name))
nasdaqDict = dict(zip(nasdaq.Ticker, nasdaq.Name))
djiaDict = dict(zip(djia.Symbol, djia.Company))
houstonDict = dict(zip(houston.Ticker, houston.Company))
popularTechDict = dict(zip(popularTech.Ticker, popularTech.Company))
popularDict = dict(zip(popular.Ticker, popular.Company))
sp500Dict = dict(zip(sp500.Symbol, sp500.Security))

print(popularTechDict)