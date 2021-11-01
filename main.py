minNumber = int(input("Lütfen minimum sayı giriniz."))
maxNumber = int(input("Lütfen maximum sayı giriniz."))
numberDivided = int(input("Lütfen bölüm için sayı giriniz."))

def bolum(minNumber, maxNumber, numberDivided):
    allNumber = list(range(minNumber, maxNumber +1))

    fullyDividedNumbers = []

    j = 0

    for element in allNumber:
        if (allNumber[j] % numberDivided == 0): #Zero control
            fullyDividedNumbers.append(allNumber[j])
        j += 1
    return fullyDividedNumbers

latestSituation = bolum(minNumber, maxNumber, numberDivided)
print(latestSituation)
