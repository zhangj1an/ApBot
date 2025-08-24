# Variable for power on/off
# User manual: Power On/Off - The power turns off automatically if you do not press “Start/Pause” within 10 minutes after power-on.
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Variable for start running
# User manual: 3. Start. - Press Start/Pause.
variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Variable for child lock
# User manual: Setting Child Lock - To prevent children from falling into the tub and drowning, if the lid is opened while the washing machine is operating, this function sounds a buzzer until it is closed.
variable_child_lock = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Variable for water level
# User manual: Change Water Level - During the wash process, press “Water Level” to change the water level.
variable_water_level = DiscreteVariable(
    value_range=["20 L", "29 L", "32 L", "37 L", "42 L", "55 L"],
    current_value="20 L"
)

# Variable for preset (timer)
# User manual: Preset - Set the time to finish washing (in hours).
variable_preset_timer = ContinuousVariable(value_ranges_steps=[(2, 24, 1)], current_value=2) # Defaults to 8 hours in example, but starting at 2 based on user manual specification.

# Variable for process setting (wash, rinse, spin)
# User manual: Wash / Rinse / Spin - According to your purpose, change the process settings.
variable_process_setting = DiscreteVariable(
    value_range=["wash", "rinse", "spin"],
    current_value="wash"
)

# Variable for program selection
# User manual: Programs - Variety of Programs allows selection from Normal, Delicate, Baby-care, etc.
variable_program_selection = DiscreteVariable(
    value_range=[
        "1 Normal",
        "2 Delicate",
        "3 Baby-care",
        "4 Fragrance",
        "5 Blanket",
        "6 Soak",
        "7 Energy Save (Speedy)",
        "8 Water Save",
        "9 Air Dry",
        "10 Tub Hygiene"
    ],
    current_value="1 Normal"
)