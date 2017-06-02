
import csv



in_file = open("C:/Users/acedon/Desktop/american-election.csv","r") 
out_file= open("C:/Users/acedon/Desktop/neue-american-election.csv","wb" )

reader = csv.reader(in_file,delimiter=";")
writer = csv.writer(out_file,delimiter=";")

for row in reader:
    row[2] = row[2].replace("True","1")#wandelt die boolschen Werte von True/False zu 1 und 0
    row[2] = row[2].replace("False","0")
    row[4] = row[4].replace("T"," ")#Entfernt das T zum einlesen des Datums
    if row[10] != "True":#Entfernt gekürzte tweeets
                        writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[7],row[8]])# Entfernt überflüssige Rows die nicht in der Datenbank benötig werden
        
in_file.close()
out_file.close()

		
			
