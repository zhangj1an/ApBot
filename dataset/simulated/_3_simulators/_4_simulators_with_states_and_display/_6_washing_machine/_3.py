# 6 variables

# User manual: The power turns off automatically if you do not press “Start/Pause” within 10 minutes after power-on.
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")

variable_child_lock = DiscreteVariable(value_range=["on", "off"], current_value="off")

variable_program = DiscreteVariable(
    value_range=[
        "1 Normal", "2 Delicate", "3 Baby-care", "4 Fragrance", 
        "5 Blanket", "6 Soak", "7 Energy Save (Speedy)", 
        "8 Water Save", "9 Air Dry", "10 Tub Hygiene"
    ], 
    current_value="1 Normal"
)

variable_water_level = DiscreteVariable(
    value_range=["55 L", "42 L", "37 L", "32 L", "29 L", "20 L"], 
    current_value="55 L"
)

variable_preset = ContinuousVariable(
    value_ranges_steps=[(0, 2, 2), (2, 24, 1)], 
    current_value=0
)

feature_list = {}

feature_list["turn_on_off"] = [
    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off", "step_size": 2}
]

feature_list["start_pause"] = [
    {"step": 1, "actions": ["press_start_pause_button"], "variable": "variable_start_running", "step_size": 2}
]

feature_list["program_selection"] = [
    {"step": 1, "actions": ["press_program_button"], "variable": "variable_program", "step_size": 10}
]

feature_list["water_level_selection"] = [
    {"step": 1, "actions": ["press_water_level_button"], "variable": "variable_water_level", "step_size": 6}
]

feature_list["preset_time"] = [
    {"step": 1, "actions": ["press_preset_button"], "variable": "variable_preset", "step_size": 24}
]

feature_list["process_selection"] = [
    {"step": 1, "actions": ["press_process_button"]}
]

feature_list["child_lock"] = [
    {"step": 1, "actions": ["press_and_hold_program_button"], "variable": "variable_child_lock", "step_size": 2}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_power_on_off = variable_power_on_off
        self.variable_start_running = variable_start_running
        self.variable_child_lock = variable_child_lock
        self.variable_program = variable_program
        self.variable_water_level = variable_water_level
        self.variable_preset = variable_preset

    def press_power_button(self):
        # Update feature progress and set power to "on" or "off"
        self.feature.update_progress("press_power_button")
        self.variable_power_on_off.set_current_value("on" if self.variable_power_on_off.get_current_value() == "off" else "off")

    def press_start_pause_button(self):
        # Update feature progress and set start to "on" or "off"
        self.feature.update_progress("press_start_pause_button")
        self.variable_start_running.set_current_value("on" if self.variable_start_running.get_current_value() == "off" else "off")

    def press_program_button(self):
        # Update feature progress and change the program to the next one
        self.feature.update_progress("press_program_button")
        self.execute_action_and_set_next("press_program_button")

    def press_water_level_button(self):
        # Update feature progress and change the water level to the next one
        self.feature.update_progress("press_water_level_button")
        self.execute_action_and_set_next("press_water_level_button")

    def press_preset_button(self):
        # Update feature progress and change the preset time to the next one
        self.feature.update_progress("press_preset_button")
        self.execute_action_and_set_next("press_preset_button")

    def press_process_button(self):
        # Update feature progress for process selection
        self.feature.update_progress("press_process_button")
    
    def press_and_hold_program_button(self, duration = 5):
        # Update feature progress and set child lock to "on" or "off"
        self.feature.update_progress("press_and_hold_program_button")
        self.variable_child_lock.set_current_value("on" if self.variable_child_lock.get_current_value() == "off" else "off")

    def run_action(self, action_name, execution_times=1, **kwargs):
        
        # Check if child lock is on, only allow power and unlock actions
        if self.variable_child_lock.get_current_value() == "on" and all(item not in action_name for item in ["press_power_button"]):
            self.display = "child lock: locked"
            return self.display

        # Execute the action
        return super().run_action(action_name, execution_times, **kwargs)