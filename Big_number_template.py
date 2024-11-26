from Crypto.Util import number
from random import getrandbits

nbits = 512

primeNum1 = number.getPrime(nbits)
primeNum2 = 7966919325049983427477025466251372129123
moduloN = getrandbits(512)

multipl = primeNum1*primeNum2

print ("a*b=", hex(multipl))

modExp = (primeNum1 * primeNum2) % moduloN
print ("(a^c) mod n =", hex(modExp))
