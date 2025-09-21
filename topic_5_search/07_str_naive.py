
# Наївний алгоритм пошуку підрядка має складність O(n×m), де n — довжина головного рядка, а m — довжина підрядка
# ситуацію, де довжина підрядка M наближається до довжини головного рядка 
# N, складність може бути представлена вже як 
# O(n^2). Це робить алгоритм неефективним для довгих рядків.
def naive_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    # Перебір по символах головного рядка
    for i in range(N - M + 1):
        j = 0
        # Перебір по символах підрядка
        while j < M:
            if main_string[i + j] != pattern[j]:
                break
            j += 1
        # Якщо значення j дорівнює довжині підрядка, то підрядок знайдено
        if j == M:
            return i

    return -1


def main():
    main_string = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    position = naive_search(main_string, pattern)

    if position != -1:
        print(f"Підрядок знайдено на позиції {position}")
    else:
        print("Підрядок не знайдено в головному рядку.")


if __name__ == '__main__':
   main()
