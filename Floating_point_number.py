# Число с плавающей точкой

# Создайте регулярное выражение для проверки того, является ли строка валидным числом с плавающей точкой. Обратите внимание: написать нужно паттерн, а не функцию.

pattern = "ваш_паттерн"
bool(re.match(pattern, "12.12")) ➞ True
bool(re.match(pattern, "12.")) ➞ False
bool(re.match(pattern, ".1")) ➞ True
bool(re.match(pattern, "-.1")) ➞ True
bool(re.match(pattern, "+4.4")) ➞ True
bool(re.match(pattern, "+4")) ➞ False
bool(re.match(pattern, "+4.4av")) ➞ False


pattern = "^[+-]?\d*\.\d+$"
