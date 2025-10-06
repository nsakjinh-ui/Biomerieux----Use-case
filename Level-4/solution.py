import binascii
import secrets
import hashlib
import os
import bcrypt

class Random_generator:

    # generates a random token using the secrets library for true randomness
    def generate_token(self, length=8, alphabet=(
        '0123456789'
        'abcdefghijklmnopqrstuvwxyz'
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    )):
        return ''.join(secrets.choice(alphabet) for i in range(length))

    # generates salt using the bcrypt library which is a safe implementation
    def generate_salt(self, rounds=12):
        return bcrypt.gensalt(rounds)

class SHA256_hasher:
    """
    NOTE: kept original class name/structure for compatibility.
    Internally uses PBKDF2-HMAC-SHA256 (100000 iterations) to derive a key,
    then hashes that derived key with bcrypt. Returns/stores bcrypt hashes
    as ASCII strings, and verifies accordingly.
    """

    # produces the password hash by deriving a key with PBKDF2 and then bcrypting it
    # salt: expected to be a bcrypt-style salt (bytes), e.g. bcrypt.gensalt()
    def password_hash(self, password, salt):
        # normalize salt to bytes if caller supplied string
        if isinstance(salt, str):
            salt = salt.encode('ascii')

        # derive a key using PBKDF2-HMAC-SHA256
        # 100_000 iterations is a reasonable default; tune to your environment
        dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100_000)

        # hash the derived key with bcrypt using provided bcrypt salt
        bcrypt_hash = bcrypt.hashpw(dk, salt)

        # return ASCII string for storage
        return bcrypt_hash.decode('ascii')

    # verifies that the hashed password matches the stored bcrypt hash
    def password_verification(self, password, password_hash):
        # ensure password_hash is bytes
        if isinstance(password_hash, str):
            password_hash_bytes = password_hash.encode('ascii')
        else:
            password_hash_bytes = password_hash

        # extract bcrypt salt from stored hash (first 29 bytes of bcrypt hash)
        bcrypt_salt = password_hash_bytes[:29]

        # re-derive the key using PBKDF2 with same salt/iterations
        dk = hashlib.pbkdf2_hmac('sha256', password.encode(), bcrypt_salt, 100_000)

        # bcrypt.checkpw compares the derived key against the stored bcrypt hash
        return bcrypt.checkpw(dk, password_hash_bytes)

# a collection of sensitive secrets necessary for the software to operate
PRIVATE_KEY = os.environ.get('PRIVATE_KEY')
PUBLIC_KEY = os.environ.get('PUBLIC_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')
PASSWORD_HASHER = 'SHA256_hasher'

# Solution explanation:

# Some mistakes are basic, like choosing a cryptographically-broken algorithm
# or committing secret keys directly in your source code.

# You are more likely to fall for something more advanced, like using functions that
# seem random but produce a weak randomness.

# The code suffers from:
# - reinventing the wheel by generating salt manually instead of calling gensalt()
# - not utilizing the full range of possible salt values
# - using the random module instead of the secrets module

# Notice that we used the “random” module, which is designed for modeling and simulation,
# not for security or cryptography.

# A good practice is to use modules specifically designed and, most importantly,
# confirmed by the security community as secure for cryptography-related use cases.

# To fix the code, we used the “secrets” module, which provides access to the most secure
# source of randomness on my operating system. I also used functions for generating secure
# tokens and hard-to-guess URLs.

# Other python modules approved and recommended by the security community include argon2
# and pbkdf2.
