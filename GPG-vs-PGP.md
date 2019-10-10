# GPG vs. PGP

PGP, GPG, GnuPG, Open PGP. These terms file under the same category but refer to slightly different things.

# Analogy

- PGP is a car
- OpenPGP is the requirements for the PGP car
- GnuPG is another car satisfying the same requirements
- RSA is a diesel engine, and other engines are available
- SSH isn't a car at all. But it uses engines.

# PGP (Pretty Good Privacy)

PGP stands for Pretty Good Privacy. It was created in the 1990s and is currently owned by security software company **Symantec**. Over the course of nearly three decades, PGP has been developed, improved, and updated, making it the standard option for file encryption today.

PGP uses several encryption technologies, like hashing, data compression, and public/private PGP keys to protect an organization’s critical information (i.e., the company’s crown jewels). While it’s often used to encrypt files before exchanging them with trading partners or remote locations, PGP can also encrypt emails, directories, and disk partitions, so it's a fitting solution for modern cybersecurity needs.

# Open PGP

Open PGP is an encryption standard. Vendors who want to include Open PGP in their solutions must follow IETF (Internet Engineering Task Force) standards and integrate well with other Open PGP-compliant software vendors.

## How it works

OpenPGP is a hybrid of the two-key cryptography approach where the message to be exchanged (called plaintext) is first compressed and then a **session key** is created as a one-time use secret key. The compressed plaintext is then encrypted with the session key. The session key is then encrypted with the destination’s public key and bundled with the encrypted message (called ciphertext). The destination can decrypt the session key with their private key then then decompress it to recover the original plaintext.

# GPG (GNU Privacy Guard)

GPG, or **[GnuPG](https://www.goanywhere.com/managed-file-transfer/encryption/gnupg-gpg)**, stands for GNU Privacy Guard. GPG is a different implementation of the Open PGP standard and a strong alternative to Symantec’s official PGP software.

GPG is defined by RFC 4880 (the official name for the Open PGP standard). The GPG Project provides the tools and libraries to allows users to interface with a GUI or command line to integrate encryption with emails and operating systems like **[Linux](https://www.goanywhere.com/platforms/linux)**. GPG can open and decrypt files encrypted by PGP or Open PGP, meaning it works well with other products.

# Comparisons

## GPG vs. PGP

PGP is a proprietary solution owned by Symantec, and GPG is an open source standard. Functionally, each format is virtually identical.

## GPG vs. RSA

[RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) is a public-key cryptosystem. That is, it is an algorithm for encrypting, decrypting and signing data using a set of two keys (the public key and private key).

PGP and GnuPG both offer the use of RSA for general purpose encryption and signing of data. They also offer other options, like [Elgamal and DSA](https://en.wikipedia.org/wiki/ElGamal_encryption).

## GPG vs. SSH

SSH uses RSA for authentication, not encryption. The server has your public key, and you have the private key, and SSH uses this fact to make sure you are, well, you. SSH also supports other keypairs, for example, [ECDSA](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm).

# References

- [https://askubuntu.com/questions/785056/difference-between-pgp-protocol-and-rsa-protocol](https://askubuntu.com/questions/785056/difference-between-pgp-protocol-and-rsa-protocol)
- [https://www.goanywhere.com/blog/2019/03/28/pgp-vs-gpg-whats-the-difference](https://www.goanywhere.com/blog/2019/03/28/pgp-vs-gpg-whats-the-difference)
- [https://www.quora.com/What-is-a-GPG-key-and-how-do-I-create-it](https://www.quora.com/What-is-a-GPG-key-and-how-do-I-create-it)
- [https://cran.rstudio.com/web/packages/gpg/vignettes/intro.html](https://cran.rstudio.com/web/packages/gpg/vignettes/intro.html)

[Difference between pgp protocol and rsa protocol](https://askubuntu.com/questions/785056/difference-between-pgp-protocol-and-rsa-protocol)

[Difference between pgp protocol and rsa protocol](https://askubuntu.com/questions/785056/difference-between-pgp-protocol-and-rsa-protocol)

[PGP vs. GPG: What's the Difference?](https://www.goanywhere.com/blog/2019/03/28/pgp-vs-gpg-whats-the-difference)

[What is a GPG key, and how do I create it?](https://www.quora.com/What-is-a-GPG-key-and-how-do-I-create-it)

[Encryption and Digital Signatures using GPG](https://cran.rstudio.com/web/packages/gpg/vignettes/intro.html)