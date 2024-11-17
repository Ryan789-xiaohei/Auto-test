# 将角色的hp,和power通过传参传入
# 第二个角色，他叫后裔，后裔继承了角色的hp和power。并对了护甲属性。
# houyi_hp = hp+defense-enemy_power
# """
# 这里设置断点 你要干嘛？？？？？


from example.game_001 import GameYi

class HouYi(GameYi):
    def __init__(self, defense):
        self.defense=defense
        super().__init__(1000,200)

    def HouYi_fight(self, enemy_hp, enemy_power):
        while True:
            self.hp = self.hp+self.defense- enemy_power
            enemy_hp = enemy_hp - self.power
            print(self.hp)
            print(enemy_hp)
            if self.hp<=0:
                print("我输了")
                break
            elif enemy_hp<=0:
                print("敌人输了")
                break
game2=HouYi(-10)
game2.HouYi_fight(1000,200)