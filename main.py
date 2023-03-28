import time
import random

# 필요한 기능들 함수로 정의하기


def y_or_n(question):
    while "input yes or no":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False


class Login():  # id 입력하고 확인 및 저장
    def __init__(self, name):
        self.name = name

    def input_name(self):
        self.name = input("플레이어 이름을 입력하세요 >> ")

    def id_check(self):
        q_id = (f'{self.name}, 이 이름이 맞습니까?')

        if y_or_n(q_id) == True:
            self.start_game
        else:
            id_count = 0
            while "re-input player name":
                name = input("다시 플레이어 이름을 입력하세요 >> ")
                id_count += 1
                if y_or_n(q_id) == True:
                    self.start_game()
                    return name
                elif id_count == 4:
                    Ending.errorend()
                    break

    def start_game(self):
        self = print(f'{self.name}(으)로 게임을 시작합니다!')


# 플레이어 코드
# 플레이어 생성 - 이름 입력
# 플레이어 공격타입 2가지, 일반, 마법

class Player(Login):  # 플레이어
    def __init__(self, name, hp, mp, power):
        self.name = super().__init__(name)
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.power = power

    def attack(self, enemy):
        damage = random.randint(self.power - 2, self.power + 2)
        enemy.hp = max(enemy.hp - damage, 0)
        if damage:
            time.sleep(1)
            print(f"{self.name}의 공격! {enemy.name}에게 {damage}의 피해를 입혔습니다.")

    def magic_attack(self, enemy):
        magic_damage = random.randint(self.power - 5, self.power + 15)
        enemy.hp = max(enemy.hp - magic_damage, 0)
        if magic_damage:
            self.mp -= 20
            print('mp를 20 사용했다.')
            time.sleep(1)
            print(f"{self.name}의 마법 공격! {enemy.name}에게 {magic_damage}의 피해를 입혔습니다.")

    def cure(self):
        self.mp -= 10
        self.cure = random.randint(self.power - 2, self.power + 10)
        time.sleep(1)
        print(f'치유 마법으로 {self.cure}만큼 치료되었다.')

    def show_status(self):
        print(
            f"{self.name}의 상태: HP {self.hp}/{self.max_hp}, MP {self.mp}/{self.max_mp}")


# 몬스터 코드 - random을 사용하여 임의 생성(마릿수가? 특성이?)
# 몬스터는 일반 공격


class Monster():
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power
        self.attribute = "무서운"

    def attack(self, damage):
        self.hp -= damage
        damage = self.power(10)

        Player.hp = max(Player.hp - damage, 0)
        if damage:
            print(f"{self.name}의 공격! {Player.name}에게 {damage}의 피해를 입혔습니다.")

    def status_check(self):
        print(f'몬스터의 hp가 {self.hp} 남았다')


class FireMonster(Monster):
    def __init__(self):
        self.attribute = "불꽃"
        super().__init__(hp)

    def attack(self, damage):
        super().attack
        damage = self.power(12)

    def status_check(self):
        print(f'{self.attribute}몬스터의 hp가 {self.hp} 남았다')


class IceMonster(Monster):
    def __init__(self):
        self.attribute = "서리"
        super().__init__(hp)

    def attack(self, damage):
        super().attack
        damage = self.power(15)

    def status_check(self):
        print(f'{self}몬스터의 hp가 {self.hp} 남았다')


# while을 사용해 종료조건 충족할 때 까지 턴제로 전투 진행

class RunGame():
    def create_unit(self, enemy):
        player_status = Player.show_status
        print(player_status)

        enemy_status = enemy.status_check()
        print(f'{enemy}몬스터와 마주쳤다!')
        print(enemy_status)

        def player_turn(self):
            print(f'{Player.__name__}의 차례')

            print('< 스킬 선택 >')
            print('1 물리 공격')
            print('2 마법 공격')
            print('3 치유 마법')
            ps_input = int(input('사용할 스킬의 번호를 입력하세요. : '))

            while "1~3을 입력할 때까지":
                if ps_input == 1:
                    Player.attack
                    print(enemy_status)
                elif ps_input == 2:
                    Player.magic_attack
                    print(enemy_status)
                elif ps_input == 3:
                    Player.cure
                    print(enemy_status)
                else:
                    print('잘못된 입력! 1 2 3 중 하나를 입력하세요.')
                    continue

        def enemy_turn(enemy):
            print(f'{enemy}의 차례')
            time.sleep(1.5)
            print(enemy.attack())

        def unit_status():
            time.sleep(1)
            print(player_status)
            print(enemy_status)

    # 종료 조건 : 플레이어의 패배, 모든 몬스터에게 승리


