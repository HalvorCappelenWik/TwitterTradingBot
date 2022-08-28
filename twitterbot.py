# Trading Strategy:
# Want to use Elon Musks tweets on twitter to perfrom seniment analysis.
# Based on sentiment analysis results we make a trade decision wheater or not to buy TSLA stock. :) 
# We will only consider tweets where tesla is mentioned. 
# Positive sentiment = Long
# Negate sentiment = Short
# Netural = No position 
# Will use NLTK for sentiment analysis. 


# Dataset:
# Use kaggle to find dataset containg Elon Musk tweets the from 2012 - 2017. 
# Pre process dataset using jupyter notebook, use pandas to import into a datafram.


#region imports
from AlgorithmImports import *
#endregion
from nltk.sentiment import SentimentIntensityAnalyzer

class MyAlgorithm(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2012, 11, 1)
        self.SetEndDate(2017, 1, 1)
        self.SetCash(100000)
        
        self.tsla = self.AddEquity("TSLA", Resolution.Minute).Symbol
        self.musk = self.AddData(MuskTweet, "MUSKTWTS", Resolution.Minute).Symbol
        
        self.Schedule.On(self.DateRules.EveryDay(self.tsla),
        self.TimeRules.BeforeMarketClose(self.tsla, 15), self.ExitPositions)

    def OnData(self, data):
        if self.musk in data:
            score = data[self.musk].Value
            content = data[self.musk].Tweet
            
            if score > 0.5:
                self.SetHoldings(self.tsla, 1)
            elif score < -0.5:
                self.SetHoldings(self.tsla, -1)
                
            if abs(score) > 0.5:
                self.Log("Score: " + str(score) + ", Tweet: " + content)

    def ExitPositions(self):
        self.Liquidate()


class MuskTweet(PythonData):

    sia = SentimentIntensityAnalyzer()

    def GetSource(self, config, date, isLive):
        source = "https://www.dropbox.com/s/cmi9xcvhh1cbhjl/MuskTweetsPreProcessed.csv?dl=1"
        return SubscriptionDataSource(source, SubscriptionTransportMedium.RemoteFile);

    def Reader(self, config, line, date, isLive):
        if not (line.strip() and line[0].isdigit()):
            return None
        
        data = line.split(',')
        tweet = MuskTweet()
        
        try:
            tweet.Symbol = config.Symbol
            tweet.Time = datetime.strptime(data[0], '%Y-%m-%d %H:%M:%S') + timedelta(minutes=1)
            content = data[1].lower()
            
            if "tsla" in content or "tesla" in content:
                tweet.Value = self.sia.polarity_scores(content)["compound"]
            else:
                tweet.Value = 0
            
            tweet["Tweet"] = str(content)
            
        except ValueError:
            return None
        
        return tweet