# User manual: Tap the power button then tap the menu button until the sterilizer option appears. 
# User manual: Tap the power button to shut down the appliance. 
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# User manual: Tap the menu button to cycle through various function modes ("Quick", "Slow", "Defrost", "Sterilize", "Steam", "Preset"). 
variable_menu_index = DiscreteVariable(value_range=["Quick", "Slow", "Defrost", "Sterilize", "Steam", "Preset"], current_value="Quick")

# Place holder for menu setting. The actual variable will depend on the current menu index.
variable_menu_setting = None

# Quick function time setting (3 minutes default, adjustable with +/-)
variable_menu_setting_quick = ContinuousVariable(value_ranges_steps=[(0, 8, 1)], current_value=3)

# Slow function setting - LO and HI
variable_menu_setting_slow = DiscreteVariable(value_range=["LO", "HI"], current_value="LO")

# Defrost function time setting (adjustable per item size/temperature)
variable_menu_setting_defrost = ContinuousVariable(value_ranges_steps=[(0, 30, 1)], current_value=5)

# Sterilizer function time settings (10, 15, 20 minutes adjustable with +/-)
variable_menu_setting_sterilize = DiscreteVariable(value_range=["10", "15", "20"], current_value="15")

# Steam function time setting (default 12 minutes, adjustable using +/-)
variable_menu_setting_steam = ContinuousVariable(value_ranges_steps=[(0, 30, 1)], current_value=12)

# Preset function time setting (initiate functions at a future time, up to 15 hours adjustable in minutes using +/-)
variable_menu_setting_preset = ContinuousVariable(value_ranges_steps=[(0, 900, 1)], current_value=10)

# Mapping dictionary for menu settings
menu_setting_dict = {
    "Quick": variable_menu_setting_quick,
    "Slow": variable_menu_setting_slow,
    "Defrost": variable_menu_setting_defrost,
    "Sterilize": variable_menu_setting_sterilize,
    "Steam": variable_menu_setting_steam,
    "Preset": variable_menu_setting_preset
}