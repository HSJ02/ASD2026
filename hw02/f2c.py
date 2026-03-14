def f2c(temp_f):
    return (temp_f - 32) * 5.0/9.0

temp_f = float(input("화씨도를 입력하세요: "))
print(f"{temp_f}°F는 {f2c(temp_f):.2f}°C입니다.")