DNA = "ACTGTGCTGACTCCCGGTGCTGCCGCTGCCATAGCTAAAGCCCGGGTCCTGGTAGGCAGGCGGGAAGCAGGGTGGGGGTCCCGGGTACTGGTAGGGGTAGCCCTGACCCAGAGGCGGGGGGGCAGCCGGGTGGGGCAGCGGGGCCAGCGTGTCCTGAA-CGAAGTCCCACTGGAGCCACTGTTGAGGTTCAGGGTGGCGAGATCTGGCGGNNNAGGGTAGGTGAGGGCCGCGGAGGGGCCTCCGGCGTTCCCCTCCCCCCCGCCCTGAAACCCGAAGCCCCCACTCACTGCTGCAGAGATCCCCTGAAAACGTAGTAGCACTGCTCgagacAGGTGATCTGTTGACCTGAAACCGCAGGAAGCCGTGCTTCAGCAAGCTGCTGGCGTACTTCCGGGCCT---GCCGCTCCTTGAAGCCCTCCACGTGTGTGTACAGCCAGTCCACCACGTCCGCCCCTGGCCGGCACCAGCGGTCAGCCCGCAGCCTCGAGGCAAGCAGCCCTGCCNNTGGCACTATCCGC-CGCGGGGACGGCCACTCACCGATGACGGCATNNGCGATGGTGATCTTGAGCCACATGCGGTCGCGGATCTCCAGTCCCGAG---GGCAGCTGCATGACCCGGACGACGGCGCTCATGTCACtcaccgtcagcggcgcctcttccagCCAGCTCTGCAAAGCACAGACAGCCCCGCTTCGCCCCAGCATCTGAAAGCGGGGGACTCggcAcgCTGCACCCCCAGGGGAGCCTCTGGGCAGAGCCTGCGCCAGGGCGCAAGCTGGACGGTGCGTGACAGCAGGGCCCCGGCCCACTGCAGGATGCACCCCCGTGAGGCTGGGGCGTGAGCAGGGGGGTTGGACAtttAGTCTCCCACTTCTACAGACACTTTTCATCAGGATCCTAGGCACAAACTGGGCTGAAACCCCACCCTGCAGACCAGGAAGTAATGAGAACAGGGCAGGCCCCTTCCCCTCNNCGCATGCC-CACCCGAGAGCGCAGGCTGTTAGTCGTGTTAATGGCAGGAAGCAGAATGGAGACCTGGCCCCTGCCTCTGAA-CCGTGGGTGCTCaactggctaGCCCTACGTACATCCCCTGTTCcggCCAACACACAGACATGAGCAGGATGGGCTGCACAAGGTGGGCACGGGTGCCTGTGCACACGTCTGTGCAGGGAGTTGGGGACAGGCAACACACACGTGTCACAGCCCCATGACGGggcaattgcGCCATGCTGGCTGAATGGCAGAGACGCCCCTCCAAGCCTCGGTTTCTGCTGGGGCCCTCAGGAGCTGCCACTTACGTGGAGCACCAGGCACGGAGCTGGTTAGTGAGGAGGAGCTGGTGCGCGTGACGGCGCTGGAGCAGGGACTCGTACCGTAGCGGGGCAGGGCNNNTGTCAGTGCCGCCGTGTGGtcagcggcgatCGGCG-GGTCGATGGGCCGCACCGGGTCAGCTGGGTGNAGACACGTGGCGATGACAGGCGGACAGATGGACAGGGTGGGAGGGCAGGGTGCAGGGCACAGAGGAGAGAGGCCTTCAGGCTAGGTAGGCGCCCCCTCCCCATCCCGccccGTGTGCCCCGAGGGCCACTCACCCCGTGGGACGGTGAAGTAGCTTCG-GGCGTTGGGTCCAGCACTTGGCCACAGTGAGGCTGNAAATGGCTGCAGGAACGGTGGTCCCCCCGCAAGGCCCCCATGGTCCCACCTCCCTGCCTGGCCCCTCCCGCTCCAGCGCCNCCAGCC"

print("Czy DNA zawiera tylko wielkie litery?: ", DNA.isupper())
print("Czy DNA zawiera tylko litery?: ", DNA.isalpha())
print("Czy DNA zawiera puste przestrzenie?: ", DNA.isspace())
print("Ilość '-' w DNA: ", DNA.count("-"))
smalla = DNA.count("a")
biga = DNA.count("A")
print("Ilość Adeniny w DNA: ", smalla + biga)
smallc = DNA.count("c")
bigc = DNA.count("C")
print("Ilość Cytozyny w DNA: ", smallc + bigc)
smallg = DNA.count("g")
bigg = DNA.count("G")
print("Ilość Guaniny w DNA: ", smallg + bigg)
smallt = DNA.count("t")
bigt = DNA.count("T")
print("Ilość Cytozyny w DNA: ", smallt + bigt)
print("Ilość występienia GAGA: ", DNA.count("GAGA"))
DNA1 = DNA.replace("GAGA", "AGAG")
print("Zamieniam wszystkie GAGA na AGAG")
print("Ilość występienia GAGA: ", DNA1.count("GAGA"))
DNA2 = DNA1.replace("GAGA", "AGAG")
print("Ilość występienia GAGA: ", DNA2.count("GAGA"))
print("GGGGGGG występuję na pozycji: ", DNA2.index("GGGGGGG"))
print("CCCCCC od końca łańcucha występuje na pozycji: ", DNA2.rindex("CCCCCC"))
print("Sekwencja CTGAAA pojawiła się w DNA: ", DNA2.count("CTGAAA"), " razy.")
print("Sekwencja CTGAAAA, która czasem mutuje, pojawiła się w DNA: ", DNA2.count("CTGAAAA"), " razy.")
RNA = DNA2.replace("T", "U")
RNA1 = DNA2.replace("-", "")
print("Prawidłowe RNA: ", RNA1.upper())
