from monster import Monster

class Iblis(Monster):
    def __init__(self, name, job, hp, max_hp, level):
        super().__init__(name, job, hp, max_hp, level, role="Raja Iblis")
        self.rage = False  

    def rage_mode(self):
        if self.hp <= self.max_hp * 0.5 and not self.rage:
           self.rage = True
           print(f"=== 👹 {self.name} Memasuki Rage Mode ===")


    def critical(self, target):
        dmg = 60 
        print(f"\n🔥 {self.name} menggunakan: 💥 Soul Mind Explosion!")
        print(f"🥊 {target.name} terkena {dmg} DMG dari {self.name}!")

        target.damage(dmg)

    def damage(self, dmg):
        super().damage(dmg)      
        self.rage_mode()        



    def domain(self, target1, target2, target3):
        dmg = 40
        print(f"\n🌑 {self.name} membuka: DOMAIN SOUL CORRUPTION!")
        print(f"💀 Semua target terkena {dmg} DMG!")
        for target in (target1, target2, target3):
            target.damage(dmg)
