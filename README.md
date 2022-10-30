# ultrarian

early phase of a python runtime (de)cryptor

## what's this?

the goal is to provide a layer of security by running a python script after
encrypting its bytecode with a random 16-byte aes key but replacing 4 bits of
it, that need to be brute forced by the loader later.


