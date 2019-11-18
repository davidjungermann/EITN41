import hashlib

def read_hashes():
    f = open('hashes.txt', "r")
    hashes = f.readlines()
    f.close

    stripped_hashes = []
    for hash in hashes:
        stripped_hashes.append(hash.strip())
    return stripped_hashes

def conc_hash(hash, node):
    if node[0] == "L":
        return hash_node(node[1:] + hash)
    return hash_node(hash + node[1:])

def calc_merkle():
    hashes = read_hashes()
    past_hash = hashes.pop(0)
    for hash in hashes:
        past_hash = conc_hash(past_hash, hash)
    print("The merkle root is: " + past_hash)

def hash_node(hash):
    hash = bytes.fromhex(hash)
    return hashlib.sha1(hash).hexdigest()
     
calc_merkle()

