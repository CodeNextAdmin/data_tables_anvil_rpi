# data_tables_anvil_rpi
A demo raspberry Pi Anvil Server Project that talks to a data table module to store environmental data gathered by the Sense Hat.

This project requires an Anvil Project with a Data Tables module. The **raspi_data.py** script turns the Raspberry Pi into an Anvil Server that can connect to a data table on Anvil. 
The Anvil project todes not need to be running for the data table to be accesible.

## Requirements
1. A Raspberry Pi 3 or 4
2. A Sense HAT module
3. An Anvil account.

## Setting up Data Tables in Anvil

1. Go to [anvil.works](https://anvil.works) and sign up for a free account. 
2. Create a new project - Material Design theme is ok. The project doesn't need a front end to work, but one will be created for potential use. 
3. Read [documentation](https://anvil.works/docs/data-tables) to set up your Data Table.
   This project uses a data and time column, and three number columns to store the 
humidity, temperature and pressure read from the Sense HAT. After you have set it up, it should look like this. The columns can be in a different order.

 ![data](https://i.imgur.com/gA6wgYh_d.webp?maxwidth=1520&fidelity=grand)

4. Make sure that the table has permissions enabled for the Server (default).
5. Get and enable the [Uplink](https://anvil.works/docs/uplink) Key for the Server:

![Uplink](https://anvil.works/docs/uplink/img/uplink-dialog-location.png)

6. Clone this project on the Rasperry Pi.
7. Replace the Uplink key with yours.
8. Run the script. Adjust the time intervals between saving of data: sleep(10) to something else, if needed.

 
