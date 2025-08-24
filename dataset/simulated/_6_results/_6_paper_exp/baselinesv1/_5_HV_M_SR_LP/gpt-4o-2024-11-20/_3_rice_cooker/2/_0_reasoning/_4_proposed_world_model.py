class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = Feature(
            feature_list={
                "select_cooking_mode": [
                    {"step": 1, "actions": ["press_menu_cancel_button"], "variable": "variable_cooking_mode"}
                ],
                "adjust_preset_timer": [
                    {"step": 1, "actions": ["press_preset_time_time_button"], "variable": "variable_preset_timer"}
                ],
                "start_cooking": [
                    {"step": 1, "actions": ["press_start_button"], "variable": "variable_start_running", "comment": "value always set to on"}
                ],
                "null": [
                    {"step": 1, "actions": ["press_and_hold_preset_time_time_button"], "missing_variables": []}
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

    # Action: press_menu_cancel_button
    # Effect: Updates the cooking mode to the next or previous value in the list.
    def press_menu_cancel_button(self):
        self.feature.update_progress("press_menu_cancel_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "select_cooking_mode":
            self.execute_action_and_set_next("press_menu_cancel_button")

    # Action: press_preset_time_time_button
    # Effect: Adjusts the preset timer by increasing its value in 15-minute increments.
    def press_preset_time_time_button(self):
        self.feature.update_progress("press_preset_time_time_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_preset_timer":
            self.execute_action_and_set_next("press_preset_time_time_button")

    # Action: press_start_button
    # Effect: Starts the cooking process by setting the variable_start_running to "on".
    def press_start_button(self):
        self.feature.update_progress("press_start_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "start_cooking":
            self.variable_start_running.set_current_value("on")

    # Action: press_and_hold_preset_time_time_button
    # Effect: This action is listed under "null" and does not require implementation.
    def press_and_hold_preset_time_time_button(self, duration=3):
        pass

    # Wrapper function to execute actions with global condition checks.
    def run_action(self, action_name, execution_times=1, **kwargs):
        # Execute the action.
        return super().run_action(action_name, execution_times, **kwargs)