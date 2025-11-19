# Il nostro obiettivo è creare un programma capace di analizzare automaticamente un testo scritto in italiano.
# In particolare il codice individua le parole più significative, eliminando quelle troppo comuni
# come articoli, preposizioni e congiunzioni.
# Successivamente abbiamo inserito anche una serie di associazioni concettuali
# che collegano alcune parole chiave del testo a idee filosofiche.

# Importiamo due librerie fondamentali per il nostro programma:

import string
# Il modulo "string" ci fornisce strumenti per lavorare con testi e caratteri.
# In particolare:
# - string.ascii_letters → tutte le lettere maiuscole e minuscole.
# - string.digits       → tutte le cifre da 0 a 9.
# - string.punctuation  → tutti i simboli di punteggiatura, come ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~
# Nel nostro codice useremo string.punctuation per eliminare tutta la punteggiatura dal testo,
# così da contare solo parole significative senza simboli strani o punti.

from collections import Counter
# Counter è una classe del modulo "collections" che permette di contare rapidamente
# quante volte ogni elemento compare in una lista o collezione.
# Ad esempio, se abbiamo una lista di parole, Counter ci dirà quante volte compare ciascuna parola,
# senza bisogno di scrivere cicli e contatori manuali.
# Questo ci servirà per trovare facilmente le parole più frequenti nel testo che stiamo analizzando.


# In questa parte creiamo la lista delle "stopwords".
# Le stopwords sono parole molto frequenti nella lingua italiana che però non portano
# un significato reale all’interno del testo, come articoli (il, la), preposizioni (di, a),
# congiunzioni (e, o) ecc.
# Eliminandole otterremo un’analisi più accurata e centrata sulle parole importanti.
stopwords = ['il', 'la', 'lo', 'i', 'gli', 'è', 'si', 'le', 'un', 'una', 'uno','di', 'a', 'da', 'in', 'con', 'su', 'per', 'tra', 'fra', 'e', 'o','ma', 'che', 'non', 'più', 'come', 'anche', 'se']

# A questo punto il programma deve leggere il contenuto del file di testo che vogliamo analizzare.
# Usiamo "with open(...)" perché permette di aprire e chiudere automaticamente il file
# senza rischio di errori.
# la "r" è la modalità di apertura (r = read, cioè lettura)
# L’encoding "utf-8" è necessario per leggere correttamente lettere accentate e simboli speciali.
with open("testo_meraviglia.txt", "r", encoding="utf-8") as file:
    testo = file.read()

# Ora comincia la fase di pulizia del testo.
# Il primo passo è trasformare tutto il testo in minuscolo: in questo modo "Sapere" e "sapere"
# saranno riconosciute come la stessa parola, evitando doppioni nel conteggio.
testo_pulito = testo.lower()

# Il secondo passaggio è eliminare completamente la punteggiatura dal testo.
# Per farlo analizziamo uno a uno i simboli contenuti in "string.punctuation"
# e li sostituiamo con una stringa vuota, così il testo rimane composto solo da parole.
for carattere in string.punctuation:
    testo_pulito = testo_pulito.replace(carattere, '')

# Con il testo ormai pulito possiamo estrarre tutte le parole significative.
#questa qui sotto e una list comprehension (e un modo rapido per scrivere le liste) e fa queste cose:
#testo_pulito.split() → divide il testo in una lista di parole.
#for parola in testo_pulito.split() → scorre ogni parola della lista.
#if parola not in stopwords → filtra le parole, tenendo solo quelle che NON sono nelle stopwords.
#[parola ...] → costruisce una nuova lista con le parole filtrate.
#Alla fine, parole conterrà solo le parole significative, senza articoli, preposizioni ecc.
#potrei fare anche senza list comprehinsion con il for cosi:
#parole = []
#for parola in testo_pulito.split():
#    if parola not in stopwords:
#       parole.append(parola)
parole = [parola for parola in testo_pulito.split() if parola not in stopwords]

# Ora utilizziamo "Counter" per contare automaticamente quante volte appare ogni parola.
# Il risultato è simile a un dizionario: ad ogni parola viene associato il numero delle sue occorrenze.
conteggio = Counter(parole)

# Il passo successivo è trovare le 5 parole più frequenti del testo.
# "conteggio" è un oggetto di tipo Counter, cioè un dizionario speciale che tiene conto di quante volte
# ogni parola appare nel testo.
# Il metodo most_common(n) restituisce una lista ordinata di tuple (parola, frequenza), 
# partendo dalla parola più frequente.
# Qui passiamo 5 come argomento, quindi otteniamo le 5 parole più usate.
top_5 = conteggio.most_common(5)


# Stampiamo le 5 parole più usate, una per riga, insieme al numero di volte in cui compaiono.
print("Le 5 parole più frequenti:")
for parola, frequenza in top_5:
    print(f"- {parola}: {frequenza}")


# Si tratta di un semplice dizionario che associa parole rilevanti a concetti filosofici collegati,
# permettendo una lettura più profonda e interpretativa del testo.
concetti = {'filosofia': 'conoscenza','meraviglia': 'origine','sapere': 'epistemologia','desiderio': 'motivazione','conoscenza': 'fine in sé'}

# Infine stampiamo tutte le associazioni concettuali in formato chiaro.
print("\nAssociazioni concettuali:")
for parola, concetto in concetti.items():
    print(f"- {parola} → {concetto}")


