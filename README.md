# Simple-ThreeCryptography

## 3 Different Ciphers
1. Caesar Cipher
2. Vigenere Cipher
3. Simplifly AES(S-AES)

# Requirements
* numpy 1.24 or later
* matplotlib 3.6.3

# Files
* ## Caesar_Cipher.py
    Break Caesar Cipher after found out key length(1) by coincidence and find key by brute force.

* ## Vigenere_Cipher.py
    Break Vigenere Cipher after found out key length(8) by coincidence and find key by letter Freqeuncy.

* ## S-AES.py
    Break Simplify AES by following steps in Note.

# RUN
python Caesar_Cipher.py<br>
python Vigenere_Cipher.py<br>
python S-AES.py

# Note
Note that for Caesar_Cipher.py & Vigenere_Cipher.py, key length is found out by coincidences.<br>
Note that S-AES follows next steps.<br>
## Encryption:<br>
1. Add Round 0 Key
2. Nibble substitution(use S-box)
3. Shift Row
4. Mix Columns
5. Add Round 1 Key
6. Nibble substitution(use S-box)
7. Shift Row
8. Add Round 2 Key
## Decryption:<br>
1. Add Round 2 Key
2. Inverse shift row
3. Inverse nibble sub
4. Add Round 1 Key
5. Inverse Mix Columns
6. Inverse Shift Row
7. Inverse nibble Sub
8. Add Round 0 key
