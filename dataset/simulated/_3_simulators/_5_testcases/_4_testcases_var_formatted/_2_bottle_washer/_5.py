[
    {
        "command": "Turn on the washer and sterilize the bottles for 10 minutes.",
        "id": 1,
        "important_target_states": {
            "variable_power_on_off": "on",
            "variable_sterilise_only_time": 10
        },
        "optimal_step_size": 2,
        "target_state": {
            "variable_auto_mode_time": 0,
            "variable_drying_only_time": 0,
            "variable_power_on_off": "on",
            "variable_sterilise_only_time": 10,
            "variable_storage_mode": "off"
        }
    },
    {
        "command": "Turn on the washer and perform a 35-minute auto cycle.",
        "id": 2,
        "important_target_states": {
            "variable_auto_mode_time": 35,
            "variable_power_on_off": "on"
        },
        "optimal_step_size": 2,
        "target_state": {
            "variable_auto_mode_time": 35,
            "variable_drying_only_time": 0,
            "variable_power_on_off": "on",
            "variable_sterilise_only_time": 0,
            "variable_storage_mode": "off"
        }
    },
    {
        "command": "Power up the washer and dry the bottles for 40 minutes.",
        "id": 3,
        "important_target_states": {
            "variable_drying_only_time": 40,
            "variable_power_on_off": "on"
        },
        "optimal_step_size": 3,
        "target_state": {
            "variable_auto_mode_time": 0,
            "variable_drying_only_time": 40,
            "variable_power_on_off": "on",
            "variable_sterilise_only_time": 0,
            "variable_storage_mode": "off"
        }
    },
    {
        "command": "Start the washer, set sterilization for 35 minutes, and enable storage mode.",
        "id": 4,
        "important_target_states": {
            "variable_power_on_off": "on",
            "variable_sterilise_only_time": 35,
            "variable_storage_mode": "on"
        },
        "optimal_step_size": 4,
        "target_state": {
            "variable_auto_mode_time": 0,
            "variable_drying_only_time": 0,
            "variable_power_on_off": "on",
            "variable_sterilise_only_time": 35,
            "variable_storage_mode": "on"
        }
    },
    {
        "command": "Switch on the washer and execute a 60-minute auto cycle with storage mode.",
        "id": 5,
        "important_target_states": {
            "variable_auto_mode_time": 60,
            "variable_power_on_off": "on",
            "variable_storage_mode": "on"
        },
        "optimal_step_size": 4,
        "target_state": {
            "variable_auto_mode_time": 60,
            "variable_drying_only_time": 0,
            "variable_power_on_off": "on",
            "variable_sterilise_only_time": 0,
            "variable_storage_mode": "on"
        }
    },
    {
        "command": "Activate the washer and dry items for 50 minutes, then ensure they stay sterile with storage mode.",
        "id": 6,
        "important_target_states": {
            "variable_drying_only_time": 50,
            "variable_power_on_off": "on",
            "variable_storage_mode": "on"
        },
        "optimal_step_size": 5,
        "target_state": {
            "variable_auto_mode_time": 0,
            "variable_drying_only_time": 50,
            "variable_power_on_off": "on",
            "variable_sterilise_only_time": 0,
            "variable_storage_mode": "on"
        }
    },
    {
        "command": "Power the washer on and perform a short sterilization cycle for 10 minutes, keep it in storage mode.",
        "id": 7,
        "important_target_states": {
            "variable_power_on_off": "on",
            "variable_sterilise_only_time": 10,
            "variable_storage_mode": "on"
        },
        "optimal_step_size": 3,
        "target_state": {
            "variable_auto_mode_time": 0,
            "variable_drying_only_time": 0,
            "variable_power_on_off": "on",
            "variable_sterilise_only_time": 10,
            "variable_storage_mode": "on"
        }
    },
    {
        "command": "Enable the washer for a 50-minute drying and keep sterile items in storage mode.",
        "id": 8,
        "important_target_states": {
            "variable_drying_only_time": 50,
            "variable_power_on_off": "on",
            "variable_storage_mode": "on"
        },
        "optimal_step_size": 5,
        "target_state": {
            "variable_auto_mode_time": 0,
            "variable_drying_only_time": 50,
            "variable_power_on_off": "on",
            "variable_sterilise_only_time": 0,
            "variable_storage_mode": "on"
        }
    },
    {
        "command": "Activate the washer and begin a 60-minute auto cycle, ensuring it is stored post-operation.",
        "id": 9,
        "important_target_states": {
            "variable_auto_mode_time": 60,
            "variable_power_on_off": "on",
            "variable_storage_mode": "on"
        },
        "optimal_step_size": 4,
        "target_state": {
            "variable_auto_mode_time": 60,
            "variable_drying_only_time": 0,
            "variable_power_on_off": "on",
            "variable_sterilise_only_time": 0,
            "variable_storage_mode": "on"
        }
    },
    {
        "command": "Initiate the washer to dry bottles for 30 minutes, then enable storage.",
        "id": 10,
        "important_target_states": {
            "variable_drying_only_time": 30,
            "variable_power_on_off": "on",
            "variable_storage_mode": "on"
        },
        "optimal_step_size": 3,
        "target_state": {
            "variable_auto_mode_time": 0,
            "variable_drying_only_time": 30,
            "variable_power_on_off": "on",
            "variable_sterilise_only_time": 0,
            "variable_storage_mode": "on"
        }
    }
]
