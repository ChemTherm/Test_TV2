config = {

    "HPLC-Pumpe": { 
        "type": "Vorgabe",
        "x": 200,
        "y": 780,
        "Box": 1,
        "DeviceInfo":{  "Bezeichnung":"HPLC Pumpe TV.2 Test1",
                        "Seriennummer":"TestNummer123",
                        "ChemTherm-DeviceID": 15,
                        "Information": "Test DLR",
                        "unit": "ml/min",
                        "gradient": 1, 
                        "y-axis":   0,  
                        }
    },

    "Verdampfer": { 
        "type": "ExtInput",
        "input_device": "Zyk",
        "input_channel": 1,
        "x": 290,
        "y":  240,
        "Box": 1,
        "DeviceInfo":{  "Bezeichnung":"Verdampver TV.2 Test1",
                        "Seriennummer":"TestNummer123",
                        "ChemTherm-DeviceID": 15,
                        "Information": "Test DLR",
                        "Power": "6000", # Angabe der Leistung in Watt
                        "unit": "W",
                        "gradient": 0.3, # Steigung umrechnung Rohdaten mA in W 
                        "y-axis":   0,  # Y-Achsenabschnitt umrechnung Rohdaten
                        }
    },
    
    "p_1": { 
        "type": "pressure",
        "input_device": "23UK",
        "input_channel": 0,
        "x": 370,
        "y": 540,
        "DeviceInfo":{  "Bezeichnung":"IFM PT5052",
                        "Seriennummer":"TestNummer1111",
                        "ChemTherm-DeviceID": 19,
                        "Information": "5 bar",
                        "unit": "mbar",
                        "gradient": 0.5, # Steigung umrechnung Rohdaten mA in mbar 
                        "y-axis":   0,  # Y-Achsenabschnitt umrechnung Rohdaten
                        }
    },
    
          
    "T_1": { 
        "type": "thermocouple",
        "tc_type": "K",
        "input_device": "WPP",
        "input_channel": 0,
        "x": 890,
        "y": 690,
        "DeviceInfo":{  "Bezeichnung":"Verdampfer Regeltemperatur",
                        "unit": "°1C",
                        }
    },
    
    "T_2": { 
        "type": "thermocouple",
        "tc_type": "N",
        "input_device": "WQ3",
        "input_channel": 0,
        "x": 130,
        "y": 450,
        "DeviceInfo":{  "Bezeichnung":"Verdampfer Regeltemperatur",
                        "unit": "°1C",
                        }
    },
    
    "T_3": { 
        "type": "thermocouple",
        "tc_type": "N",
        "input_device": "WjR",
        "input_channel": 0,
        "x": 610,
        "y": 320,
        "DeviceInfo":{  "Bezeichnung":"Verdampfer Regeltemperatur",
                        "unit": "°1C",
                        }
    }    
}
