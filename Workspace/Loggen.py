import logging #protokollieren


def f():
    logger = logging.getLogger('programm.klasse.f')
    logger.setLevel(logging.DEBUG)
    logger.debug('in der Funktion')


logging.basicConfig(filename='text log.log', level=logging.INFO)  # Main-Logger mit Level INFO der initialisiert wurde

logger = logging.getLogger('meinLogger')  # neuer logger (nicht logging wie in Main-Logger)der hinzugefügt wird mit Name meinLogger

logger.setLevel(logging.DEBUG)  # neuer Logger hat neues Level (DEBUG statt INFO)

file = logging.FileHandler('text logme.txt')  # File erstellt in der zusätlich gespeichert wird

form = logging.Formatter('%(name)s - %(levelname)s : %(asctime)s - %(message)s')  # zuweisung in welcher form in neuer datei gespeichert werden soll

file.setFormatter(form)

logger.addHandler(file)

logging.info('dies ist eine Info')  # main logger

logger.debug('debugging')

# logging.debug('debugging')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')

# f()
