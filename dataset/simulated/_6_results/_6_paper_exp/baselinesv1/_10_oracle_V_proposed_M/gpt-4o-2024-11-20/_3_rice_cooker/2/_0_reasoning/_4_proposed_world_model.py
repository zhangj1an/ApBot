class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = Feature(
            feature_list={
                "start_running": [
                    {"step": 1, "actions": ["press_start_button"], "variable": "variable_start_running", "comment": "value always set to 'on'"}
                ],
                "set_cooking_mode": [
                    {"step": 1, "actions": ["press_menu_cancel_button"], "variable": "variable_cooking_mode"}
                ],
                "set_preset_timer": [
                    {"step": 1, "actions": ["press_preset_time_time_button"], "variable": "variable_preset_timer"}
                ],
                "null": [
                    {"step": 1, "actions": [], "missing_variables": []}
                ]
            },
            current_value=("empty", 1)
        )
        self.variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_cooking_mode = DiscreteVariable(
            value_range=["fast cook", "white rice", "congee", "soup", "cake", "keep warm"],
            current_value="fast cook"
        )
        self.variable_preset_timer = ContinuousVariable(
            value_ranges_steps=[(0, 1440, 15)],  # in minutes, up to 24 hours
            current_value=0
        )

    def press_start_button(self):
        # Update feature progress and set variable_start_running to "on"
        self.feature.update_progress("press_start_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "start_running":
            self.variable_start_running.set_current_value("on")

    def press_menu_cancel_button(self):
        # Update feature progress and adjust variable_cooking_mode
        self.feature.update_progress("press_menu_cancel_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_cooking_mode":
            self.execute_action_and_set_next("press_menu_cancel_button")

    def press_preset_time_time_button(self):
        # Update feature progress and adjust variable_preset_timer
        self.feature.update_progress("press_preset_time_time_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_preset_timer":
            self.execute_action_and_set_next("press_preset_time_time_button")

    def run_action(self, action_name, execution_times=1, **kwargs):
        # Execute the action
        return super().run_action(action_name, execution_times, **kwargs)