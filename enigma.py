
w1=[4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]

w2=[0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]

w3=[1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]

w4=[4, 18, 14, 21, 15, 25, 9, 0, 24, 16, 20, 8, 17, 7, 23, 11, 13, 5, 19, 6, 10, 3, 2, 12, 22, 1]

reflec=[24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]

def shift(seq, n, rn, numb):
    if rn==1:
        n= -n%len(seq)

    elif rn==2:
        n= -int(n/25)%len(seq)
        
    elif rn==3:
        n= -int(n/675)%len(seq)

    elif rn==4:
        n= -int(n/17575)%len(seq)
       
    return seq[n:]+seq[:n]

def set(seq,st):
    return shift(seq,st)

def rotorrev(seq):
    rotorrev=[0]*26
    for i in range(26):
        rotorrev[seq[i]]=i
    
    return rotorrev

def forward(seq,n,rn):
    numb=[]
    for i in range(len(n)):
        rot=shift(seq,i,rn,n)
        numb.append(rot[n[i]])

    return numb

def backward(seq,n,rn):
    numb=[]
    for i in range(len(n)):
        rotation=shift(seq, i, rn, n)
        seqrev=rotorrev(rotation)
        numb.append(seqrev[n[i]])

    return numb

def reflector(seq,n):
    ref=[]
    for i in range(len(n)):
        ref.append(seq[n[i]])
        
    return ref


def encrypt(numb,wh1=w1,wh2=w2,wh3=w3,wh4=w4,ref=reflec):
    w1s=forward(wh1,numb,1)
    w2s=forward(wh2,w1s,2)
    w3s=forward(wh3,w2s,3)
    w4s=forward(wh4,w3s,4)
    refs=reflector(ref,w4s)
    w4s=backward(wh4,refs,4)
    w3s=backward(wh3,w4s,3)
    w2s=backward(wh2,w3s,2)
    w1s=backward(wh1,w2s,1)
    
    return w1s

while True:
    msg=input('Enter the message you want to encrypt > ')
    if msg=='':
        break
    msg=msg.upper()
    numb=[(ord(i)-65) for i in msg if i!=' ']
    print('Encrypted message is ',''.join([(chr(i+65)) for i in encrypt(numb)]))

