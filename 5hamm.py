def Ham(s, t):
    dh = 0

    for i, c in enumerate(s):  # will make certain loops a bit cleare
        if c != t[i]:
            dh += 1

    return dh


if __name__ == "__main__":
    dataset = open('rosalind_hamm.txt').read()

    s, t = dataset.split()
    dist = Ham(s, t)

    print(dist)
