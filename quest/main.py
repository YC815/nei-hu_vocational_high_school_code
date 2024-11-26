import json
import random

# 載入題目資料
with open('quest/test.json', 'r', encoding='utf-8') as file:
    questions = json.load(file)

# 輸入題目範圍
def get_question_range():
    while True:
        user_input = input("請輸入題目範圍 (例如: 1-20, ALL 或 [3, 5, 8]): ").strip()
        if user_input.lower() == "all":
            return list(range(1, 151))
        if user_input.startswith("[") and user_input.endswith("]"):
            try:
                question_numbers = list(map(int, user_input.strip("[]").split(",")))
                if all(1 <= num <= 150 for num in question_numbers):
                    return question_numbers
                else:
                    print("範圍超出題目數目，請重新輸入！")
            except ValueError:
                print("輸入格式錯誤，請重新輸入！")
        else:
            try:
                start, end = map(int, user_input.split('-'))
                if 1 <= start <= 150 and 1 <= end <= 150 and start <= end:
                    return list(range(start, end + 1))
                else:
                    print("範圍超出題目數目，請重新輸入！")
            except ValueError:
                print("輸入格式錯誤，請重新輸入！")

# 題目問答邏輯
def ask_questions(question_numbers, retry_mode=False):
    wrong_questions = []
    random.shuffle(question_numbers)  # 隨機排列題目順序

    for num in question_numbers:
        question_data = next(q for q in questions if q['question_number'] == num)
        print(f"\n題目 {num}: {question_data['question']}")
        for option, text in question_data['options'].items():
            print(f"  {option}: {text}")
        
        while True:
            answer = input("你的答案是 (A/B/C/D): ").strip().upper()
            if answer in "ABCD":
                if answer == question_data['correct_answer']:
                    print("✔ 答對了！")
                else:
                    print(f"✘ 答錯了，正確答案是 {question_data['correct_answer']}")
                    if not retry_mode:
                        wrong_questions.append(num)
                break
            else:
                print("無效的輸入，請輸入 A, B, C 或 D")

    return wrong_questions

# 主程式邏輯
if __name__ == "__main__":
    retry_mode = False
    previous_wrong_questions = []

    while True:
        if not retry_mode:
            question_range = get_question_range()
        else:
            question_range = previous_wrong_questions
            print("\n重新挑戰以下錯題範圍:", question_range)
        
        wrong_questions = ask_questions(question_range, retry_mode)
        
        if not wrong_questions:
            print("\n恭喜！該範圍所有題目已經全對！輸出: all")
            break
        else:
            print("\n錯題列表:", wrong_questions)
            previous_wrong_questions = wrong_questions
            retry_mode = True
