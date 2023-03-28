import time
import random
import sys

# 필요한 기능들 함수로 정의하기


def y_or_n(question):
    while "input yes or no":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[0] != 'y' or 'n':
            print("y나 n을 입력해주세요.")
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False


class Login():  # id 입력하고 확인 및 저장
    def __init__(self):
        self.name = None

    def input_name(self):
        self.name = input("플레이어 이름을 입력하세요 >> ")

    def id_check(self):
        q_id = (f'{self.name}, 이 이름이 맞습니까?')

        if self.name is None:
            while "re-input player name":
                self.input_name(("다시 플레이어 이름을 입력하세요 >> "))
                id_count = 0

                if y_or_n(q_id) is True:
                    self.start_game()
                else:
                    self.input_name("다시 플레이어 이름을 입력하세요 >> ")
                    id_count += 1
                    if id_count == 3:
                        Ending.errorend()
                        break

    def start_game(self):
        self = print(f'{self.name}(으)로 게임을 시작합니다!')


# 플레이어 코드
# 플레이어 생성 - 이름 입력
# 플레이어 공격타입 2가지, 일반, 마법

class Player():  # 플레이어
    def __init__(self, name, hp, mp, power):
        self.name = name
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
    def __init__(self, name='무서운', hp=100, power=10, attribute='무서운'):
        self.name = name
        self.hp = hp
        self.power = power
        self.attribute = attribute

    def attack(self, player, damage=1):
        self.hp -= damage
        damage = self.power * damage

        player.hp = max(player.hp - damage, 0)
        if damage:
            print(f"{self.name}의 공격! {player.name}에게 {damage}의 피해를 입혔습니다.")

    def status_check(self):
        print(f'{self.name}몬스터의 hp가 {self.hp} 남았다')


class FireMonster(Monster):
    def __init__(self):
        super().__init__('불꽃', 100, 10, '불꽃')

    def attack(self, player, damage=1.3):
        super().attack(player, damage)


class IceMonster(Monster):
    def __init__(self):
        super().__init__('서리', 120, 10, '서리')

    def attack(self, player, damage=1.1):
        super().attack(player, damage)


# while을 사용해 종료조건 충족할 때 까지 턴제로 전투 진행

class RunGame():
    def create_unit(self):
        enemy = random.choice([Monster, FireMonster, IceMonster])
        enemy = enemy()

        print(f'{enemy.name}몬스터와 마주쳤다!')
        enemy.status_check()
        return enemy

    def player_turn(self, player, enemy):
        print(f'{player.name}의 차례')

        print('< 스킬 선택 >')
        print('1 물리 공격')
        print('2 마법 공격')
        print('3 치유 마법')
        ps_input = int(input('사용할 스킬의 번호를 입력하세요. : '))

        while ps_input in range(1, 3):
            if ps_input == 1:
                player.attack(enemy)
                enemy.status_check()
            elif ps_input == 2:
                player.magic_attack(enemy)
                enemy.status_check()
            elif ps_input == 3:
                player.cure()
                enemy.status_check()
            else:
                print('잘못된 입력! 1 2 3 중 하나를 입력하세요.')
                continue

    def enemy_turn(self, player, enemy):
        print(f'{enemy.name}의 차례')
        time.sleep(1.5)
        print(enemy.attack(player))

    def unit_status(self, player, enemy):
        time.sleep(1)
        player.show_status()
        enemy.status_check()

    # 종료 조건 : 플레이어의 패배, 모든 몬스터에게 승리


class Ending():
    def __init__(self):
        pass

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

    def retry():
        if y_or_n("retry? : ") == True:
            print("새로운 적이 나타났다! 내 이름은..")
            time.sleep(1)
            print(login.input_name())

            player = Player(login.name, 100, 100, 10)
            in_game = RunGame()
            enemy = in_game.create_unit()
            print(run_game())
        else:
            ("게임을 종료합니다.")
            time.sleep(2)
            sys.exit


# 게임 실행
def run_game(player, enemy):
    while "둘 중 한 유닛hp가 0이 될때까지":
        print(in_game.player_turn(player, enemy))
        time.sleep(2)
        print(in_game.unit_status(player, enemy))
        time.sleep(1)
        print(in_game.enemy_turn(player, enemy))
        time.sleep(2)
        print(in_game.unit_status(player, enemy))
        if enemy.hp == 0:
            print(endings.victoryend())
            break
        elif player.hp == 0:
            print(endings.defeatend())
            break
        else:
            print(endings.dreamend())
            break


"""여기부터 게임 실행 코드"""

login = Login()
endings = Ending()

# print하는 함수를 만들기

# 게임 play 내용 입력
# class 호출 : 변수를 만들어 인스턴스를 생성하고, 메소드를 호출한다.

print("평화로운 서울 한복판에 몬스터가 나타났다!!")
time.sleep(1.5)
print("당신은 함께있던 연인을 지켜야합니다!")
time.sleep(1.5)

if y_or_n("싸울까?") == False:
    if y_or_n("..정말로 도망갈까?") == True:
        print(endings.bad)
        exit(0)
    else:
        time.sleep(2)
        print("연인을 보고 용기를 냈다.")
        time.sleep(1)

print("내 이름은..")
time.sleep(1)
print(login.input_name())
if login.name:
    print(login.id_check())

    player = Player(login.name, 100, 100, 10)
    in_game = RunGame()
    enemy = in_game.create_unit()
    print(run_game())


# print(endings.retry())
