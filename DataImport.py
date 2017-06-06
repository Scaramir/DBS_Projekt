
import psycopg2
#Läd die Daten durch eine psycopg2 Verbindung mit der postgresql Datenbank,
#über eine SQL Querie in die election Datenbank
#der Cursor ermöglicht die connection und execute führt die jeweiligen
#Sql Statements aus!
connection = psycopg2.Connect(host='localhost', user='kikou', passwd='hallo123', db='election')
cursor = connection.cursor()
query1 = "LOAD DATA LOW_PRIORITY LOCAL INFILE 'C:/Users/acedon/Desktop/new-american-election.csv' INTO TABLE tweets CHARACTER SET ascii FIELDS TERMINATED BY ';' ENCLOSED BY '\"' ESCAPED BY '\"' LINES TERMINATED BY '\\r\n' IGNORE 1 LINES (`TEXT`, `REPLY_TO`, `DATUM`, `is_quote`, `RETWEET_CNT`, `LIKE_CNT`, `ID`, `truncated`);"
query2 = "LOAD DATA LOW_PRIORITY LOCAL INFILE 'C:/Users/acedon/Desktop/hashtags.csv' INTO TABLE hashtag CHARACTER SET ascii FIELDS TERMINATED BY ';' ENCLOSED BY '\"' ESCAPED BY '\"' LINES TERMINATED BY '\\r\n' (`HASHTAGS`, `ID`);"
cursor.execute( query1 )
cursor.execute( query2 )
connection.commit()
