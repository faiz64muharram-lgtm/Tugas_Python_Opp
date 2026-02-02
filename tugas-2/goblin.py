from monster import Monster

class Goblin(Monster):
    def __init__(self, name, job, hp, max_hp, level):
        super().__init__(name, job, hp, max_hp, level, role="Goblin")


    def critical(self, target):
        dmg = 15
        print (f"\n🔥 {self.name} menggunakan: 🕸️  Soul Binding Curse !")
        print(f"🥊 {target.name} terkena critical {dmg} DMG dari {self.name}!")

      
        target.damage(dmg)