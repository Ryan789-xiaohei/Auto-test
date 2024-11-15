# 将角色的hp,和power通过传参传入
# 第二个角色，他叫后裔，后裔继承了角色的hp和power。并对了护甲属性。
# houyi_hp = hp+defense-enemy_power
# """
# 这里设置断点 你要干嘛？？？？？
from example.game_001 import GameYi

class HouYi(GameYi):
    def __init__(self, defense):
        self.defense=defense
        super().__init__(800,700)

    def HouYi_fight(self, enemy_power, enemy_hp):
        final_hp = self.hp+self.defense- enemy_power
        enemy_final_hp = enemy_hp - self.power
        if final_hp>enemy_hp:
            print("我赢了")
        elif final_hp<enemy_hp:
            print("敌人赢了")
        else:
            print("平局")

game2=HouYi(900)
game2.HouYi_fight(800,500)