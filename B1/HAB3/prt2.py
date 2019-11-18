import hashlib


def read_hashes():
    f = open('example.txt', "r")
    hashes = f.readlines()
    f.close
    stripped_hashes = []
    for hash in hashes:
        stripped_hashes.append(hash.strip())
    return stripped_hashes


def main():
    leaves = read_hashes()
    leaf_index = leaves.pop(0).strip()
    path_depth = leaves.pop(0).strip()
    tree = build_tree(leaves)

def build_tree(leaves):
    cont = True
    tree = []
    tree.append(leaves[:])
    i = 1
    while(cont):
        tree.append([])
        while len(leaves) != 0:
            string = leaves.pop(0)
            if len(leaves) != 0:
                string = string + leaves.pop(0)
            else:
                string = string + string
            string = hashlib.sha1(bytes.fromhex(string)).hexdigest()
            tree[i].append(string)
            
        cont = len(tree[i]) != 1
        leaves = tree[i][:]
        i+=1
    return tree

main()   