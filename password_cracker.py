import hashlib

def crack_sha1_hash(target_hash, use_salts=False):
    # Load the top 10,000 passwords
    with open('top-10000-passwords.txt', 'r') as f:
        passwords = [line.strip() for line in f]
    
    # Load salts if needed
    salts = []
    if use_salts:
        with open('known-salts.txt', 'r') as f:
            salts = [line.strip() for line in f]
    
    # Check each password
    for password in passwords:
        if use_salts:
            # Try each salt combination
            for salt in salts:
                # Try salt before password
                salted_password = salt + password
                hashed = hashlib.sha1(salted_password.encode()).hexdigest()
                if hashed == target_hash:
                    return password
                
                # Try salt after password
                salted_password = password + salt
                hashed = hashlib.sha1(salted_password.encode()).hexdigest()
                if hashed == target_hash:
                    return password
        else:
            # Check plain password
            hashed = hashlib.sha1(password.encode()).hexdigest()
            if hashed == target_hash:
                return password
    
    return "PASSWORD NOT IN DATABASE"