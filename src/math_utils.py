def factorial(n: int) -> int:
    """Trả về giai thừa của số nguyên không âm n."""
    if n < 0:
        raise ValueError("Đối số phải là số nguyên không âm")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
