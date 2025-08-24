# 8 variables

# User manual: Press this button to switch power on and off.
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# User manual: Starts and pauses operation.
variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")

# User manual: The delay time can be set between 3 and 12 hours.
variable_delay_time = ContinuousVariable(value_ranges_steps=[(0, 3, 3), (3, 12, 1)], current_value=0)

# User manual: Changes the spin time. The spin time can be set between one and 9 minutes.
variable_spin_time = ContinuousVariable(value_ranges_steps=[(0, 1, 1), (1, 9, 1)], current_value=0)

# User manual: Changes the number and type of rinses.
variable_rinse_type = DiscreteVariable(value_range=["Normal Rinse 2 times",
"Water-Injection Rinse 2 times",
"no rinsing", "Normal Rinse 1 time",
"Water-Injection Rinse 1 time"], current_value="no rinsing")

# User manual: Changes the washing time. The washing time can be set between 3 and 18 minutes.
variable_wash_time = ContinuousVariable(value_ranges_steps=[(0, 3, 3), (3, 18, 1)], current_value=0)

# User manual: Changes the water level.
variable_water_level = DiscreteVariable(value_range=["59 L", "50 L", "40 L", "35 L", "30 L", "25 L (Auto)"], current_value="25 L (Auto)")

# User manual: Selects programs. The program changes each time the button is pressed.
variable_program = DiscreteVariable(value_range=["P1. Fuzzy", "P2. Powerful", "P3. Speedy", "P4. Fragrance", "P5. Soak", "P6. Tub Clean", "P7. Water Save", "P8. Energy Save", "P9. Small Load"], current_value="P1. Fuzzy")

feature_list = {}

feature_list["turn_on_off"] = [
    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off", "step_size": 2}
]

feature_list["start_pause"] = [
    {"step": 1, "actions": ["press_start_pause_button"], "variable": "variable_start_running", "step_size": 2}
]

feature_list["set_delay_time"] = [
    {"step": 1, "actions": ["press_delay_timer_button"], "variable": "variable_delay_time", "step_size": 10}
]

feature_list["set_spin_time"] = [
    {"step": 1, "actions": ["press_spin_button"], "variable": "variable_spin_time", "step_size": 10}
]

feature_list["set_rinse_type"] = [
    {"step": 1, "actions": ["press_rinse_button"], "variable": "variable_rinse_type", "step_size": 4}
]

feature_list["set_wash_time"] = [
    {"step": 1, "actions": ["press_wash_button"], "variable": "variable_wash_time", "step_size": 17}
]

feature_list["set_water_level"] = [
    {"step": 1, "actions": ["press_water_level_button"], "variable": "variable_water_level", "step_size": 6}
]

feature_list["select_program"] = [
    {"step": 1, "actions": ["press_program_button"], "variable": "variable_program", "step_size": 9}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_power_on_off = variable_power_on_off
        self.variable_start_running = variable_start_running
        self.variable_delay_time = variable_delay_time
        self.variable_spin_time = variable_spin_time
        self.variable_rinse_type = variable_rinse_type
        self.variable_wash_time = variable_wash_time
        self.variable_water_level = variable_water_level
        self.variable_program = variable_program

    def press_power_button(self):
        # This action toggles the power on/off
        self.feature.update_progress("press_power_button")
        self.execute_action_and_set_next("press_power_button")

    def press_start_pause_button(self):
        # This action starts or pauses the washing machine
        self.feature.update_progress("press_start_pause_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "start_pause":
            self.variable_start_running.set_current_value("on")

    def press_delay_timer_button(self):
        # This action sets the delay time
        self.feature.update_progress("press_delay_timer_button")
        self.execute_action_and_set_next("press_delay_timer_button")

    def press_spin_button(self):
        # This action sets the spin time
        self.feature.update_progress("press_spin_button")
        self.execute_action_and_set_next("press_spin_button")

    def press_rinse_button(self):
        # This action sets the rinse type
        self.feature.update_progress("press_rinse_button")
        self.execute_action_and_set_next("press_rinse_button")

    def press_wash_button(self):
        # This action sets the wash time
        self.feature.update_progress("press_wash_button")
        self.execute_action_and_set_next("press_wash_button")

    def press_water_level_button(self):
        # This action sets the water level
        self.feature.update_progress("press_water_level_button")
        self.execute_action_and_set_next("press_water_level_button")

    def press_program_button(self):
        # This action selects the washing program
        self.feature.update_progress("press_program_button")
        self.execute_action_and_set_next("press_program_button")