array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:  #array에 원소가 1개인 경우
        return
    pivot = start
    left = start+1
    right = end
    while(left <= right):
        while(left <= end and array[left] <= array[pivot]):
            #pivot보다 작은 큰 데이터 찾을 때까지 반복
            left += 1
        while(right > start and array[right] >= array[pivot]):
            # pivot보다 작은 작은 데이터 찾을 때까지 반복
            right -= 1
        if(left > right):   #엇갈리면 작은 데이터와 pivot 바꿈
            array[right], array[pivot] = array[pivot], array[right]
        else:   #아니면 큰 수와 작은 수 바꿈
            array[right], array[left] = array[left], array[right]
    #pivot을 기준으로 나눠진 왼쪽, 오른쪽에서 다시 정렬
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
quick_sort(array, 0, len(array) - 1)
print(array)