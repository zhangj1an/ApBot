# User manual: Press the On/Off (power symbol) button once and the function icons will light up. If there is no selection of function after pressing on/off button, the appliance will automatically switch off.
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Automatic Sterilize/Dry Function: Choose the drying time (after steam sterilization). 
# Press the Sterilize/Dry button 1 time for 30 minute dry time, 2 times for 45 minute dry time, 3 times for 60 minute dry time.
variable_dry_time = DiscreteVariable(value_range=["0", "30", "45", "60"], current_value="0")

# User manual: Sterilize only function: No additional adjustable variables since it only initiates sterilization.
# User manual: Dryer only function: Drying time is selected similarly as Automatic Sterilize/Dry Function.
# Press the Dry button 1 time for 30 minute dry time, 2 times for 45 minute dry time, 3 times for 60 minute dry time.
variable_dryer_only_time = DiscreteVariable(value_range=["0", "30", "45", "60"], current_value="0")