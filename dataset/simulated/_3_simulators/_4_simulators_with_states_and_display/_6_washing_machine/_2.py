# 7 variables

# Variable for power on/off
# User manual: Press the ON/OFF button to power your wash on.
variable_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Variable for start/pause
variable_start_running = DiscreteVariable(value_range=["start", "pause"], current_value="pause")

# Variable for washing program
variable_washing_program = DiscreteVariable(value_range=["Heavy", "Gentle", "Normal", "Rapid", "Soak"], current_value="Heavy")

# Variable for load size
variable_load_size = DiscreteVariable(value_range=["1", "2", "3"], current_value="1")

# Variable for washing time
variable_wash_time = ContinuousVariable(value_ranges_steps=[(0, 1, 1), (1, 20, 1)], current_value=0)

# Variable for rinse times
variable_rinse_times = ContinuousVariable(value_ranges_steps=[(0, 1, 1), (1, 3, 1)], current_value=0)

# Variable for spin time
variable_spin_time = ContinuousVariable(value_ranges_steps=[(0, 3, 3), (3, 9, 1)], current_value=0)

feature_list = {}

feature_list["turn_on_off"] = [
    {"step": 1, "actions": ["press_on_off_button"], "variable": "variable_on_off", "step_size": 2}
]

feature_list["select_washing_program"] = [
    {"step": 1, "actions": ["press_program_button"], "variable": "variable_washing_program", "step_size": 5}
]

feature_list["set_load_size"] = [
    {"step": 1, "actions": ["press_load_size_button"], "variable": "variable_load_size", "step_size": 3}
]

feature_list["set_wash_time"] = [
    {"step": 1, "actions": ["press_wash_button"], "variable": "variable_wash_time", "step_size": 21}
]

feature_list["set_rinse_times"] = [
    {"step": 1, "actions": ["press_rinse_button"], "variable": "variable_rinse_times", "step_size": 4}
]

feature_list["set_spin_time"] = [
    {"step": 1, "actions": ["press_spin_button"], "variable": "variable_spin_time", "step_size": 7}
]

feature_list["start_pause_cycle"] = [
    {"step": 1, "actions": ["press_start_pause_button"], "variable": "variable_start_running", "step_size": 2}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_on_off = variable_on_off
        self.variable_start_running = variable_start_running
        self.variable_washing_program = variable_washing_program
        self.variable_load_size = variable_load_size
        self.variable_wash_time = variable_wash_time
        self.variable_rinse_times = variable_rinse_times
        self.variable_spin_time = variable_spin_time

    def press_on_off_button(self):
        # This action toggles the power state of the appliance.
        self.feature.update_progress("press_on_off_button")
        self.execute_action_and_set_next("press_on_off_button")

    def press_program_button(self):
        # This action cycles through the washing programs.
        self.feature.update_progress("press_program_button")
        self.execute_action_and_set_next("press_program_button")

    def press_load_size_button(self):
        # This action cycles through the load sizes.
        self.feature.update_progress("press_load_size_button")
        self.execute_action_and_set_next("press_load_size_button")

    def press_wash_button(self):
        # This action adjusts the wash time.
        self.feature.update_progress("press_wash_button")
        self.execute_action_and_set_next("press_wash_button")

    def press_rinse_button(self):
        # This action adjusts the rinse times.
        self.feature.update_progress("press_rinse_button")
        self.execute_action_and_set_next("press_rinse_button")

    def press_spin_button(self):
        # This action adjusts the spin time.
        self.feature.update_progress("press_spin_button")
        self.execute_action_and_set_next("press_spin_button")

    def press_start_pause_button(self):
        # This action toggles the start/pause state of the appliance.
        self.feature.update_progress("press_start_pause_button")
        self.execute_action_and_set_next("press_start_pause_button")