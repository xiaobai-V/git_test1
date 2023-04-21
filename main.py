print("hello git!")


# 冒泡排序

def bubble_sort(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


# 测试
if __name__ == "__main__":
    lists = [3, 4, 2, 8, 9, 5, 1]
    print(bubble_sort(lists))
