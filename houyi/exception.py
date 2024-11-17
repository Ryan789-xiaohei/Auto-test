from logging import exception

from game import Game


class HouYi(Game):

    def __init__(self, defense):
        super().__init__(1000, 500,)
        self.defense=defense
    def houyi_fight(self, enemy_hp,enemy_power ):
        final_hp = self.hp+self.defense - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if final_hp > enemy_final_hp:
            print("我赢了")
        elif final_hp < enemy_final_hp:
            print("敌人赢了")
        else:
            raise exception("没有平局")

game1=HouYi(0)
game1.houyi_fight(1000,500)