#The rotor setting[It is original one's]
I = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]

II = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]

III = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]

IV = [4, 18, 14, 21, 15, 25, 9, 0, 24, 16, 20, 8, 17, 7, 23, 11, 13, 5, 19, 6, 10, 3, 2, 12, 22, 1]

V = [21, 25, 1, 17, 6, 8, 19, 24, 20, 15, 18, 3, 13, 7, 11, 23, 0, 22, 12, 9, 16, 14, 5, 4, 2, 10]

VI = [9, 15, 6, 21, 14, 20, 12, 5, 24, 16, 1, 4, 13, 7, 25, 17, 3, 10, 0, 18, 23, 11, 8, 2, 19, 22]

VII = [13, 25, 9, 7, 6, 17, 2, 23, 12, 24, 18, 22, 1, 14, 20, 5, 0, 8, 21, 11, 15, 4, 10, 16, 3, 19]

VIII = [5, 10, 16, 7, 19, 11, 23, 14, 2, 1, 9, 18, 15, 3, 25, 17, 0, 12, 4, 22, 13, 8, 20, 24, 6, 21]

#The reflector setting the original ones
RI = [4, 9, 12, 25, 0, 11, 24, 23, 21, 1, 22, 5, 2, 17, 16, 20, 14, 13, 19, 18, 15, 8, 10, 7, 6, 3]

RII=[24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]

RIII=[5, 21, 15, 9, 8, 0, 14, 24, 4, 3, 17, 25, 23, 22, 6, 2, 19, 10, 20, 16, 18, 1, 13, 12, 7, 11]

RIV=[4, 13, 10, 16, 0, 20, 24, 22, 9, 8, 2, 14, 15, 1, 11, 12, 3, 23, 25, 21, 5, 19, 7, 17, 6, 18]

RV=[17, 3, 14, 1, 9, 13, 19, 10, 21, 4, 7, 12, 11, 5, 2, 22, 25, 0, 23, 6, 24, 8, 15, 18, 20, 16]

def shift(seq, n, rn):
    '''
shifts the rotor in every keypress [if called]
seq --> the sequence which the rotor has
n --> the rotation the sequence has gone through
rn --> rotor number
returns: the shifted sequence
    '''
    if rn == 1:
        n = -n%len(seq)

    elif rn == 2:
        n = -int(n/25)%len(seq)
        
    elif rn == 3:
        n = -int(n/675)%len(seq)

    elif rn==4:
        n = -int(n/17575)%len(seq)
       
    return seq[n:]+seq[:n]

def set(seq,st):
    '''
incomplete
    '''
    return shift(seq,st)

def rotorrev(seq):
    '''
seq -->which is to reversed
returns: reversed list in which output<->input got interchanged
    '''
    rotorrev = [0]*26
    for i in range(26):
        rotorrev[seq[i]] = i
    
    return rotorrev

def forward(seq,n,rn):
    '''
seq --> the sequence which the rotor has
n --> the character sequence or message sequence
rn --> rotor number
returns: forward cipher or the value[in the list] it aquired in moving forward
    '''
    numb = []
    for i,v in enumerate(n):
        rot = shift(seq,i,rn)
        numb.append(rot[v])

    return numb

def backward(seq,n,rn):
    '''
seq --> the sequence which the rotor has
n --> the character sequence or message sequence
rn --> rotor number
returns: backward cipher or the value[in the list] it aquired in moving backward
    '''
    numb = []
    for i,v in enumerate(n):
        rotation = shift(seq, i, rn)
        seqrev = rotorrev(rotation)
        numb.append(seqrev[v])

    return numb

def reflector(seq,n):
    '''
seq --> the sequence which the reflector has
n --> the character sequence or message sequence
    '''      
    return [seq[i] for i in n]


def encrypt(numb,wh1=I,wh2=II,wh3=III,wh4=IV,ref=RI):
    w1s = forward(wh1,numb,1)
    w2s = forward(wh2,w1s,2)
    w3s = forward(wh3,w2s,3)
    w4s = forward(wh4,w3s,4)
    refs = reflector(ref,w4s)
    w4s = backward(wh4,refs,4)
    w3s = backward(wh3,w4s,3)
    w2s = backward(wh2,w3s,2)
    w1s = backward(wh1,w2s,1)
    
    return w1s

while True:
    msg = input('Enter the message you want to encrypt > ')
    if msg == '':
        break
    msg = msg.upper()
    numb = [(ord(i)-65) for i in msg if i != ' ']
    print('Encrypted message is ',''.join([(chr(i+65)) for i in encrypt(numb)]))

