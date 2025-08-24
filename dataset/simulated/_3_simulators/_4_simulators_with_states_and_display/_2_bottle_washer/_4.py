# 10 variables

# Variable for power on/off
# User manual: Tap the power button to turn on the machine.
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Variable for menu selection
variable_menu_index = DiscreteVariable(value_range=["quick", "slow", "defrost", "sterilize", "steam", "preset"], current_value="quick")

# Variable for quick warm time
variable_quick_warm_time = ContinuousVariable(value_ranges_steps=[(0, 10, 1)], current_value=3)

# Variable for slow warm setting
variable_slow_warm_setting = DiscreteVariable(value_range=["LO", "HI"], current_value="LO")

# Variable for defrost time
variable_defrost_time = ContinuousVariable(value_ranges_steps=[(0, 10, 1)], current_value=0)

# Variable for sterilize time
variable_sterilize_time = ContinuousVariable(value_ranges_steps=[(0, 10, 10), (10, 20, 5)], current_value=15)

# Variable for steam time
variable_steam_time = ContinuousVariable(value_ranges_steps=[(0, 12, 12), (12, 25, 1)], current_value=12)

# Variable for preset time
variable_preset_time = DiscreteVariable(value_range=["1 hr", "2 hrs", "3 hrs", "4 hrs", "5 hrs", "10 hrs", "15 hrs"], current_value="1 hr")

# Note: Each time an action is made to adjust variable_menu_index, the corresponding time variable will be set from the dictionary.
menu_time_dict = {
    "quick": variable_quick_warm_time,
    "slow": variable_slow_warm_setting,
    "defrost": variable_defrost_time,
    "sterilize": variable_sterilize_time,
    "steam": variable_steam_time,
    "preset": variable_preset_time
}

variable_menu_time = None # This variable will be set to the corresponding time variable based on the selected menu.

feature_list = {}

feature_list["turn_on_off"] = [
    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off", "step_size": 2}
]

feature_list["menu"] = [
    {"step": 1, "actions": ["press_menu_button"], "variable": "variable_menu_index", "step_size": 6}, 
    {"step": 2, "actions": ["press_plus_button", "press_minus_button"], "variable": "variable_menu_time", "step_size": 14}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_power_on_off = variable_power_on_off
        self.variable_menu_index = variable_menu_index
        self.variable_quick_warm_time = variable_quick_warm_time
        self.variable_slow_warm_setting = variable_slow_warm_setting
        self.variable_defrost_time = variable_defrost_time
        self.variable_sterilize_time = variable_sterilize_time
        self.variable_steam_time = variable_steam_time
        self.variable_preset_time = variable_preset_time
        self.menu_time_dict = menu_time_dict
        self.variable_menu_time = None

    def press_power_button(self):
        # Update feature and set power on/off
        self.feature.update_progress("press_power_button")
        self.variable_power_on_off.set_current_value("on" if self.variable_power_on_off.get_current_value() == "off" else "off")

    def press_menu_button(self):
        # Update feature and set menu index
        self.feature.update_progress("press_menu_button")
        self.execute_action_and_set_next("press_menu_button")
        # Set the corresponding time variable based on the selected menu
        self.variable_menu_time = self.menu_time_dict[self.variable_menu_index.get_current_value()]

    def press_plus_button(self):
        # Update feature and increase the time or setting
        self.feature.update_progress("press_plus_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "menu":
            self.execute_action_and_set_next("press_plus_button")

    def press_minus_button(self):
        # Update feature and decrease the time or setting
        self.feature.update_progress("press_minus_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "menu":
            self.execute_action_and_set_prev("press_minus_button")



