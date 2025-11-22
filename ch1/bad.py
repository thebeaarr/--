client1_nom = "ahmed"
client1_points = 10 
client1_email = "ahmed@gmail.com"


client2_nom = "Fatima"
client2_points = 25
client2_email = "fatima@gmail.com"

client1_points += 5
client2_points += 5


# les infos des clients 

def show_info(s: str ,  e: str ,  p : int):
	print(f"client name : {s} , client email : {e} , client points: {p}")



show_info(client1_nom , client1_email , client1_points)

show_info(client2_nom, client2_email , client2_points)
