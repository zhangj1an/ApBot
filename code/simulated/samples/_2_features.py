meta_actions_dict = {
        "0": "press_number_0_button",
        "1": "press_number_1_button",
        "2": "press_number_2_button",
        "3": "press_number_3_button",
        "4": "press_number_4_button",
        "5": "press_number_5_button",
        "6": "press_number_6_button",
        "7": "press_number_7_button",
        "8": "press_number_8_button",
        "9": "press_number_9_button",
}

meta_actions_on_number = ["press_number_1_button", "press_number_2_button", "press_number_3_button", "press_number_4_button", "press_number_5_button", "press_number_6_button", "press_number_7_button", "press_number_8_button", "press_number_9_button", "press_number_0_button"]

class Feature():
    def __init__(self, feature_list=None, current_value=("empty", 1)):
        self.feature_list = feature_list
        self.feature_list["empty"] = [{"step": 1, "actions": ["empty"]}]
        self.current_value = current_value # (feature, step)
        self.build_index_map()
    
    def get_current_value(self):
        return self.current_value
    
    def reach_end(self):
        feature_length = len(self.feature_list[self.current_value[0]])
        if self.current_value[1] == feature_length:
            return True
        return False
    
    def build_index_map(self):
        index_map = {}
        for feature, steps in self.feature_list.items():
            for index, step in enumerate(steps):
                step_key = f"{feature}_step_{step['step']}"
                index_map[step_key] = index
        self.feature_index_map = index_map

    def get_feature_step_detail(self, feature, step):
        step_key = f"{feature}_step_{step}"
        if step_key in self.feature_index_map:
            step_index = self.feature_index_map[step_key]
            return self.feature_list[feature][step_index]
        else:
            return None
        
    def get_actions(self, feature, step):
        detail = self.get_feature_step_detail(feature, step)
        if detail is not None:
            return detail["actions"]
        return None

    def update_progress(self, button_name):
        # return feature the machine will be at if the button execute successfully. 
        feature = self.current_value[0]
        step = self.current_value[1] 
        # still adjusting the same variable, then no change in progress 
        details = self.get_feature_step_detail(feature, step)
        if details is not None:
            controls = details["actions"] 
            if "variable" in details and button_name in controls:
                return
        
        next_step_details = self.get_feature_step_detail(feature, step + 1)
        # if taking action on the next step, then progress to next step
        if next_step_details is not None: 
            next_step_controls = next_step_details["actions"]
            if button_name in next_step_controls:
                self.current_value = (feature, step + 1) 
                return
        
            # checking if skipping steps to future steps in the same feature. 
            if "skip_to" in next_step_details:
                step = next_step_details["skip_to"]
                next_step_details = self.get_feature_step_detail(feature, step)
                if next_step_details is not None and button_name in next_step_details["actions"]:
                    self.current_value = (feature, step)
                    return

        # the action is not valid in this feature and is meant to transit to another feature
        
        for feature in self.feature_list.keys():
            if button_name in self.get_actions(feature, 1):
                self.current_value = (feature, 1)
                return
       
        
    
    def get_current_variable(self, action):
        detail = self.get_feature_step_detail(self.current_value[0], self.current_value[1])
        if detail is not None:
            valid_actions = detail["actions"]
            if action in valid_actions and "variable" in detail:
                return detail["variable"]
        return None
    
    def compare(self, other):
        if self.current_value != other.current_value:
            return 1
        return 0

 