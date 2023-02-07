# making keys
binaryKey = 0b1010_0111_0011_1011 #set1
plaintext = 0b0110_1111_0110_1011 #set1
#binaryKey = 0b0100_1010_1111_0101 #set2
#plaintext = 0b1101_0111_0010_1000 #set2
#binaryKey = 0b1010_0111_0011_1011 #set3
#plaintext = 0b0110_1111_0110_1011 #set3

sBox = {0: 9, 1: 4, 2: 10, 3: 11, 4: 13, 5: 1, 6: 8, 7: 5, 8: 6, 9: 2, 10: 0, 11: 3, 12: 12, 13: 14, 14: 15, 15: 7}


def subNib(splittedKey):
    frontKey = (splittedKey & 0b1111) << 4
    backKey = (splittedKey & 0b1111_0000) >> 4
    return frontKey + backKey


def rotNib(splittedKey):
    frontKey = (sBox[splittedKey >> 4] << 4)
    backKey = (sBox[splittedKey & 0b1111])
    return frontKey + backKey


w0 = binaryKey >> 8
w1 = binaryKey & 0b11111111
w2 = w0 ^ 0b1000_0000 ^ subNib(rotNib(w1))
w3 = w2 ^ w1
w4 = w2 ^ 0b0011_0000 ^ subNib(rotNib(w3))
w5 = w4 ^ w3

key0 = (w0 << 8) + w1
key1 = (w2 << 8) + w3
key2 = (w4 << 8) + w5

# encryption

def nibbleRound1(binaryCode):
    # nibble substitution(S-boxes)
    binCode0 = sBox[binaryCode & 0b1111]
    binCode1 = sBox[(binaryCode & 0b1111_0000) >> 4]
    binCode2 = sBox[(binaryCode & 0b1111_0000_0000) >> 8]
    binCode3 = sBox[(binaryCode & 0b1111_0000_0000_0000) >> 12]

    substitutedCode = (binCode3 << 12) + (binCode0 << 8) + (binCode1 << 4) + (binCode2)

    # mix columns. using GF
    b0 = (substitutedCode & 0b1000_0000_0000_0000)>>15
    b1 = (substitutedCode & 0b100_0000_0000_0000)>>14
    b2 = (substitutedCode & 0b10_0000_0000_0000)>>13
    b3 = (substitutedCode & 0b1_0000_0000_0000)>>12
    b4 = (substitutedCode & 0b1000_0000_0000)>>11
    b5 = (substitutedCode & 0b100_0000_0000)>>10
    b6 = (substitutedCode & 0b10_0000_0000)>>9
    b7 = (substitutedCode & 0b1_0000_0000)>>8
    c0 = (substitutedCode & 0b1000_0000)>>7
    c1 = (substitutedCode & 0b100_0000)>>6
    c2 = (substitutedCode & 0b10_0000)>>5
    c3 = (substitutedCode & 0b1_0000)>>4
    c4 = (substitutedCode & 0b1000)>>3
    c5 = (substitutedCode & 0b100)>>2
    c6 = (substitutedCode & 0b10)>>1
    c7 = (substitutedCode & 0b1)

    nb0 = (b0^b6)<<15
    nb1 = (b1^b4^b7)<<14
    nb2 = (b2^b4^b5)<<13
    nb3 = (b3^b5)<<12
    nb4 = (b2^b4)<<11
    nb5 = (b0^b3^b5)<<10
    nb6 = (b0^b1^b6)<<9
    nb7 = (b1^b7)<<8
    nc0 = (c0^c6)<<7
    nc1 = (c1^c4^c7)<<6
    nc2 = (c2^c4^c5)<<5
    nc3 = (c3^c5)<<4
    nc4 = (c2^c4)<<3
    nc5 = (c0^c3^c5)<<2
    nc6 = (c0^c1^c6)<<1
    nc7 = (c1^c7)

    mixedColumnsCode = nb0+nb1+nb2+nb3+nb4+nb5+nb6+nb7+nc0+nc1+nc2+nc3+nc4+nc5+nc6+nc7

    return mixedColumnsCode

def nibbleRound2(binaryCode):
    # nibble substitution(S-boxes)
    binCode0 = sBox[binaryCode & 0b1111]
    binCode1 = sBox[(binaryCode & 0b1111_0000) >> 4]
    binCode2 = sBox[(binaryCode & 0b1111_0000_0000) >> 8]
    binCode3 = sBox[(binaryCode & 0b1111_0000_0000_0000) >> 12]

    substitutedCode = (binCode3 << 12) + (binCode0 << 8) + (binCode1 << 4) + (binCode2)

    return substitutedCode