class Ending():
    def __init__(self):
        self.victory = print(Ending.victoryend)
        self.defeat = print(Ending.defeatend)
        self.bad = print(Ending.badend)
        self.dream = print(Ending.dreamend)
        self.error = print(Ending.errorend)

    def victoryend():  # 승리 시
        print("당신은 연인을 지켜내었습니다!")
        print("환상의 동물이 👍를 눌러 관심을 표현했습니다^^ -끝-")

    def defeatend():  # 패배 시
        print("전투에서 패배했다!")
        time.sleep(1)
        print("연인이 환상의 동물이 되어 사라졌습니다... -끝-")

    def badend():  # 도망친다를 선택했을 때
        print("도망가는 중...")
        time.sleep(2)
        print("...")
        time.sleep(3)
        print("연인을 지키지 못한 당신은 평생을 홀로 살았습니다.. -끗-")

    def dreamend():
        print("당신은 꿈에서 깨어났습니다.")
        time.sleep(3)
        print("옆을 돌아본 당신의 눈가에 눈물이 맺혔습니다.")
        time.sleep(2)
        print("-꿈-")

    def errorend():
        print("Error!")
        print("갈팡질팡하다 패배했다.")
        if y_or_n("retry? : ") == True:
            print(login.input_name())
        else:
            ("게임을 종료합니다.")


# 게임 실행
def run_game():
    while "둘 중 한 유닛hp가 0이 될때까지":
        print(in_game.player_turn())
        time.sleep(2)
        print(in_game.unit_status())
        time.sleep(1)
        print(in_game.enemy_turn())
        time.sleep(2)
        print(in_game.unit_status())
        if enemy.hp == 0:
            print(endings.victory)
            break
        elif player.hp == 0:
            print(endings.defeat)
            break
        else:
            print(endings.dream)
            break

    if y_or_n("새로운 게임을 시작할까요? : ") == True:
        print("새 게임을 시작합니다!")
        print(login.input_name)
        run_game
    else:
        print("게임을 종료합니다.")


"""여기부터 게임 실행 코드"""

login = Login()
player = Player({Login.name}, 100, 100, 10)
in_game = RunGame()
endings = Ending()
enemy = random.choice(Monster, FireMonster, IceMonster)


# print하는 함수를 만들기

# 게임 play 내용 입력
# class 호출 : 변수를 만들어 인스턴스를 생성하고, 메소드를 호출한다.

print("평화로운 서울 한복판에 몬스터가 나타났다!!")
time.sleep(1.5)
print("당신은 함께있던 연인을 지켜야합니다!")
time.sleep(1.5)
if y_or_n("싸울까?") == True:
    print("내 이름은..")
    time.sleep(1)
    print(login.input_name())
    if login.name in login:
        in_game.create_unit()
        print(run_game)

else:
    time.sleep(1.5)
    if y_or_n("..정말로 도망갈까?") == True:
        print(endings.bad)
    else:
        time.sleep(2)
        print("연인을 보고 용기를 냈다.")
        time.sleep(1)
        print("내 이름은..")
        print(login.input_name())
        if login.name in login:
            in_game.create_unit()
            print(run_game)


# if yes_or_no("새로운 게임을 시작할까요?") == True:
#     print("새 게임을 시작합니다!")
#     print(Id.add_id)
# else:
#     print("게임을 종료합니다.")


# print(f'{id}(이)가 monster_random 을 만났다!')
# print("도망쳤다!")
# print("승리!")

# input문으로 아예..?

# if yes_or_no("새로운 게임을 시작할까요?") == True:
#     print("새 게임을 시작합니다!")
#     print(Id.add_id)
# else:
#     print("게임을 종료합니다.")


# 전투관련
# 매 전투시 플레이어, 몬스터의 상태정보 출력 (hp mp 등)
#
