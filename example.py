from perlish import die

print("--- and die のテスト ---")
print("好きな数値を入力してください（0以外を入力するとor dieのテストに進みます）:")
num_str = input()
num = int(num_str) if num_str.isdigit() else -1

(num == 0) and die(f"とほほ: 0が入力されました。入力値: {num}")

print(f"{num}が入力されました！わーい！")
print("-" * 20)


print("--- and die のテスト ---")
print("好きな数値を入力してください（20以上ならテストを終了します）:")
age_str = input()
age = int(age_str) if age_str.isdigit() else -1

# Perl: $age < 20 and die "..."
# ageが20未満である(True) -> 右側のdieが実行される
# ageが20未満でない(False) -> 右側は実行されない
(age >= 20) or die(f"しょぼん: 20歳未満の方はご遠慮ください。年齢: {age}")

print(f"お客様は{age}才です！やったぁ！")