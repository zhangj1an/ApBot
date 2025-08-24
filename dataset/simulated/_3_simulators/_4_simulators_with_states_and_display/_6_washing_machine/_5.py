# 9 variables

# User manual: 1 On/Off button - Product is switched On or Off.
variable_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# User manual: 2 Start/Pause button - Press the button to start or pause the washing cycle.
variable_start_running = DiscreteVariable(value_range=["start", "pause"], current_value="pause")

# User manual: 3 Program buttons - Available according to the laundry type.
variable_program = DiscreteVariable(value_range=["Regular", "Delicates", "Mixed", "Wool", "Heavy Duty", "Bedding", "Quick Wash", "Fuzzy weighting", "Free-cleaning function"], current_value="Regular")

# User manual: Water Level - Select water level according to clothing categories, degree of soiling and washing habits of customers.
variable_water_level = DiscreteVariable(value_range=["Low", "Mid", "High"], current_value="Low")

# User manual: Time Manager - Washing time, rinsing times, spinning time and other settings can be selectable.
variable_time_manager = ContinuousVariable(value_ranges_steps=[(0, 60, 1)], current_value=0)

# User manual: Rinse - Washing time, rinsing times, spinning time and other settings can be selectable.
variable_rinse = DiscreteVariable(value_range=["1 Time", "2 Times", "3 Times"], current_value="1 Time")

# User manual: Spin - Washing time, rinsing times, spinning time and other settings can be selectable.
variable_spin = DiscreteVariable(value_range=["Short", "Regular", "Long"], current_value="Short")

# User manual: Clean Tub Off - Free-cleaning function: when the tub is spinning, The strong water flow will scour the inner/outer tub and reduce the dirt residue. The machine has the free-cleaning function when start the machine. (Clean tub light is on), and press the tub clean button to turn off the function.
variable_clean_tub = DiscreteVariable(value_range=["on", "off"], current_value="on")

# User manual: Child Lock - To avoid operation of functions accidentally pressed by children
variable_child_lock = DiscreteVariable(value_range=["locked", "unlocked"], current_value="unlocked")

feature_list = {}

feature_list["turn_on_off"] = [
    {"step": 1, "actions": ["press_on_off_button"], "variable": "variable_on_off", "step_size": 2}
]

feature_list["start_pause"] = [
    {"step": 1, "actions": ["press_start_pause_button"], "variable": "variable_start_running", "step_size": 2}
]

feature_list["set_program"] = [
    {"step": 1, "actions": ["press_program_buttons"], "variable": "variable_program", "step_size": 9}
]

feature_list["set_water_level"] = [
    {"step": 1, "actions": ["press_water_level_button"], "variable": "variable_water_level", "step_size": 3}
]

feature_list["set_time_manager"] = [
    {"step": 1, "actions": ["press_time_manager_button"], "variable": "variable_time_manager", "step_size": 60}
]

feature_list["set_rinse"] = [
    {"step": 1, "actions": ["press_rinse_button"], "variable": "variable_rinse", "step_size": 3}
]

feature_list["set_spin"] = [
    {"step": 1, "actions": ["press_spin_button"], "variable": "variable_spin", "step_size": 3}
]

feature_list["clean_tub"] = [
    {"step": 1, "actions": ["press_clean_tub_off_button"], "variable": "variable_clean_tub", "step_size": 2}
]

feature_list["child_lock"] = [
    {"step": 1, "actions": ["press_and_hold_water_level_button_and_time_manager_button"], "variable": "variable_child_lock", "step_size": 2}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_on_off = variable_on_off
        self.variable_start_running = variable_start_running
        self.variable_program = variable_program
        self.variable_water_level = variable_water_level
        self.variable_time_manager = variable_time_manager
        self.variable_rinse = variable_rinse
        self.variable_spin = variable_spin
        self.variable_clean_tub = variable_clean_tub
        self.variable_child_lock = variable_child_lock

    def press_on_off_button(self):
        # Toggle the on/off state of the appliance
        self.feature.update_progress("press_on_off_button")
        self.execute_action_and_set_next("press_on_off_button")

    def press_start_pause_button(self):
        # Toggle the start/pause state of the washing cycle
        self.feature.update_progress("press_start_pause_button")
        self.execute_action_and_set_next("press_start_pause_button")

    def press_program_buttons(self):
        # Cycle through available programs
        self.feature.update_progress("press_program_buttons")
        self.execute_action_and_set_next("press_program_buttons")

    def press_water_level_button(self):
        # Cycle through water level settings
        self.feature.update_progress("press_water_level_button")
        self.execute_action_and_set_next("press_water_level_button")

    def press_time_manager_button(self):
        # Adjust the time manager setting
        self.feature.update_progress("press_time_manager_button")
        self.execute_action_and_set_next("press_time_manager_button")

    def press_rinse_button(self):
        # Cycle through rinse settings
        self.feature.update_progress("press_rinse_button")
        self.execute_action_and_set_next("press_rinse_button")

    def press_spin_button(self):
        # Cycle through spin settings
        self.feature.update_progress("press_spin_button")
        self.execute_action_and_set_next("press_spin_button")

    def press_clean_tub_off_button(self):
        # Toggle the clean tub function
        self.feature.update_progress("press_clean_tub_off_button")
        self.execute_action_and_set_next("press_clean_tub_off_button")

    def press_and_hold_water_level_button_and_time_manager_button(self, duration=3):
        # Toggle the child lock feature if held for 3 seconds
        self.feature.update_progress("press_and_hold_water_level_button_and_time_manager_button")
        if duration >= 3:
            self.execute_action_and_set_next("press_and_hold_water_level_button_and_time_manager_button")