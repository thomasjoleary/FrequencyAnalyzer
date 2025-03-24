def analyze(inString):
    letarray = [0]*26
    for char in inString:
        if char.isalpha():
            letarray[ord(char.lower()) - ord('a')] += 1
    curletter = 'a'
    for i in letarray:
        print(curletter + ": " + str(i))
        curletter = chr(ord(curletter) + 1)


def OneLineAnalysis():
    inString = input("Enter string for analysis: ")
    analyze(inString)
    

def MultiLineAnalysis():
    inString = open("input.txt", "r").read()
    analyze(inString)

def main():
    print("1. One Line Analysis")
    print("2. Multi Line Analysis")
    choice = int(input("Enter choice: "))
    if choice == 1:
        OneLineAnalysis()
    elif choice == 2:
        if input("Multi Line Analysis selected. Ensure input.txt is prepared. When ready to continue, type 'y'. Otherwise, type anything else.") == 'y':
            MultiLineAnalysis()
    else:
        print("Invalid choice")
        main()

main()