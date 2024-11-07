import random

# 랜덤 숫자와 입력한 숫자의 크기를 비교하는 함수
def compare_numbers(target, guess):
    if target > guess:
        return '랜덤 숫자보다 작습니다. 다시 입력하세요.'
    elif target < guess:
        return '랜덤 숫자보다 큽니다. 다시 입력하세요.'
    else:
        return '정답입니다!'

def play_game():
    target_number = random.randint(1, 10)
    print("행운의 랜덤 숫자를 맞혀보세요! 랜덤 숫자는 1 이상 10 이하입니다.")
    
    while True:
        while True:
            guess_number = int(input('예상 숫자: '))
            
            # 사용자의 입력값을 1~10 범위로 제한
            if guess_number < 1 or guess_number > 10:
                print('잘못된 입력입니다. 1 이상 10 이하의 수를 입력하세요.')
            else:
                break
            
        result = compare_numbers(target_number, guess_number)
        print(result)
        
        # 정답인 경우 반복문 탈출
        if '정답' in result:
            break

def main():
    restart = 'y'
    while True:
        play_game()
        
        while True:
            restart = input('게임을 다시 하시겠습니까? (y/n): ').lower()
            
            # 올바른 입력을 받도록 조건 작성
            if restart == 'y' or restart == 'n':
                break
            else:
                print('잘못된 입력입니다.')

        if restart == 'n':
            print('게임을 종료합니다.')
            break

if __name__ == "__main__":
    main()