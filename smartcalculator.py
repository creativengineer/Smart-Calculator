from tkinter import *

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

def lcm(a,b):
    L = a if a>b else b
    while L<= a*b:
        if L%a==0 and L%b == 0:
            return L
        L+=1

def hcf(a,b):
    H = a if a<b else b
    while H >=1:
        if a%H==0 and b%H== 0 :
            return H
        H-=1

def extract_from_text(text):
    l= []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

def calculate():
    text= textin.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extract_from_text(text)
                r=operations[word.upper()](l[0], l[1])
                list.delete(0,END)
                list.insert(END,r)
            except:
                list.delete(0,END)
                list.insert(END,'Something went wrong please enter again!')
            finally:
                break
        elif word.upper() not in operations.keys():
            list.delete(0,END)
            list.insert(END,'This operation is not Defined!')

operations = {'ADD':add , 'ADDITION': add, 'SUM':add , 'PLUS': add,
                'SUB':sub,'DIFFERENCE':sub,'MINUS':sub , 'SUBTRACT':sub,
                 'LCM':lcm , 'HCF':hcf , 'PRODUCT':mul , 'MULTIPLICATION':mul,
                 'MULTIPLY':mul , 'DIVISION':div , 'DIV':div ,'DIVIDE':div,
                 'MOD':mod ,'REMAINDER':mod , 'MODULUS':mod}

win=Tk()
win.geometry('350x400')
win.title('Smart Calculator')
win.configure(bg='#B0E0E6')

l1=Label(win, text='I am a Smart Calculator',bg='#FFEFDB',font="Times 20 bold",cursor='heart',width=25,padx=2)
l1.place(x=50,y=20)

l2=Label(win, text='My Name is TEXT-TO-CALCULATE',bg='#FFEFDB',font="Times 15",cursor='star',width=30,padx=2)
l2.place(x=55,y=65)

l2=Label(win, text='What can i help you',bg='#FFEFDB',font="Times 10",cursor='dotbox',width=20,padx=2)
l2.place(x=105,y=140)

textin = StringVar()
e1=Entry(win, width=22 , textvariable = textin)
e1.place(x=75,y=180)

b1=Button(win, text='Just This',fg='blue',font='Times 20 bold',activeforeground='red',command=calculate)
b1.place(x=120,y=230)

list=Listbox(win,width=30,height=3)
list.place(x=35,y=280)
win.mainloop()
