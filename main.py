# This is a sample Python script.
import re
import hashlib

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def crack_md5_from_text(text):
    md5_pattern = r'[0-9a-fA-F]{32}'

    md5_hashes = re.findall(md5_pattern, text)

    if not md5_hashes:
        return "MD5-хеши не найдены в тексте."

    common_strings = [
        "admin", "user", "login", "password", "123456", "123",  "qwerty", "letmein",
        "admin123", "pass123", "test", "guest", "thunder", "root", "secret", "hello"
    ]

    results = {}

    for md5_hash in md5_hashes:
        print(f"Пытаемся восстановить строку для хеша: {md5_hash}")
        found = False

        for candidate in common_strings:
            candidate_hash = hashlib.md5(candidate.encode('utf-8')).hexdigest()
            if candidate_hash.lower() == md5_hash.lower():
                results[md5_hash] = candidate
                found = True
                print(f"Найдено совпадение! Хеш {md5_hash} соответствует строке: {candidate}")
                break

        if not found:
            results[md5_hash] = "Не удалось восстановить (попробуйте расширить словарь)."

    return results


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Player')
    text = """
        Инструкция по установке и запуску Django-проекта
        Login MD5: 5C7686C0284E0875B26DE99C1008E998
        Password MD5: 202CB962AC59075B964B07152D234B70
        """

    result = crack_md5_from_text(text)

    print("\nРезультаты:")
    for md5_hash, original in result.items():
        print(f"MD5: {md5_hash} -> {original}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/