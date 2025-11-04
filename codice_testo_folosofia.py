import re
form collections import counter
stopwords=['il','la','lo','i','gli','le','un','una','uno','di','a','da','in','con','su','per','tra','fra','e','o','ma','che','non','più','come','anche','se']
with open("testo_meraviglia.txt","r",encodig="utf-8") as file:
    testo=file.read()
testo_pulito=testo.lower().traslate(str.maketrans('', '',string.punctuation))
parole=[parole for parola in testo_pulito.split() if parola not in stopwords]
io = Counter(paorle)
conteggio.most_common(5)
print("le 5 parole più frequenti: ")
for parola, ferequanza in top_5:
    print(f"-{parola}: {frequenza})
concetti = {
    
