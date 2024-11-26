from Crypto.Util import number
from random import getrandbits
import time

# Given parameters
p = 87712020782810358806012366960530480363676290880575039025592945358193408249897
q = 102835471351264451708400576484301274347085188629221996951152314010256656047547
e = 65537
N = p * q
given_d = 2777113439026967813870345260359839597823226328146295814538363064080293099090869828193345932139225213849393071682039628960771675474665521453093256445593377

# Generate keys
calculated_d = number.inverse(e, (p - 1) * (q - 1))
# confirm if the calculated_d is the same as the given_d
if(calculated_d == given_d):
    print("Value of d is verified. \nCalculated_d = ", calculated_d, "\nGiven_d = \t", calculated_d)
else:
    print("Value of d is not verified. \nCalculated_d = ", calculated_d, "\nGiven_d = ", calculated_d)

# Calculate the time that it takes to generate private keys of the following sizes: 256, 512,1024, 2048, 4096, and 8192.

# let's create a loop that takes the number of bits as an argument and returns the time it takes to generate private keys of that size
def generate_keys(bits):
    start_time = time.time()
    p = number.getPrime(bits)
    q = number.getPrime(bits)
    N = p * q
    e = 65537
    d = number.inverse(e, (p - 1) * (q - 1))
    end_time = time.time()
    time_taken = end_time - start_time
    print("Time taken to generate private keys of", bits, "bits: ", time_taken, "seconds")
    return N, e, d

# run the loop for 256, 512, 1024, 2048, 4096, 8192 bits
for bits in [256, 512, 1024, 2048, 4096, 8192]:
    generate_keys(bits)
    
