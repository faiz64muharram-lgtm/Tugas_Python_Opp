from monster import Monster

class Iblis(Monster):
    def __init__(self, name, job, hp, max_hp, level):
        super().__init__(name, job, hp, max_hp, level, role="Raja Iblis")
        self.rage = False  # status rage

    # 🔥 cek rage mode
    def check_rage(self):
        if self.hp <= self.max_hp / 2 and not self.rage:
            self.rage = True
            print(f"\n== 👹 {self.name} Masuk Rage Mode ==\n")

    def critical(self, target):
        dmg = 60
        if self.rage:
            dmg += 30  

        print(f"\n🔥 {self.name} menggunakan: 💥 Soul Mind Explosion!")
        print(f"🥊 {target.name} terkena {dmg} DMG dari {self.name}!")

        target.damage(dmg)

    def hool(self):
        heal_amount = 20
        self.heal(heal_amount)
        print(f"\n🔥 {self.name} menggunakan: 🩸 Evil Soul Devouring!")
        print(f"💚 {self.name} menerima +{heal_amount} HP!")

    def domain(self, target1, target2, target3):
        dmg = 40
        if self.rage:
            dmg += 20

        print(f"\n🌑 {self.name} membuka: DOMAIN SOUL CORRUPTION!")
        print(f"💀 Semua target terkena {dmg} DMG!")

        for target in (target1, target2, target3):
            target.damage(dmg)
