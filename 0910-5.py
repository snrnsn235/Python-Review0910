##클래스 선언
class car:
    speed=0
    def upspeed(self, value):
        self.speed+=value

        print("현재 속도(슈퍼 클래스) : %d" %self.speed)

class sedan(car):
    def upspeed(self, value):
        self.speed+=value

        if self.speed>150:
            self.speed=150

        print("현재 속도(서브 클래스) : %d" %self.speed)

class truck(car):
    pass ##빈 클래스

#변수 선언
sedan1, truck1=None, None

#메인 코드 부분
truck1=truck()
sedan1=sedan()

print("트럭-->", end="")
truck1.upspeed(200)
print("승용차-->", end="")
sedan1.upspeed(200)
