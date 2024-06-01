import re

pattern_password = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
user_input = input("Введите пароль: ")
invalid_pass_text = (
    "Ваш пароль должен содержать не менее 8 символов "    "по крайней мере, заглавную и "
    "строчную букву, цифру "    "и символ для обеспечения безопасности"
)
if re.search(pattern_password, user_input):
    print("Strong Password Set! Good job!")
else:
    print(invalid_pass_text)
