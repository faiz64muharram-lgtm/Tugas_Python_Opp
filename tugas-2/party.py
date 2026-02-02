from fighter import Fighter
from assasint import Assasint
from tank import Tank
from detian import Iblis
from goblin import Goblin





print('\n== SUMMON SEMUA DOULUO ==\n')
Yuhou = Fighter("Yuhou","Spy",100,70,)
Donger = Assasint("Dong'er","Light",100,67)
Sanshi = Tank("Xu Sanshi","Control",150,50)


print("\n🚨 PERINGATAN! Para goblin muncul! \n")

goblin_1 =Goblin("Goblin Ijo","kroco",60,60,10)
goblin_2 =Goblin("Goblin Ungu","kroco",60,60,10)
goblin_3 =Goblin("Goblin Pink","kroco",60,60,10)

print("\n⚔️  ---RAID DIMULAI--- ⚔️\n")
Yuhou.attack(goblin_2)

Sanshi.shield(Yuhou)

goblin_1.critical(Sanshi)

Donger.critical(goblin_1)

goblin_2.critical(Donger)

goblin_3.critical(Donger)
Sanshi.shield(Donger)
Yuhou.critical(goblin_1)
goblin_2.attack(Yuhou)
goblin_3.critical(Yuhou)
Yuhou.attack(goblin_3)
goblin_3.critical(Sanshi)
goblin_2.attack(Sanshi)
Donger.critical(goblin_3)
Donger.critical(goblin_2)
print ("\nYuhou : Aku akan menyelesaikan semuanya\n")
Yuhou.critical(goblin_3)
Yuhou.critical(goblin_2)

print("=== Detian: “Kematian para Goblin telah membangunkanku.” ===")
print("=== PERINGATAN RAJA IBLIS TELAH MUNCUL! ===")
detian=Iblis("Detian","RajaIblis",300,300,99)

detian.critical(Yuhou)
Sanshi.shield(Yuhou)
Donger.critical(detian)
Sanshi.shield(Yuhou)
Yuhou.critical(detian)
detian.critical(Donger)
Sanshi.critical(detian)
Donger.critical(detian)
detian.critical(Sanshi)
Donger.critical(detian)
Yuhou.attack(detian)
print(f"\n== 👹 Detian Masuk Rage Mode ==\n")
detian.domain(Yuhou,Sanshi,Donger)
print("\n=== Detian: HAhaha Manusia Sampah ===\n")
print("\n=== Yuhou: Dasar raja iblis Bajing**n ===\n")
print("\n=== 😈 Yuhou Masuk Asura Mode  ===\n")
Yuhou.ulti(detian)
print("\n=== Detian: Haa!,Kenapa Bisa Kau Sekuat Ini ? ===\n")
Yuhou.final(detian)





   




print("\n== Status Raid Hero ==\n")
print(Yuhou)
print(Donger)
print(Sanshi)

print("\n== Status Raid Monster ==\n")
print(goblin_1)
print(goblin_2)
print(goblin_3)
print("\n== Status Raid Raja Iblis ==\n")
print(detian)