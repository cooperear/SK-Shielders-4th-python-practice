def merge_lists(list1, list2):
    """
    두 개의 리스트를 병합하여 하나의 리스트로 반환합니다.
    중복된 요소는 제거됩니다.
    """
    merged_list = list(set(list1 + list2))
    return merged_list

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print(f"병합된 리스트: {merge_lists(list1, list2)}")
print(f'공통 요소 : {set(list1) & set(list2)}')