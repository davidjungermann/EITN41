import hashlib


def read_hashes():
    f = open('leaves.txt', "r")
    hashes = f.readlines()
    f.close
    stripped_hashes = []
    for hash in hashes:
        stripped_hashes.append(hash.strip())
    return stripped_hashes


def main():
    leaves = read_hashes()
    leaf_index = int(leaves.pop(0).strip())
    path_depth = int(leaves.pop(0).strip())
    tree = build_tree(leaves)
    merkle_root = tree[len(tree) - 1][0]
    route = calc_route(leaf_index, tree)
    string = str(route[len(tree) - path_depth - 1]) + merkle_root
    print("The concatination of the specifed node and the Merkle root is: " + string)


def build_tree(leaves):
    cont = True
    tree = []
    tree.append(leaves[:])
    i = 1
    while cont:
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
        i += 1
    return tree


def calc_route(leave_index, tree):

    index = leave_index
    route = []
    for i in range(len(tree) - 1):
        if(index % 2 == 0):
            if len(tree[i]) - 1 < index + 1:
                route.append("R" + tree[i][index])
            else:
                route.append("R" + tree[i][index + 1])
        else:
            route.append("L" + tree[i][index - 1])
        index = index // 2
    return(route)


main()
