initialCapital = 20000
percent = 0.03
maxTimeYears = 10 
i = 0

print("Wpłacono środki w wysokości:", initialCapital,"na:", maxTimeYears, "przy rocznym oprocentowaniu:", percent)
while i <= maxTimeYears:
    odsetki = initialCapital * percent
    print("Po",i,"latach będziesz miał:", odsetki)
    
    finalCapital = ((initialCapital + odsetki) * percent) + initialCapital
    i += 1
    finalCapital *= i

    print(finalCapital, "wynosi")

print("\tzad 2)")

number = 20730906
dig = number
sumdig = 0

while dig > 0:
        last = dig % 10
        sumdig += last
        dig = dig // 10
else:
        print("The sum of digits of: ", number, "is", sumdig)
        
print("\tzad 3)")

txt ="United Space Alliance: This company provides major support to NASA for various projects, such as the space shuttle. One of its projects is to create Workflow Automation System (WAS), an application designed to manage NASA and other third-party projects. The setup uses a central Oracle database as a repository for information. Python was chosen over languages such as Java and C++ because it provides dynamic typing and pseudo-code–like syntax and it has an interpreter. The result is that the application is developed faster, and unit testing each piece is easier"

wordLength = 6
listOfWords = txt.split(" ")
shortWords = 0
longWords = 0
l = 0

print(len(listOfWords))


while l < len(listOfWords):
        if len(listOfWords[l])>wordLength:
                longWords+=1
        else:
                shortWords+=1
        
        l+=1
print("Words shorter than ",wordLength,":",shortWords)
print("Words longer than ",wordLength,":",longWords)    
