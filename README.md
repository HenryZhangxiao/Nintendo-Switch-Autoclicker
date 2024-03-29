<h1 align="center">
    Nintendo Switch Autoclicker
  <br>
  <br>
  <p align="center">
  	<img width="460" height="300" src="https://github.com/HenryZhangxiao/Nintendo-Switch-Autoclicker/assets/44578113/db2f95d4-fd33-46fc-ba87-3bb69a6c39f9">
	</p>
</h1>

## Introduction

An autoclicker program designed to work with a Micro Servo and run on a Raspberry Pi.

The inspiration for this project comes from the tiresome methods needed to accumulate money in Pokémon Violet. To construct a viable competitive team, millions of in-game currency is required but each battle only yields approximately 20-30k, ergo the need for some kind of automated process.

A more in-depth explanation of the game strategy used for this project can be found [below](#explanation) if it interests you


#### Table of Contents
- [Technologies Used ](#technologies)
- [At a Glance ](#glance)
- [See it in Action ](#demo)
- [Let it Run ](#let-it-run)
- [How to Run ](#run)
- [Game Mechanics explanation ](#explanation)
- [Copyright ](#copyright)


<br></br>
## Technologies Used <a name="technologies"></a>
- Raspberry Pi 3 - Model A+
- Raspberry Pi OS (32-bit) (Debian distro)
- TowerPro SG91R - Micro Servo
- 3D Printer (Thanks [@The-OnlyBirdman](https://github.com/The-OnlyBirdman)!)
  - Used to print a Micro Servo case for the Nintendo Switch controller
  - Printables file can be found [here](https://www.printables.com/model/138284-nintedo-switch-auto-clicker)
  - Note: This project used `A-Masher_Case_Corded.stl` but if you are using an external battery to power your servo, you may wish to use `A5-Masher_Case_Battery.stl` instead
- Nintendo Switch
- Python3
- gpiozero
- Thonny
- Git


<br></br>
## At a Glance <a name="glance"></a>
<img width=50% height=50% src="https://github.com/HenryZhangxiao/Nintendo-Switch-Autoclicker/assets/44578113/62176d68-95c1-4b6d-a579-fc4fa262ee20">

- 9g Micro Servo with jumper cables attached to the 5V Power, Ground, and GPIO PWM pins
- Servo drilled in to case using 2x M3 screws


<br></br>
## See it in Action <a name="demo"></a>
- Running with an `INTERVAL` of 8 seconds as obtained from a run with `IntervalTester.py`

https://github.com/HenryZhangxiao/Nintendo-Switch-Autoclicker/assets/44578113/d9044a19-65af-4c9e-98bf-4dac29bfc831


<br></br>
## Let it Run <a name="let-it-run"></a>
- Now that we know the program and hardware work as intended, all that's left is to dock the switch and leave it running overnight

<img width=50% height=50% src="https://github.com/HenryZhangxiao/Nintendo-Switch-Autoclicker/assets/44578113/793a36ac-8559-4b1b-a044-9db7e88eaf7e">

<br></br>
- So that we go from $300,000
<img width=50% height=50% src="https://github.com/HenryZhangxiao/Nintendo-Switch-Autoclicker/assets/44578113/1f9bc1a0-4b86-4ca3-8e4b-113c8e49d3d9">

<br></br>
- To $3,000,000
<img width=50% height=50% src="https://github.com/HenryZhangxiao/Nintendo-Switch-Autoclicker/assets/44578113/aff75ca0-317f-483a-b82a-cffc3d28cb62">


<br></br>
## How to Run <a name="run"></a>
- Clone this GitHub repo
- To run IntervalTester.py
  - `python3 IntervalTester.py`
  - Press `Enter` every time you click the 'A' button
  - Input `Q` or `q` when you are finished an iteration
  - After quitting, the program will print out the fastest, slowest, and average time between button presses
- To run ServoController.py
  - Pre-requisites
    - Micro Servo set up and pins connected to Raspberry Pi
    - NOTE: Check the pin layout for your Raspberry Pi. The default GPIO Pin# being used in this program is 18 which corresponds to my PWM data pin. If your data pin is different, change the `GPIO_DATA_PIN` variable accordingly. If you are unsure what number your data pin is, just keep as default and only change if the program throws an error
    - NOTE: If you don't use some sort of Micro Servo printed case like the one detailed, you must find some way to properly secure the Servo as it produces more torque than you would think
  - `sudo pigpiod` to launch the pigpio library as a daemon
  - (Optional) Edit the `INTERVAL` definition to the average button press timing obtained from `IntervalTester.py`
  - `python3 ServoController.py` to run the main program or run with command line argument `c` or `calibrate` to quickly determine the min, mid, and max angles of the servo. (Used to determine if pulse widths are satisfactory)
- If all goes well... congrats! You just managed to accomplish what a turbo controller does for only 3x the price! But wasn't that rewarding?


<br></br>
## Game Mechanics Explanation <a name="explanation"></a>
- Pokémon Violet reintroduces the purchasable vitamins feature from previous games and as such, creates a somewhat artificial demand for in-game currency to create viable competitive teams
- Pokémon Violet lacks easy ways to farm said in-game currency in comparison to previous games, and as such, requires the player to put in tens to hundreds of real-time hours to construct a single competitive team
- This "AFK" method revolves around the fact that the "Academy Ace Tournament" has the potential to go infinite bar extremely unlikely chance based events during battles
- We can abuse the tournament by only having one pokémon in our party with only one usable move and continuously pressing the 'A' button. If done correctly with no RNG to disrupt this process, this method can go on infinitely


<br></br>
### Copyright <a name="copyright"></a>
Pokémon Scarlet and Pokémon Violet by Game Freak Inc.

This project was created privately for educational purposes only with no intent to distribute.

All game content, mechanics, media, and all other game components belong to Nintendo, The Pokémon Company, Game Freak Inc. and their rightful owners.
