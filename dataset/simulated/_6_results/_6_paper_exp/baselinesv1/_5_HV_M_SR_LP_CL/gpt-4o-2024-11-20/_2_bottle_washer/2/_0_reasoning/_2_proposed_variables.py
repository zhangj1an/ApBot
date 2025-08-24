# User manual: **ON/OFF:** Press this button to turn on the appliance and the light is on. Press again to turn it off and the light is off.
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# User manual: **Night light:** Long press the power button to turn on/off the night light. (Night light can be controlled separately at any time)
variable_night_light = DiscreteVariable(value_range=["on", "off"], current_value="off")

# User manual: | Select bottle | Select initial temp       | Select Volume |
#              |---------------|---------------------------|---------------|
#              | Milk bag      | Room- 25℃ (77℉)           | 1-3 fl- oz    |
#              | Plastic       | Refrig- 4℃ (39.2℉)        | 4-6 fl- oz    |
#              | Silicone      | Frozen- 0℃ (32℉)          | 7+ fl- oz     |
variable_bottle_type = DiscreteVariable(value_range=["Milk bag", "Plastic", "Silicone"], current_value="Milk bag")
variable_initial_temp = DiscreteVariable(value_range=["Room", "Refrig", "Frozen"], current_value="Room")
variable_volume = DiscreteVariable(value_range=["1-3 fl-oz", "4-6 fl-oz", "7+ fl-oz"], current_value="1-3 fl-oz")

# User manual: 3. Press the power button after selection and the device will start warming.
variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")