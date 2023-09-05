

def collatz(num: int) -> int:
    """
    @param num: 正整数
    @return: 函数返回
    """
    result = num % 2
    if result == 0:
        result = num // 2
        print(num // 2)
        if result != 1:
            collatz(result)
        else:
            print(f"最终的结果是: {result}")
    else:
        result = num * 3 + 1
        print(result)
        collatz(result)

    return result

# collatz(100)
# collatz(-7)
try:
    a = int(input("请输入任意整数:"))
except ValueError as e:
    print(e)
else:
    collatz(a)
