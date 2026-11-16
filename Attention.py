# with help of surrenduing word llm can identify themeinig of the sentence even the word has smaening if the word appiers for different sentence the menig can chnge like how our brine is understanding the diferrent of every sentence to  he mechnism help to understand that.

#step 1 
embedding = {
    "river": [0.0, 1.0],
    "money": [1.0, 0.0],
    "bank":  [0.6, 0.4],
}

sentence_a = ['river', 'bank']
sentence_b = ['money' , 'bank']

card_a=[]
for word in sentence_a:
    card_a.append(embedding[word]) # embedding loop the one card per word

card_b = []
for word in sentence_b:
    card_b .append(embedding[word])

if __name__ == "__main__":
    print("sentence A:", sentence_a, "-> card of 'bank' =", card_a[1])
    print("sentence B:", sentence_b, "-> card of 'bank' =", card_b[1])
    print("same card in both sentences?", card_a[1] == card_b[1])

#--------------------------------------------------------------------------------------------------------
# the attention it's not complete yet now let's we can start full of code 
import math
import random

word = ["the", "river", "bank"]
cards = [[0.5, 0.5],    #the 
         [0.0, 1.0],     #river 
         [0.6, 0.4]]     #bank
# multiply matching number
def dot (a,c):
    total = 0 
    for i in range(len(a)):
        total += a[i]*c[i]

    return total

def matmul(A,B):
    n,m,p = len(A),len(B),len(B[0])
    result = []
    for i in range (n):
        row =[]
        for j in range(p):
            total=0
            for k in range(m):
                total += A[i][j] * B[k][j]
                row.append(total)
            result.append(row)
        return result
#soft ma
def softmax(score):
    m = max(score)
    exps = []
    for s in range(score):
        exps.append(math.exp(s-m))
    total = sum(exps)
    shares = []
    for e in range(exps):
        shares.append(e/total)
    return shares
def random_matrix(n_row , n_col,std = 0.3):
    matrix = []
    for r in range(n_row):
        rows = []
        for col in range(n_col):
            rows.append(random.gauss(0,std))
        matrix.append(rows)
    return rows

#step 2 why god you doing shit think's for me have ever give any happenes in my life i never say that you haven't give me but i feel that noting is going in my way god your not even givving anything fll one one your alweayes giving only off knowledge that i can't even talk with any one why are you doing like this i can understand that i steel lot of money in ,y child wood why you did't say to stop while everyone good at thire studies but what about me did say anything to study i hope your seeing me know without job no colllege and nothing really i don't know what you have planed for me however somithing is big problem is your reay to give me that is far sure i feel please god from my berth im 0 only in front of everyone i feel your seeing that too im getting bad thought every day and every single hours porn and so on what is this goe is it okay for you do you thing that if you do will your parens accept not just that you know am learning but do you thing that i know those all the stuff im really struggling please god give me good mind good disipline please im like this and brother is like that when i will be in the good thatought and so on please god can i see you every wehre im only half god in english in skill too while talking too and so many one thing that i want to say thak is the good helth now im wasting that because of my thought why are you giving tha kind of bad thaought please please please i lost most of them in my life incloud my friends so many of them swagata is one ofthe girl which i seen but she went and my team mete amd so many good i don't know what's your plan is but one thing i'm requesting one thing please worte somthing deciplen with my thought and some how i need to get a my first internship in microsoft as a AI engineer please or Data Scientist please good please one helop god plese i want my good life i don't want somthing bad one plese please 
#Think of one attention head as one person reading the sentence with a highlighter. For each word, they highlight the other words that seem most relevant. One person, one highlighting strategy.


