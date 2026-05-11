import tkinter as tk
import random

guessnum = 0


def getWord():
  guessedWord = EntryBox.get()
  global guessnum
  cnt = 0
  if guessedWord in wordlist:
    # A valid word entered .
    for kk in range(5):
      label = tk.Label(text=guessedWord[kk].upper(),
                       pady=5,
                       font=12,
                       borderwidth=1,
                       relief='solid')
      label.grid(row=guessnum, column=kk, sticky=tk.NSEW)

      if guessedWord[kk] in chosenWord:
        if guessedWord[kk] == chosenWord[kk]:
          label.config(bg='green')
          label.config(fg='white')
        else:
          label.config(bg='gold')
          label.config(fg='white')
          print('kk = ', kk, ' yellow found ', 'cnt =', cnt)
          if cnt < guessedWord.count(guessedWord[kk]) - chosenWord.count(
              guessedWord[kk]):
            label.config(bg='grey')
            label.config(fg='white')
            cnt = cnt + 1

      else:
        label.config(bg='grey')
        label.config(fg='white')

  else:
    print('Invalid word, please enter again.')

  guessnum = guessnum + 1


#f = open('Five_letterwords_new.txt')
#words = f.read()
#f.close()

with open('Five_letterwords_new.txt') as file:
  words = file.read()

wordlist = words.split('\n')

chosenWord = random.choice(wordlist)
# chosenWord = 'first'

window = tk.Tk()
window.title("Wordle")
window.geometry("300x300")

#if guessedWord[kk] in chosenWord:
#  pass
#else:
#  label.config(bg = 'grey')
#  label.config(fg = 'white')

#hello = tk.Label(text="Hello world!")
#hello.pack()
#button = tk.Button(text="Click me!")
#button.pack()

EntryBox = tk.Entry()
EntryBox.grid(row=99, column=0, columnspan=5)
GuessButton = tk.Button(text="Guess", command=getWord)
GuessButton.grid(row=100, column=0, columnspan=5)

tk.mainloop()
