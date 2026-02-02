from hero import Hero

class Fighter (Hero):
    def __init__(self, name, job, hp, level,):
        super().__init__(name, job, hp, level,role="Fighter")


    def critical(self, target):
        dmg = 30
        print (f"\n🔥 {self.name} menggunakan: ❄️ Extreme Ice !")
        print(f"🥊 {target.name} terkena critical {dmg} DMG dari {self.name}!")

     
        target.damage(dmg)


    def ulti(self, target):
        dmg = 70
        print (f"\n🌑 {self.name} menggunakan: 👁️ Tatapan kehancuran !")
        print(f"🥊 {target.name} terkena tatapan kehancuran {dmg} DMG dari {self.name} (Asura Mode) !")

     
        target.damage(dmg)

    def final(self, target):
        dmg = 70
        print(f"=== 🟣 {self.name}: Masuk lah Kedalam Kehampaan Dasar Iblis Neraka 🟣 ===")
        print (f"\n🌑 {self.name} menggunakan: 💀 Kehancuran Abadi !")
        print(f"💀 {target.name} tenggelam dalam kehancuran abadi dari {self.name} (Asura Mode) 🟣!")
        
     
        target.damage(dmg)