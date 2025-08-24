class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = Feature(
            feature_list={
                "power_on_off": [
                    {"step": 1, "actions": ["press_power_button", "press_and_hold_power_button"], "variable": "variable_power_on_off"}
                ],
                "start_pause": [
                    {"step": 1, "actions": ["press_start_pause_button", "press_and_hold_start_pause_button"], "variable": "variable_start_running", "comment": "value always set to either 'start' or 'pause'"}
                ],
                "adjust_program": [
                    {"step": 1, "actions": ["press_program_button"], "variable": "variable_program"}
                ],
                "adjust_water_level": [
                    {"step": 1, "actions": ["press_water_level_button"], "variable": "variable_water_level"}
                ],
                "adjust_wash_time": [
                    {"step": 1, "actions": ["press_wash_button"], "variable": "variable_washing_time"}
                ],
                "adjust_rinse_type": [
                    {"step": 1, "actions": ["press_rinse_button"], "variable": "variable_rinse_type"}
                ],
                "adjust_spin_time": [
                    {"step": 1, "actions": ["press_spin_button"], "variable": "variable_spin_time"}
                ],
                "delay_timer": [
                    {"step": 1, "actions": ["press_delay_timer_button"], "variable": "variable_delay_timer"}
                ],
                "null": [
                    {"step": 1, "actions": [], "missing_variables": []}
                ]
            },
            current_value=("empty", 1)
        )
        self.variable_power_on_off = variable_power_on_off
        self.variable_start_running = variable_start_running
        self.variable_program = variable_program
        self.variable_water_level = variable_water_level
        self.variable_washing_time = variable_washing_time
        self.variable_rinse_type = variable_rinse_type
        self.variable_spin_time = variable_spin_time
        self.variable_delay_timer = variable_delay_timer

    # Action: press_power_button
    # Effect: Toggles the power state between "on" and "off".
    def press_power_button(self):
        self.feature.update_progress("press_power_button")
        self.execute_action_and_set_next("press_power_button")

    # Action: press_and_hold_power_button
    # Effect: Toggles the power state between "on" and "off" with a hold duration of 1 second.
    def press_and_hold_power_button(self, duration=1):
        self.feature.update_progress("press_and_hold_power_button")
        if duration >= 1:
            self.execute_action_and_set_next("press_and_hold_power_button")

    # Action: press_start_pause_button
    # Effect: Toggles the start/pause state between "start" and "pause".
    def press_start_pause_button(self):
        self.feature.update_progress("press_start_pause_button")
        self.variable_start_running.set_current_value("start" if self.variable_start_running.get_current_value() == "pause" else "pause")

    # Action: press_and_hold_start_pause_button
    # Effect: Toggles the start/pause state between "start" and "pause" with a hold duration of 3 seconds.
    def press_and_hold_start_pause_button(self, duration=3):
        self.feature.update_progress("press_and_hold_start_pause_button")
        if duration >= 3:
            self.variable_start_running.set_current_value("start" if self.variable_start_running.get_current_value() == "pause" else "pause")

    # Action: press_program_button
    # Effect: Cycles through the available programs.
    def press_program_button(self):
        self.feature.update_progress("press_program_button")
        self.execute_action_and_set_next("press_program_button")

    # Action: press_water_level_button
    # Effect: Adjusts the water level within the range of 25 to 59 L.
    def press_water_level_button(self):
        self.feature.update_progress("press_water_level_button")
        self.execute_action_and_set_next("press_water_level_button")

    # Action: press_wash_button
    # Effect: Adjusts the washing time within the range of 3 to 18 minutes.
    def press_wash_button(self):
        self.feature.update_progress("press_wash_button")
        self.execute_action_and_set_next("press_wash_button")

    # Action: press_rinse_button
    # Effect: Cycles through the rinse types.
    def press_rinse_button(self):
        self.feature.update_progress("press_rinse_button")
        self.execute_action_and_set_next("press_rinse_button")

    # Action: press_spin_button
    # Effect: Adjusts the spin time within the range of 1 to 9 minutes.
    def press_spin_button(self):
        self.feature.update_progress("press_spin_button")
        self.execute_action_and_set_next("press_spin_button")

    # Action: press_delay_timer_button
    # Effect: Adjusts the delay timer within the range of 3 to 12 hours.
    def press_delay_timer_button(self):
        self.feature.update_progress("press_delay_timer_button")
        self.execute_action_and_set_next("press_delay_timer_button")

    # Run action with global condition checks
    def run_action(self, action_name, execution_times=1, **kwargs):
        # Execute the action
        return super().run_action(action_name, execution_times, **kwargs)