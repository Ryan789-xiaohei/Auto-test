"""
# 将角色的hp,和power通过传参传入
# 第二个角色，他叫后裔，后裔继承了角色的hp和power。并对了护甲属性。
# houyi_hp = hp+defense-enemy_power
# """
class Game:
    def __init__(self,hp,power):
        self.hp=hp
        self.power=power


    def fight(self, enemy_power, enemy_hp):
        final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if final_hp>enemy_hp:
            print("我赢了")
        elif final_hp<enemy_hp:
            print("敌人赢了")
        else:
            print("平局")
game = Game(88, 500)
game.fight(1000,500)