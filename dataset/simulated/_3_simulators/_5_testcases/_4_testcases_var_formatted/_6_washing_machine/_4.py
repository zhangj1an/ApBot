[
    {
        "command": "Turn on the washing machine and run a Powerful wash cycle for 18 minutes with a water level of 59 L, a spin time of 9 minutes, and set rinse to 'Water-Injection Rinse 2 times', then start the machine running.",
        "id": 1,
        "important_target_states": {
            "variable_power_on_off": "on",
            "variable_program": "P2. Powerful",
            "variable_rinse_type": "Water-Injection Rinse 2 times",
            "variable_spin_time": 9,
            "variable_start_running": "on",
            "variable_wash_time": 18,
            "variable_water_level": "59 L"
        },
        "optimal_step_size": 33,
        "target_state": {
            "variable_delay_time": 0,
            "variable_power_on_off": "on",
            "variable_program": "P2. Powerful",
            "variable_rinse_type": "EX 1",
            "variable_spin_time": 9,
            "variable_start_running": "on",
            "variable_wash_time": 18,
            "variable_water_level": "59 L"
        }
    },
    {
        "command": "Turn on the washing machine and set it to perform a Speedy wash. Use a water level of 35 L and wash for 6 minutes only with no rinse, then start the machine running.",
        "id": 2,
        "important_target_states": {
            "variable_power_on_off": "on",
            "variable_program": "P3. Speedy",
            "variable_rinse_type": "no rinsing",
            "variable_start_running": "on",
            "variable_wash_time": 6,
            "variable_water_level": "35 L"
        },
        "optimal_step_size": 17,
        "target_state": {
            "variable_delay_time": 0,
            "variable_power_on_off": "on",
            "variable_program": "P3. Speedy",
            "variable_rinse_type": "No rinsing",
            "variable_spin_time": 0,
            "variable_start_running": "on",
            "variable_wash_time": 6,
            "variable_water_level": "35 L"
        }
    },
    {
        "command": "Power up the washing machine and use the Fragrance program for 15 minutes at the lowest water level, spin 3 minutes, and set rinse to 'Water-Injection Rinse 1 time', then start the machine running.",
        "id": 3,
        "important_target_states": {
            "variable_power_on_off": "on",
            "variable_program": "P4. Fragrance",
            "variable_rinse_type": "Water-Injection Rinse 1 time",
            "variable_spin_time": 3,
            "variable_start_running": "on",
            "variable_wash_time": 15,
            "variable_water_level": "25 L (Auto)"
        },
        "optimal_step_size": 29,
        "target_state": {
            "variable_delay_time": 0,
            "variable_power_on_off": "on",
            "variable_program": "P4. Fragrance",
            "variable_rinse_type": "EX 2",
            "variable_spin_time": 0,
            "variable_start_running": "on",
            "variable_wash_time": 15,
            "variable_water_level": "25 L (Auto)"
        }
    },
    {
        "command": "Turn on the washing machine and set to Soak mode. Set washing time to 18 minutes, with 30 L of water, and spin for 3 minutes only. Set rinse type to 'Normal Rinse 2 times', then start the machine running.",
        "id": 4,
        "important_target_states": {
            "variable_power_on_off": "on",
            "variable_program": "P5. Soak",
            "variable_rinse_type": "Normal Rinse 2 times",
            "variable_spin_time": 3,
            "variable_start_running": "on",
            "variable_wash_time": 18,
            "variable_water_level": "30 L"
        },
        "optimal_step_size": 33,
        "target_state": {
            "variable_delay_time": 0,
            "variable_power_on_off": "on",
            "variable_program": "P5. Soak",
            "variable_rinse_type": 2,
            "variable_spin_time": 3,
            "variable_start_running": "on",
            "variable_wash_time": 18,
            "variable_water_level": "30 L"
        }
    },
    {
        "command": "Turn on the machine and choose the Tub Clean program for a maximum water level with rinse setting to be 'Normal Rinse 1 time' and a wash time of 3 minutes, then start the machine running.",
        "id": 5,
        "important_target_states": {
            "variable_power_on_off": "on",
            "variable_program": "P6. Tub Clean",
            "variable_rinse_type": "Normal Rinse 1 time",
            "variable_start_running": "on",
            "variable_wash_time": 3,
            "variable_water_level": "59 L"
        },
        "optimal_step_size": 10,
        "target_state": {
            "variable_delay_time": 0,
            "variable_power_on_off": "on",
            "variable_program": "P6. Tub Clean",
            "variable_rinse_type": 1,
            "variable_spin_time": 0,
            "variable_start_running": "on",
            "variable_wash_time": 0,
            "variable_water_level": "59 L"
        }
    },
    {
        "command": "Turn on the washing machine. Set the washing machine to the Energy Save program, total 30L of water, wash for the full 9 minutes, and spin for 6 minutes. Set the rinse type to 'Normal Rinse 2 times', and start the machine running",
        "id": 6,
        "important_target_states": {
            "variable_power_on_off": "on",
            "variable_program": "P8. Energy Save",
            "variable_rinse_type": "Normal Rinse 2 times",
            "variable_spin_time": 6,
            "variable_start_running": "on",
            "variable_wash_time": 9,
            "variable_water_level": "30 L"
        },
        "optimal_step_size": 30,
        "target_state": {
            "variable_delay_time": 0,
            "variable_power_on_off": "on",
            "variable_program": "P8. Energy Save",
            "variable_rinse_type": "Normal 2",
            "variable_spin_time": 6,
            "variable_start_running": "on",
            "variable_wash_time": 9,
            "variable_water_level": "30 L"
        }
    },
    {
        "command": "Turn on the washing machine. Use the Small Load program with a 25 L water limit, set a 9-minute wash cycle with the rinse type to be 'Water-Injection Rinse 2 times', and a spin duration of 1 minute, then start the machine running.",
        "id": 7,
        "important_target_states": {
            "variable_power_on_off": "on",
            "variable_program": "P9. Small Load",
            "variable_rinse_type": "Water-Injection Rinse 2 times",
            "variable_spin_time": 1,
            "variable_start_running": "on",
            "variable_wash_time": 9,
            "variable_water_level": "25 L (Auto)"
        },
        "optimal_step_size": 28,
        "target_state": {
            "variable_delay_time": 0,
            "variable_power_on_off": "on",
            "variable_program": "P9. Small Load",
            "variable_rinse_type": "EX 2",
            "variable_spin_time": 1,
            "variable_start_running": "on",
            "variable_wash_time": 9,
            "variable_water_level": "25 L"
        }
    },
    {
        "command": "Turn on the washing machine. Set the machine to Fuzzy, delay start by 5 hours with a 40 L water level, 15-minute wash time, and rinse type of 'Water-Injection Rinse 1 time', then start the machine running.",
        "id": 8,
        "important_target_states": {
            "variable_delay_time": 5,
            "variable_power_on_off": "on",
            "variable_program": "P1. Fuzzy",
            "variable_rinse_type": "Water-Injection Rinse 1 time",
            "variable_start_running": "on",
            "variable_wash_time": 15,
            "variable_water_level": "40 L"
        },
        "optimal_step_size": 32,
        "target_state": {
            "variable_delay_time": 5,
            "variable_power_on_off": "on",
            "variable_program": "P1. Fuzzy",
            "variable_rinse_type": "EX 1",
            "variable_spin_time": 0,
            "variable_start_running": "on",
            "variable_wash_time": 15,
            "variable_water_level": "40 L"
        }
    },
    {
        "command": "Turn on the washing machine. Activate Powerful mode, using the rinse setting of 'Water-Injection Rinse 2 times' and spin for 6 minutes with a water level of 59 L, then start the machine running.",
        "id": 9,
        "important_target_states": {
            "variable_power_on_off": "on",
            "variable_program": "P2. Powerful",
            "variable_rinse_type": "Water-Injection Rinse 2 times",
            "variable_spin_time": 6,
            "variable_start_running": "on",
            "variable_water_level": "59 L"
        },
        "optimal_step_size": 14,
        "target_state": {
            "variable_delay_time": 0,
            "variable_power_on_off": "on",
            "variable_program": "P2. Powerful",
            "variable_rinse_type": "EX 2",
            "variable_spin_time": 6,
            "variable_start_running": "on",
            "variable_wash_time": 18,
            "variable_water_level": "59 L"
        }
    },
    {
        "command": "Turn on the washing machine. Run Speedy wash with a wash time of 10 minutes, then set water level to be 30L. Set the rinse type to be 'Water-Injection Rinse 1 time' with 3 minute spin, then start the machine running.",
        "id": 10,
        "important_target_states": {
            "variable_power_on_off": "on",
            "variable_program": "P3. Speedy",
            "variable_rinse_type": "Water-Injection Rinse 1 time",
            "variable_spin_time": 3,
            "variable_start_running": "on",
            "variable_wash_time": 10,
            "variable_water_level": "30 L"
        },
        "optimal_step_size": 22,
        "target_state": {
            "variable_delay_time": 0,
            "variable_power_on_off": "on",
            "variable_program": "P3. Speedy",
            "variable_rinse_type": 1,
            "variable_spin_time": 3,
            "variable_start_running": "on",
            "variable_wash_time": 10,
            "variable_water_level": "30 L"
        }
    }
]
