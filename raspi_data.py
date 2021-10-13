import anvil.server
from anvil.tables import app_tables
from sense_hat import SenseHat
from time import sleep
from datetime import datetime

sense = SenseHat()
 
 
anvil.server.connect("<Add your Connect ID here>")
#anvil.server.connect(ANVIL_CONNECT_SECRET)

@anvil.server.callable
def get_env_data():
    
    humidity = sense.get_humidity()
    temperature = sense.get_temperature()
    pressure = sense.get_pressure()
    
    data = {
        "h":humidity,
        "t": temperature,
        "p": pressure
        
        }
    return data

@anvil.server.callable
def save_data():
    
    data = get_env_data()
    t = data["t"]
    h = data["h"]
    p = data["p"]
    dt = datetime.now()
    
    new_row = app_tables.env_data.add_row(datetime=dt,
                                          temperature=t,
                                          humidity=h,
                                          pressure=p)
    
    print(new_row)
    
    
    

while True:
    save_data()
    sleep(10)