# add round0 key
round0 = plaintext ^ key0
#round1
round1 = nibbleRound1(round0) ^ key1
#round2
round2 = nibbleRound2(round1) ^ key2

binaryPlaintext = format(plaintext,'b').zfill(16)
binaryCiphertext = format(round2, 'b').zfill(16)
print("Encryption of %s is %s" %(binaryPlaintext, binaryCiphertext))

########################################################################################################################

#decryption
sBoxInversed = {9: 0, 4: 1, 10: 2, 11: 3, 13: 4, 1: 5, 8: 6, 5: 7, 6: 8, 2: 9, 0: 10, 3: 11, 12: 12, 14: 13, 15: 14, 7: 15}

def nibbleDecryptRound2(binaryCode):
    # nibble substitution(S-boxes)
    binCode0 = sBoxInversed[binaryCode & 0b1111]
    binCode1 = sBoxInversed[(binaryCode & 0b1111_0000) >> 4]
    binCode2 = sBoxInversed[(binaryCode & 0b1111_0000_0000) >> 8]
    binCode3 = sBoxInversed[(binaryCode & 0b1111_0000_0000_0000) >> 12]

    substitutedCode = (binCode3 << 12) + (binCode0 << 8) + (binCode1 << 4) + (binCode2)

    return substitutedCode

def nibbleDecryptRound1(binaryCode):
    # mix columns. using GF
    nb0 = (binaryCode & 0b1000_0000_0000_0000)>>15
    nb1 = (binaryCode & 0b100_0000_0000_0000)>>14
    nb2 = (binaryCode & 0b10_0000_0000_0000)>>13
    nb3 = (binaryCode & 0b1_0000_0000_0000)>>12
    nb4 = (binaryCode & 0b1000_0000_0000)>>11
    nb5 = (binaryCode & 0b100_0000_0000)>>10
    nb6 = (binaryCode & 0b10_0000_0000)>>9
    nb7 = (binaryCode & 0b1_0000_0000)>>8
    nc0 = (binaryCode & 0b1000_0000)>>7
    nc1 = (binaryCode & 0b100_0000)>>6
    nc2 = (binaryCode & 0b10_0000)>>5
    nc3 = (binaryCode & 0b1_0000)>>4
    nc4 = (binaryCode & 0b1000)>>3
    nc5 = (binaryCode & 0b100)>>2
    nc6 = (binaryCode & 0b10)>>1
    nc7 = (binaryCode & 0b1)

    b0 = (nb3^nb5)<<15
    b1 = (nb0^nb6)<<14
    b2 = (nb1^nb4^nb7)<<13
    b3 = (nb2^nb3^nb4)<<12
    b4 = (nb1^nb7)<<11
    b5 = (nb2^nb4)<<10
    b6 = (nb0^nb3^nb5)<<9
    b7 = (nb0^nb6^nb7)<<8
    c0 = (nc3^nc5)<<7
    c1 = (nc0^nc6)<<6
    c2 = (nc1^nc4^nc7)<<5
    c3 = (nc2^nc3^nc4)<<4
    c4 = (nc1^nc7)<<3
    c5 = (nc2^nc4)<<2
    c6 = (nc0^nc3^nc5)<<1
    c7 = (nc0^nc6^nc7)

    unMixedColumnsCode = b0+b1+b2+b3+b4+b5+b6+b7+c0+c1+c2+c3+c4+c5+c6+c7

    # inverse nibble substitution(S-boxes)
    binCode0 = sBoxInversed[unMixedColumnsCode & 0b1111]
    binCode1 = sBoxInversed[(unMixedColumnsCode & 0b1111_0000) >> 4]
    binCode2 = sBoxInversed[(unMixedColumnsCode & 0b1111_0000_0000) >> 8]
    binCode3 = sBoxInversed[(unMixedColumnsCode & 0b1111_0000_0000_0000) >> 12]

    #inverse shift row
    substitutedCode = (binCode3 << 12) + (binCode0 << 8) + (binCode1 << 4) + (binCode2)

    return substitutedCode

#add round2 key
decryptRound2 = round2^key2

#inverse shift row, inverse nibble sub, add round 1 key
decryptRound1 = nibbleDecryptRound2(decryptRound2) ^ key1

#inverse mix columns, inverse shift row, inverse nibble sub, add rount 0 key
decryptRound0 = nibbleDecryptRound1(decryptRound1) ^ key0

binaryDecipheredtext = format(decryptRound0, 'b').zfill(16)
binaryCiphertext = format(round2, 'b').zfill(16)    #already ciphered above
print("Decryption of %s is %s" %(binaryCiphertext, binaryDecipheredtext))
