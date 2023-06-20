<h1 align="center">
    Nintendo Switch Autoclicker
  <br>
  <br>
  <p align="center">
  	<img width="460" height="300" src="https://github.com/HenryZhangxiao/Nintendo-Switch-Autoclicker/assets/44578113/a427111a-c4b1-4f48-a903-b53bae13095e">
	</p>
</h1>

## Introduction

An autoclicker program designed to work with a Micro Servo and run on a Raspberry Pi.

The inspiration for this project comes from the tiresome methods needed to accumulate money in Pokémon Violet. To construct a viable competitive team, millions of in-game currency is required but each battle only yields approximately 20-30k, ergo the need for some kind of automated process.

A more in-depth explanation of the game strategy used for this project can be found [below](#explanation) if it interests you


#### Table of Contents
- [Technologies used ](#technologies)
- [At a Glance ](#glance)
- [Final iteration of the game (April 8): Demo ](#final-iteration-of-the-game-april-8-demo-)
- [Game Mechanics explanation ](#explanation)
- [How to Run ](#run)
- [Copyright ](#copyright)


<br></br>
## Technologies used <a name="technologies"></a>
- Raspberry Pi 3 - Model A+
- Raspberry Pi OS (32-bit) (Debian distro)
- TowerPro SG91R - Micro Servo
- 3D Printer (Thanks @The-OnlyBirdman !)
  - Used to print a Micro Servo case for the Nintendo Switch controller
  - Printables file can be found [here](https://www.printables.com/model/138284-nintedo-switch-auto-clicker)
  - Note: This project used `A-Masher_Case_Corded.stl` but if you are using an external battery to power your servo, you may wish to use `A5-Masher_Case_Battery.stl` instead
- Nintendo Switch
- gpiozero
- Thonny
- Git


<br></br>
## At a Glance <a name="glance"></a>
<img width=50% height=50% src="https://github.com/HenryZhangxiao/Nintendo-Switch-Autoclicker/assets/44578113/df31971a-466e-4af8-88bd-60c3ac60d445">

- 2 to 4 players can join the game and take turns discarding cards and taking new ones
- The UI also allows each player to:
	- See their current cards and select some for discarding
	- Get new cards into their hand
	- See the cards discarded by other players

[PIC HERE]


<br></br>
## Final iteration of the game (April 8): [Demo](https://www.youtube.com/watch?v=jWEatQwQw0E) <a name="final"></a>
- The game is augmented with amours and allies
- Mordred as able to kill an ally


<br></br>
## Game Mechanics Explanation <a name="explanation"></a>
- Pokémon Violet reintroduces the purchasable vitamins feature from previous games and as such, creates a somewhat artificial demand for in-game currency to create viable competitive teams
- Pokémon Violet lacks easy ways to farm said in-game currency in comparison to previous games, and as such, requires the player to put in tens to hundreds of real-time hours to construct a single competitive team
- This "AFK" method revolves around the fact that the "Academy Ace Tournament" has the potential to go infinite bar extremely unlikely chance based events during battles
- We can abuse the tournament by only having one pokémon in our party with only one usable move and continuously pressing the 'A' button. If done correctly with no RNG to disrupt this process, this method can go on infinitely


<br></br>
## How to Run <a name="run"></a>
- Clone this GitHub repo
- To run IntervalTester.py
  - `python3 IntervalTester.py`
  - Press `Enter` every time you click the 'A' button
  - Press `Q` or `q` when you are finished an iteration
  - After quitting, the program will print out the fastest, slowest, and average time between button presses
- To run ServoController.py
  - Pre-requisites
    - Micro Servo set up and pins connected to Raspberry Pi
    - NOTE: Check the pin layout for your Raspberry Pi. The default GPIO Pin# being used in this program is 18 which corresponds to my PWM data pin. If your data pin is different, change the `GPIO_DATA_PIN` variable accordingly. If you are unsure what number your data pin is, just keep as default and only change if the program throws an error
    - NOTE: If you don't use some sort of Micro Servo printed case like the one detailed, you must find some way to properly secure the Servo as it produces more torque than you would think
  - `sudo pigpiod`
  - (Optional) Edit the INTERVAL definition to the average button press obtained from `IntervalTester.py`
  - `python3 ServoController.py` to run the main program or run with command line argument `c` or `calibrate` to quickly determine the min, mid, and max angles of the servo. (Used to determine if pulse widths are satisfactory)


<br></br>
### Copyright <a name="copyright"></a>
Pokémon Scarlet and Pokémon Violet by Game Freak Inc.

This project was created privately for educational purposes only with no intent to distribute.

All game content, mechanics, media, and all other game components belong to Nintendo, The Pokémon Company, Game Freak Inc. and their rightful owners.
