
s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
i = 0
j = len(s) -1
count = 0
while i < j:
    if s[i] != s[j] and count == 0:
        count += 1
        print(s[i:j+1])
        if s[i +1] == s[j]:
            print(s[i+1], s[j])
            i += 1
            continue
        elif s[i] == s[ j -1]:
            j -= 1
            continue
        print("False1")
    else:
        print(i)
        i += 1
        j -= 1
print(False)