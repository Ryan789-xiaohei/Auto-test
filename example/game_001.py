"""
一个回合制游戏，每个角色都有hp和power
hp 代表血量。power代表攻击力，hp初始值为1000，power的初始值为200.
定义一个fight的方法：
final_hp = hp-enemy_power
enemy_final_hp = enemy_hp - power
两个hp进行对比，血量生育多的人获胜
"""
from openpyxl.xml import defusedxml_env_set


class GameYi:
    def __init__(self,hp,power):
         self.hp=hp
         self.power=power

    def fight(self, enemy_power, enemy_hp):
        final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if final_hp>enemy_final_hp:
            print("我赢了")
        elif final_hp<enemy_final_hp:
            print("敌人赢了")
        else:
            print("平局")


# game = GameYi(800,200)
# game.fight(1000,500)

"""
# 将角色的hp,和power通过传参传入
# 第二个角色，他叫后裔，后裔继承了角色的hp和power。并对了护甲属性。
# houyi_hp = hp+defense-enemy_power
# """

# class HouYi(GameYi):
#     def __init__(self, defense):
#         self.defense=defense
#         super().__init__(800,700)
#
#     def HouYi_fight(self, enemy_power, enemy_hp):
#         final_hp = self.hp+self.defense- enemy_power
#         enemy_final_hp = enemy_hp - self.power
#         if final_hp>enemy_hp:
#             print("我赢了")
#         elif final_hp<enemy_hp:
#             print("敌人赢了")
#         else:
#             print("平局")
# game2=HouYi(800)
# game2.HouYi_fight(800,600)
