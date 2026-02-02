from hero import Hero

class Tank (Hero):
    def __init__(self, name, job, hp, level,):
        super().__init__(name, job, hp, level,role="Tank")


    def critical(self, target):
        dmg = 11
        print (f"\n🔥 {self.name} menggunakan: 🌊 Water Domain!")
        print(f"🥊 {target.name} terkena critical {dmg} DMG dari {self.name}!")


        target.damage(dmg)

    def shield(self, tim):
        heal_amount = 15
        tim.heal(heal_amount)
        print(f"\n🔥 {self.name} menggunakan: 🌀 Xuanwu Suppression!")
        print(f"💚 {tim.name} menerima +15 HP dari {self.name} !")
