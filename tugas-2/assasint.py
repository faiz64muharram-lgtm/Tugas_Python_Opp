from hero import Hero

class Assasint (Hero):
    def __init__(self, name, job, hp, level,):
        super().__init__(name, job, hp, level,role="Assasint")


    def critical(self, target):
        dmg = 35
        print (f"\n🔥 {self.name} menggunakan: 🦋 Martial Soul!")
        print(f"🥊 {target.name} terkena critical {dmg} DMG dari {self.name}!")

       
        target.damage(dmg)