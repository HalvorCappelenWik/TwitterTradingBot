# TwitterTradingBot

Denne tradingbot-en utfører kjøp og salg av tesla stock basert på Elon Musks sine tweets på twitter! 

Trading Strategi:
Henter ut dataset som består av Elon musk sine tweets fra perioden 2012 - 2017. (skal oppdateres med 2010 - 2022)<br/>
Dette datasettet filteres og vi undersøker kun tweets som inneholder "tesla" eller "tsla". <br/>
For hver eneste tweet utføres en sentiment analyse ved hjelp av NLTK. <br/>
Basert på analysen vil vi enten ta en posisjon i tsla eller ikke. <br/>  <br/>
Positive sentiment = Long <br/>
Negate sentiment = Short <br/>
Netural = No position


# Backtesting results 

Se logs.txt for hvilke tweets som utløste kjøpsordre! 

<img width="1026" alt="Screenshot 2022-08-28 at 11 22 39" src="https://user-images.githubusercontent.com/91557392/187067067-c8aa98b7-ca13-4b0b-9a3b-fb7b9513afc7.png">

<img width="820" alt="Screenshot 2022-08-28 at 11 21 08" src="https://user-images.githubusercontent.com/91557392/187067019-9662449e-8619-414d-9abc-b33b32bfeb19.png">

<img width="691" alt="Screenshot 2022-08-28 at 11 22 10" src="https://user-images.githubusercontent.com/91557392/187067059-c0edc98e-aac1-404e-8a86-c9ceaf86b534.png">
