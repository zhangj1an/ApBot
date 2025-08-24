# variable for power on/off control
# User manual: Press and hold the "Power" button for 3 seconds to turn on the Bottle Washer Pro®.
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# variable for starting the appliance
# User manual: Press the “Start/Pause” button to start the Bottle Washer Pro®.
variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")

# variable for wash mode selection
# User manual: Touch the “wash mode” button to choose a wash cycle.
variable_wash_mode = DiscreteVariable(
    value_range=["Wash & Dry", "Wash, Sterilize, Dry", "Wash Only"],
    current_value="Wash & Dry"
)

# variable for sterilize and dry modes
# User manual:
# Sterilize & Dry: Touch the Sterilize-Dry button 1 time, then press the Start/Pause button to start.
# Dry Only: Touch the Sterilize-Dry button 2 times, then press the Start/Pause button to start.
# Sterilize Only: Touch the Sterilize-Dry button 3 times, then press the Start/Pause button to start.
variable_sterilize_dry_mode = DiscreteVariable(
    value_range=["Sterilize & Dry", "Dry Only", "Sterilize Only"],
    current_value="Sterilize & Dry"
)