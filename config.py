config = {

    "HPLC-Pumpe": { 
        "type": "Vorgabe",
        "x": 200,
        "y": 800,
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
    "F_1": { 
            "type": "FlowMeter",
            "input_device": "ZYk",
            "input_channel": 1,
            "x": 570,
            "y": 670,
            "DeviceInfo":{  "Bezeichnung":"CoriFlow DLR",
                            "Seriennummer":"TestNummer1111",
                            "ChemTherm-DeviceID": 19,
                            "Information": "100 kg/h",
                            "unit": "kg/h",
                            "gradient": 0.05, # Steigung umrechnung Rohdaten mA in mbar 
                            "y-axis":   0,  # Y-Achsenabschnitt umrechnung Rohdaten
                            }
        },
        
    "Verdampfer": { 
        "type": "ExtInput",
        "input_device": "ZYk",
        "input_channel": 0,
        "x": 320,
        "y":  380,
        "Box": 1,
        "DeviceInfo":{  "Bezeichnung":"Verdampver TV.2 Test1",
                        "Seriennummer":"TestNummer123",
                        "ChemTherm-DeviceID": 15,
                        "Information": "Test DLR",
                        "Power": "6000", # Angabe der Leistung in Watt
                        "unit": "W",
                        "gradient": 0.003, # Steigung umrechnung Rohdaten nA in W 
                        "y-axis":   400000,  # Y-Achsenabschnitt umrechnung Rohdaten
                        }
    }, 
   
    
    
    "p_1": { 
        "type": "pressure",
        "input_device": "ZYj",
        "input_channel": 0,
        "x": 770,
        "y": 670,
        "DeviceInfo":{  "Bezeichnung":"IFM PT5052",
                        "Seriennummer":"TestNummer1111",
                        "ChemTherm-DeviceID": 19,
                        "Information": "100 bar",
                        "unit": "mbar",
                        "gradient": 0.0005, # Steigung umrechnung Rohdaten mA in mbar 
                        "y-axis":   0,  # Y-Achsenabschnitt umrechnung Rohdaten
                        }
    },
    
          
    "T_1": { 
        "type": "thermocouple",
        "tc_type": "K",
        "input_device": "23jK",
        "input_channel": 0,
        "x": 210,
        "y": 450,
        "DeviceInfo":{  "Bezeichnung":"Verdampfer Regeltemperatur",
                        "unit": "°C",
                        }
    },
    
    "T_2": { 
        "type": "thermocouple",
        "tc_type": "N",
        "input_device": "23kK",
        "input_channel": 0,
        "x": 610,
        "y": 320,
        "DeviceInfo":{  "Bezeichnung":"Verdampfer Innentemperatur",
                        "unit": "°C",
                        }
    },
    
    "T_3": { 
        "type": "thermocouple",
        "tc_type": "N",
        "input_device": "WQZ",
        "input_channel": 0,
        "x": 770,
        "y": 290,
        "DeviceInfo":{  "Bezeichnung":"Verdampfer Außentemperatur",
                        "unit": "°C",
                        }
    }    
}
