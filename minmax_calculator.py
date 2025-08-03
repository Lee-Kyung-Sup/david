def main():
    user_input = input("숫자들을 공백으로 구분해 입력하세요: ").split()
    
    try:
        numbers = [float(n) for n in user_input]
    except ValueError:
        print("Invalid input.")
        return

    max_value = numbers[0]
    min_value = numbers[0]

    for num in numbers[1:]:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num

    print(f"Min: {min_value}, Max: {max_value}")


if __name__ == "__main__":
     main()
