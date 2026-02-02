class Hero:
    def __init__(self, name, job, hp,level,role):
        self.name = name
        self.job = job
        self.hp = hp
        self.level = level
        self.role = role
        print(f"✨ {self.name} [{self.role}] memasuki arena!")

    def __str__(self):
        status = "🟢 Hidup"
        if self.hp <= 0:
            status = "💀 Matek"

        return f"[  {self.name}  [{self.role}]  | HP: {self.hp} | STATUS : {status}]"
    
        

    def attack(self, enemy):
        damage = 15
        print(f"\n⚔️  {self.name} menyerang {enemy.name}!")
        enemy.damage(damage)
 
    def damage(self, damage):
       if self.hp <= 0:
        return

       self.hp -= damage
       print(f"🥊 {self.name} terkena {damage} Attack")

       if self.hp <= 0:
          self.hp = 0
          print(f"\n💀 {self.name} Telah Tereliminasi!")
          print(f"{self.name} Tidak Bisa Diserang Maupun Menyerang lagi\n")
        
    def heal(self, amount):
            self.hp += amount
           

    def critical(self,target):
         print(f"👿 anon terkena 0 DMG!")


#hayabusa = Hero(f"Hayabusa","Jungler",100)
#claude = Hero(f"Claude","Marksman",100)
#angela = Hero(f"Angela","Healer",100)