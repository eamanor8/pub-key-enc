#include <stdio.h>
#include <string.h>
#include <openssl/bn.h>
#define NBITS 256

void printBN(char *msg, BIGNUM * a)
{
/* Use BN_bn2hex(a) for hex string
   Use BN_bn2dec(a) for decimal string */
    char * number_str = BN_bn2hex(a);
    printf("%s %s\n", msg, number_str);
    OPENSSL_free(number_str);
}

int main ()
{
    char msg[] = "Hello, this is my first RSA message!";
    int len = strlen(msg);

    char msginhex[NBITS];

    // Convert text to hex and store it in hex[].
    for (int i = 0, j = 0; i < len; ++i, j += 2)
      sprintf(msginhex + j, "%02x", msg[i] & 0xff);

    BIGNUM *msgBN = BN_new();
    BN_hex2bn(&msgBN, msginhex);
    printf("Original message = %s\n",msg);
    printBN("Hex converted Message = ",msgBN);
}
