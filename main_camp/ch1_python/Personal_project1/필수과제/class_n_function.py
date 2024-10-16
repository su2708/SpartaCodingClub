class Person:
    def __init__(self, name: str, gender: str, age: int):
        self.name: str = name
        self.gender: str = gender
        self.age: int = age
        
    def display(self):
        print(f'이름: {self.name}, 성별: {self.gender}')
        print(f'나이: {self.age}')
        
def main():
    while True:
        try:
            age = int(input('나이: '))
            if age <= 0 or age > 150:
                raise ValueError('1 이상 150 이하 사이의 값으로 입력하세요.')
            name = input('이름: ')
            gender = input('성별: ')
            break
        # 잘못된 나이를 입력할 경우
        except ValueError as ve:
            print(f'잘못된 나이 입력입니다: {ve}')
        except Exception as e:
            print(f'에러 발생: {e}')
        
    person = Person(name, gender, age)
    person.display()

if __name__ == '__main__':
    main()