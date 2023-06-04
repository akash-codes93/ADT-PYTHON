

def compute_lps(pattern):

    i = 0
    j = 1

    lps = [0]* len(pattern)

    while j < len(pattern):

        if pattern[i] == pattern[j]:
            i += 1
            lps[j] = i
            j += 1

        elif i == 0:
            j += 1
        else:
            i = lps[i-1]

    return lps


# l = compute_lps("abxdababxabxd")
# print(l)

def kmpString(pattern, text):
    i = 0
    j = 0

    lps = compute_lps(pattern)
    initial_point = []

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        elif j ==0 :
            i += 1
        else:
            j = lps[j-1]

        if j == len(pattern):
            initial_point.append(i-j)
            j = 0  # j = lsp[j-1]
            print(j)

    return initial_point


ip = kmpString("xyx", "axxxyxyxyxb")
# ip = kmpString("abc", "ababc")
print(ip)


