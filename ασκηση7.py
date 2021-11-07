import string
import math
#εισαγωγή κειμένου
with open('test.txt', 'r') as f:
  text = f.read()
  print(text)
#απαλλαγη απο σημεία στιξης και σύμβολα και ένωση του κειμένου
stripped_text = [char.strip(string.punctuation + "“”’ \n") for char in text]
stext = ''.join(stripped_text)
print(stext)
#μετατροπή σε νούμερα ascii
asci_list = [ord(char) for char in stext]
print(asci_list)
len(asci_list)
print(len(asci_list))
#εισοδος σε λίστσ των μονών
oddlist = []
for int in asci_list:
  if (int % 2 != 0):
    oddlist.append(int)
print(oddlist)
#μέτρηση του αριθμού των μονών μέσω λεξικού και εύρεση ποσοστού
counts = dict()
for i in oddlist:
  counts[i] = counts.get(i, 0) + 1
print(counts)
counts.update((x, y * 100 / len(oddlist)) for x, y in counts.items())
print(counts)
print(sum(counts.values()))
print(counts)
#στρογγυλοποίηση και μετατροπή σε αστεράκια
counts.update((x, math.ceil(y)) for x, y in counts.items())
print(counts)
counts = {chr(x): y * "*" for x, y in counts.items()}
print(counts)
for i in counts.keys():
  print(i, counts[i])