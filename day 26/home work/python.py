my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


print(f"მე-5 ელემენტი: {my_list[4]}")
print(f"მე-7 ელემენტი: {my_list[6]}")
print(f"მე-9 ელემენტი: {my_list[8]}")

reversed_list = my_list[::-1][::2]
print(f"შემოტრიალებული სია ორის გამოტოვებით: {reversed_list}")