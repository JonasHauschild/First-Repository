if __name__ == '__main__':
    f = open('text text.txt', 'r+')
    f.write('gude \nwas geht ab?')
    f.close()

# öffnet text datei mit namen 'text' im Modus r+
# schreibt in text datei das Word 'Gude, was geht?'
# w modus würde Datei überschreiben
# a modus fügt geschriebenes hinzu
# r+ modus lesen und schreiben