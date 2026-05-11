# Initial Intro

print("So you want to meet the Prof ???")
print("I am his assistant")
print("First you have to pass this quiz")
print(); 



#answer = input("Tell a word\n")
#print(answer, 'apple', sep='')
#print(answer.strip(), 'apple', sep='')


answer = input("ok, tell me what action words are called in English?\n")

# Notice the use of lower()

if answer.lower() == "verbs":
    print("Correct, but that was only a warm up ...")
else:
    print("Grrr ... your chances of meeting the Prof. are very low")  
print()

answer = input("Give me an 8 letter English word with at least 3 vowels\n")
if len(answer) == 8:
    print("Your word has 8 letters ...")
    count_a = answer.count('a')
    count_e = answer.count('e')
    count_i = answer.count('i')
    count_o = answer.count('o')
    count_u = answer.count('u')
    
    count_vowels = count_a+count_e+count_i+count_o+count_u 
    if count_vowels > 3:
        print("Oof ... you gave me more than 3 vowels")
        print("You are wasting my time, I needed only 3.")
    elif count_vowels < 3:
        print("that had less than 3 vowels")
        print("You tried to act smart, but I caught you.")
    else:
        print("What ... exactly 3 vowels ...")
        print("You are not motivated, you are not putting any extra effort")
else:
    print("You seem to be a disaster.")
    print("That word did not even have 8 letters.")

print()
sentence = input("ok, tell me a sentence ending in 'wise assistant' (no question please)\n")
# print(sentence.endswith('wise assistant.'))
if sentence.endswith('wise assistant'):
    print("Haven't you learnt about punctuations?")
elif sentence.endswith('wise assistant.'):
    len_first = sentence.find(' ')
    if len_first < 5:
        print("The first word in the sentence is too short.")
else:
    print("I really think you will make the prof. furious.")

print()   
print("Ok, pick your preferred appointment time for next Monday(A/B/C/D)")
print("A. 8 mins past midnight", "B. 16 mins before sunrise", sep='\t'); 
print("C. 24 mins before noon", "D. 48 mins after sunset", sep='\t');
appointment = input('Select your slot (A/B/C/D)\n')

if appointment == 'A':
    print("Careful, Prof may be sleepy.")
elif appointment == 'B':
    print("Warning, Prof. may be jogging.")
elif appointment == 'C':
    print("Beware, Prof. may be hungry.")
else:
    print("Caution, Prof. may be tired.")

print()
print("Good luck for your appointment, bye for now!")




          




