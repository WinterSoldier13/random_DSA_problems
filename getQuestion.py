#!/usr/bin/env python3
import pandas as pd 
import random

# Read the file
df = pd.read_csv('./questions.csv')
l = len(df['status'])

def getRandom():
    index = random.randint(0, l)

    if(df['link'][index] == "NaN" or df['status'][index] == 'Y'):
        return getRandom()
    return index

def getInfo(index : int):
    problemName = df['problem'][index]
    problemLink = df['link'][index]

    if(problemName == ""):
        main()

    print(str("|PROBLEM STATEMENT|\n"+problemName+"\n\n"+ "|LINK|\n"+problemLink))

def updateStatus(index : int):
    global df

    inp = input("\nEnter Y after you solve this question, else press N to get a new one: ")

    if(inp == "N" or inp=="no" or inp=="NO"):
        main()
    else:
        df2 = df
        # Not the right way.... anyways
        try:
            df2['status'][index] = 'Y'
            df2.to_csv("./questions.csv")
        except:
            "Error"        
    print("\n\n\nEnter C to get a new question else press CTRL+C to exit")

    inp = input()
    if(inp == "C" or inp=='c'):
        main()
    else:
        exit()


def main():
    global df, l

    df = pd.read_csv('./questions.csv')
    l = len(df['status'])

    print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
    print("Fetching a question...")

    index = getRandom()

    print(index)
    getInfo(index= index)
    updateStatus(index)




    

if __name__ == "__main__":
    try:
        main()
    except:
        print("\n\nEXIT")
        
   
