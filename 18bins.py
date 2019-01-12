def binary_search(arr, k):
	return binary_search_helper(arr, k, 0, len(arr))

def binary_search_helper(arr, k, n, m):
	if n >= m:
		return -1

	elif n == m-1:
		if arr[n] == k:
			return n+1

		else:
			return -1

	mid = (n + m) // 2
	if arr[mid] > k:
		return binary_search_helper(arr, k, n, mid)
	else:
		return binary_search_helper(arr, k, mid, m)

if __name__ == '__main__':
    with open('rosalind_BINS.txt') as inFile:
        n = int(inFile.readline())
        m = int(inFile.readline())
        arr = list(map(int, inFile.readline().split()))
        ks = list(map(int, inFile.readline().split()))

    with open('bins.txt', 'w') as outFile:
        print(' '.join(map(str, [binary_search(arr, k) for k in ks])), file=outFile)