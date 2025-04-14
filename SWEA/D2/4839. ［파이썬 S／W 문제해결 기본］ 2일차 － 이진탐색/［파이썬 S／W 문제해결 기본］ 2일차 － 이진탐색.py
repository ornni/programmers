T = int(input())

def BinarySearch(count, start, end, target):
    middle = int((start+end)/2)

    if middle == target:
        return count+1
    elif middle > target:
        return BinarySearch(count+1, start, middle, target)
    elif middle < target:
        return BinarySearch(count+1, middle, end, target)

for tc in range(T):
    P, Pa, Pb = map(int, input().split())

    count_A = BinarySearch(0, 1, P, Pa)
    count_B = BinarySearch(0, 1, P, Pb)
    
    if count_A == count_B:
        print(f'#{tc+1} 0')
    elif count_A < count_B:
        print(f'#{tc+1} A')
    else:
        print(f'#{tc+1} B')