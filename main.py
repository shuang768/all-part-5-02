def Q1length():
  userinput=len(input("what is your word?\n"))
  print("the length of your input is",userinput)
def Q2reverse():
  userinput=input("what is your word?\n")
  n=0
  ui=""
  for i in range (0,len(userinput)):
    n=n-1
    ui=ui+userinput[n]
  print("the reverse of your input is",ui)
def Q3wordtriangle():
  userinput=input("what is your word\n")
  n=-1
  k=""
  for i in range(0,len(userinput)):
    n=n+1
    k=k+userinput[n]
    print(k)
task=0
while True:
    try:
      print("which function do you want")
      print("1- Q1length")
      print("2- Q2reverse")
      print("3- Q3wordtriangle")
      print("0- exit")
      task=int(input("enter your function "))

    except ValueError:
        print("Please enter a number")
        continue
      
    else:
      if task==1:
        Q1length()
        break
      elif task==2:
        Q2reverse()
        break
      elif task==3:
         Q3wordtriangle()
         break
      elif task==0:
          print("exit")
          break
      else: 
        print("please enter a valid number")
        continue 