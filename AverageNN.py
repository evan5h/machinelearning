from tkinter import *
import numpy as np
from math import e

def forwardPass(i1, i2, w1, w2):
    actual = i1 * w1 + i2 * w2
    return (actual)

def clicked():
    global w1, w2, input1, input2, ideal, actual, Iterations
    input1 = np.random.randint(0, 100)
    input2 = np.random.randint(0, 100)
    actual = forwardPass(input1, input2, w1, w2)
    for i in range(0, int(txt.get())): 
        input1 = np.random.randint(0, 5)
        input2 = np.random.randint(0, 5)
        #print(input1)
        #print(input2)
        ideal = (input1+input2)/2
        actual = forwardPass(input1, input2, w1, w2)
        newWeights = backpropogate(input1, input2, w1, w2, actual, ideal, 0.02)
        w1 = newWeights[0]
        w2 = newWeights[1]
        Iterations += 1
        iteration.config(text="Iteration: " + str(Iterations))
        weight1.config(text="Weight 1: " + str(round(w1, 2)))
        weight2.config(text="Weight 2: " + str(round(w2, 2)))
        costt.config(text="Cost: " + str(round(cost(actual, ideal), 8)))
        num1.config(text="Input 1: " + str(round(input1, 2)))
        num2.config(text="Input 2: " + str(round(input2, 2)))
        guesss.config(text="Guessed average: " + str(round(actual, 2)))
        
    print ("Cost After: " + str(cost(forwardPass(input1, input2, w1, w2), ideal)))
    print (str(w1) + " " + str(w2))
    print ("The estimated average of " + str(input1) + " and " + str(input2) + " is " + str(actual))
    print (Iterations)

def cost(actual, ideal):
    cost = (ideal-actual)**2
    return cost

def backpropogate(i1, i2, w1, w2, actual, ideal, stepsize):
    n = stepsize
    w1_gradient = (actual-ideal) * 2 * i1
    w2_gradient = (actual-ideal) * 2 * i2
    return([w1-w1_gradient*n, w2-w2_gradient*n])


#while cost(actual, ideal)>0.01


if __name__ == "__main__":
    global w1, w2, input1, input2, ideal, actual, Iterations
    input1 = np.random.randint(0, 100)
    input2 = np.random.randint(0, 100)
    w1, w2 = (np.random.uniform(0,1), np.random.uniform(0,1))
    print (input1)
    print (input2)
    print (("Weights: %f %f") % (w1, w2))
    ideal = (input1+input2)/2
    print("ideal: " + str(ideal))
    actual = forwardPass(input1, input2, w1, w2)
    print(actual)
    print(cost(actual, ideal))
    newWeights = backpropogate(input1, input2, w1, w2, actual, ideal, 0.02)
    w1 = newWeights[0]
    w2 = newWeights[1]
    print (("Weights: %f %f") % (w1, w2))
    
    Iterations = 0
    
    window = Tk()
    lbl = Label(window, text="How many iterations to train: ")
    iteration = Label(window, text="Iteration: " + str(Iterations))
    weight1 = Label(window, text="Weight 1: " + str(round(w1, 2)))
    weight2 = Label(window, text="Weight 2: " + str(round(w2, 2)))
    num1 = Label(window, text="Input 1: " + str(round(input1, 2)))
    num2 = Label(window, text="Input 2: " + str(round(input2, 2)))
    costt = Label(window, text="Cost: " + str(round(cost(actual, ideal), 8)))
    guesss = Label(window, text="Guessed average: " + str(round(actual, 2)))
    txt = Entry(window,width=10)
    window.title("Averager")
    
    txt.insert(END, 1)
    btn = Button(window, text="Train", command=clicked)
    
    lbl.grid(column=1, row=1)
    txt.grid(column=2, row=1)
    btn.grid(column=3, row=1)
    iteration.grid(column=1, row=2)
    weight1.grid(column=2, row=2)
    weight2.grid(column=3, row=2)
    costt.grid(column=2, row=4)
    num1.grid(column=1, row=3)
    num2.grid(column=2, row=3)
    guesss.grid(column=1, row=4)
    
    window.geometry('450x100')
    window.mainloop()
    
    






























