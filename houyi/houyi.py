# 第二个角色，他叫后裔，后裔继承了角色的hp和power。并拥有了护甲属性。
from game import Game

class HouYi(Game):

    def __init__(self, defense):
        super().__init__(800, 200,)
        self.defense=defense
    def houyi_fight(self, enemy_power,enemy_hp ):
        final_hp = self.hp+self.defense - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if final_hp > enemy_final_hp:
            print("我赢了")
        elif final_hp < enemy_final_hp:
            print("敌人赢了")
        else:
            print("平局")

game1=HouYi(100)
game1.houyi_fight(1000,500)