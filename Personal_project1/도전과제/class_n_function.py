class Person:
    def __init__(self):
        while True:
            try:
                self.age = int(input('나이: '))
                if self.age <= 0 or self.age > 150:
                    raise ValueError('1 이상 150 이하 사이의 값으로 입력하세요.')
                
                self.name = input('이름: ')
                
                # 성별 입력이 'male' 또는 'female'일 때까지 반복
                while True:
                    self.gender = input('성별: ')
                    if self.gender == 'male' or self.gender == 'female':
                        break
                    else:
                        print("잘못된 성별을 입력하셨습니다. 'male' 또는 'female'을 입력하세요.")
                break
            except ValueError as ve:
                print(f'잘못된 입력입니다: {ve}')
            except Exception as e:
                print(f'에러 발생: {e}')
        
    def display(self):
        print(f'이름: {self.name}, 성별: {self.gender}')
        print(f'나이: {self.age}')
        
    # 나잇대에 맞는 인사
    def greet(self):
        if self.age < 20:
            print(f'안녕하세요, {self.name}! 미성년이시군요!')
        else:
            print(f'안녕하세요, {self.name}! 성인이시군요!')
        
def main():    
    person = Person()
    person.display()
    person.greet()

if __name__ == '__main__':
    main()
