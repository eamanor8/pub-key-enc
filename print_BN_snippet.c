
void printBN(char *msg, BIGNUM * a)
{
// Convert the BIGNUM to number string
    char * number_str = BN_bn2dec(a);
    
// Print out the number string
    printf("%s %s\n", msg, number_str);

// Free the dynamically allocated memory
    OPENSSL_free(number_str);
}

