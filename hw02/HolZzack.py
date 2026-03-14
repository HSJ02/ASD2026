# 숫자를 입력받아 홀수 짝수를 구분하는 코드를 작성해주세요
def HolZzack(num):
    if num % 2 == 0:
        return "짝수"
    else:
        return "홀수"

def main():
    num = int(input("숫자를 입력하세요: "))
    result = HolZzack(num)
    print(f"{num}은(는) {result}입니다.")

if __name__ == "__main__":
    main()