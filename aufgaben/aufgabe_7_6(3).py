import time 

added_time = int(input("Wie lange darf den Produckt ins Mikrowelle bleiben? (in Sekunden): "))
start_time = int(time.time())

end_time = (start_time + added_time) + 3600 * 2


time_std = int(end_time % 86400 / 3600)
time_min = int((end_time % 3600) / 60)
time_sec = int(end_time % 60)

print("Das Produkt wird um ", time_std, ":", time_min, ":", time_sec, "Uhr fertig sein.")




