import ship, weapon
import display_graphs_helpers
import numpy
import pandas
import weapon
import matplotlib.pyplot as plt
import json, ast
"""
This is for getting graphs of each weapon system for a doctrine in EVE Online
"""

if __name__ == '__main__':
    spaceship = ship.Ship({"name": "Retribution: TEST Armor AFs 19/05/2020",
                           "ehp": {"shield": 747.486694, "armor": 7741.684444, "hull": 2715.884861}, "droneDPS": 0,
                           "droneVolley": 0, "hp": {"shield": 395.0, "armor": 2273.75, "hull": 1273.75},
                           "maxTargets": 5, "maxSpeed": 2296.992206, "weaponVolley": 645.5295, "totalVolley": 645.5295,
                           "maxTargetRange": 50000.0, "scanStrength": 14.4, "weaponDPS": 264.18232,
                           "alignTime": 6.436921, "signatureRadius": 113.75, "weapons": [
            {"dps": 264.18232, "capUse": 5.540209, "falloff": 3125.0, "type": "Turret",
             "name": "Small Focused Beam Laser II, Gleam S", "optimal": 7425.0, "numCharges": 1, "numShots": 1000,
             "reloadTime": 0.01, "cycleTime": 2443.5, "volley": 645.5295, "tracking": 140.625, "maxVelocity": 0,
             "explosionDelay": 0, "damageReductionFactor": 0, "explosionRadius": 0, "explosionVelocity": 0,
             "aoeFieldRange": 0, "damageMultiplierBonusMax": 0.5, "damageMultiplierBonusPerCycle": 0,
             "dps_spread": {"em": 132.09116, "therm": 132.09116, "kin": 0.0, "exp": 0.0}}], "scanRes": 812.5,
                           "capUsed": 8.915209, "capRecharge": 12.778667, "capacitorCapacity": 718.8,
                           "rechargeRate": 140625.0, "rigSlots": 2.0, "lowSlots": 5.0, "midSlots": 2.0,
                           "highSlots": 5.0, "turretSlots": 4.0, "launcherSlots": 0, "powerOutput": 85.25,
                           "cpuOutput": 175.0, "rigSize": 1.0, "effectiveTurrets": 6.67, "effectiveLaunchers": 0.0,
                           "effectiveDroneBandwidth": 0.0,
                           "resonance": {"hull": {"exp": 0.469, "kin": 0.469, "therm": 0.469, "em": 0.469},
                                         "armor": {"exp": 0.156584, "kin": 0.293595, "therm": 0.33317, "em": 0.39146},
                                         "shield": {"exp": 0.11875, "kin": 0.285, "therm": 0.76, "em": 0.95}},
                           "typeID": 11393, "groupID": 324, "shipSize": "Frigate", "droneControlRange": 60000.0,
                           "mass": 1666400.0, "shieldrechargetime": 468750.0, "shipinertia": 2.7864,
                           "energyWarfareResistance": 0.75, "unpropedSpeed": 343.75, "unpropedSig": 35.0, "usingMWD": 1,
                           "mwdPropSpeed": 2296.992206, "projections": [], "repairs": [],
                           "modTypeIDs": [[3033, 12557], [3033, 12557], [3033, 12557], [3033, 12557], 3488, 35658,
                                          47255, 5849, 20347, 18797, 1306, 31484, 31358],
                           "moduleNames": ["High Slots:", "Small Focused Beam Laser II:  Gleam S",
                                           "Small Focused Beam Laser II:  Gleam S",
                                           "Small Focused Beam Laser II:  Gleam S",
                                           "Small Focused Beam Laser II:  Gleam S", "Empty Slot", "", "Med Slots:",
                                           "Small Cap Battery II", "5MN Quad LiF Restrained Microwarpdrive", "",
                                           "Low Slots:", "EFFA Compact Assault Damage Control",
                                           "Extruded Compact Heat Sink", "200mm Steel Plates II",
                                           "Coreli A-Type Thermal Coating", "Multispectrum Coating II", "",
                                           "Rig Slots:", "Small Energy Locus Coordinator II",
                                           "Small Ancillary Current Router I"],
                           "cargoItemIDs": [12559, 23071, 23085, 23079, 28668, 28999, 29001, 28680, 5445],
                           "pyfaVersion": "v2.33.0", "efsExportVersion": 0.04})

    spaceship2 = ship.Ship({"name": "Retribution: TEST Armor AFs 19/05/2020",
                  "ehp": {"shield": 747.486694, "armor": 7741.684444, "hull": 2715.884861}, "droneDPS": 0,
                  "droneVolley": 0,
                  "hp": {"shield": 395.0, "armor": 2273.75, "hull": 1273.75}, "maxTargets": 5, "maxSpeed": 2296.992206,
                  "weaponVolley": 368.874, "totalVolley": 368.874, "maxTargetRange": 50000.0, "scanStrength": 14.4,
                  "weaponDPS": 150.961326, "alignTime": 6.436921, "signatureRadius": 113.75, "weapons": [
            {"dps": 150.961326, "capUse": 5.540209, "falloff": 3125.0, "type": "Turret",
             "name": "Small Focused Beam Laser II, Aurora S", "optimal": 53460.0, "numCharges": 1, "numShots": 1000,
             "reloadTime": 0.01, "cycleTime": 2443.5, "volley": 368.874, "tracking": 28.125, "maxVelocity": 0,
             "explosionDelay": 0, "damageReductionFactor": 0, "explosionRadius": 0, "explosionVelocity": 0,
             "aoeFieldRange": 0, "damageMultiplierBonusMax": 0.5, "damageMultiplierBonusPerCycle": 0,
             "dps_spread": {"em": 94.350829, "therm": 56.610497, "kin": 0.0, "exp": 0.0}}], "scanRes": 812.5,
                  "capUsed": 8.915209, "capRecharge": 12.778667, "capacitorCapacity": 718.8, "rechargeRate": 140625.0,
                  "rigSlots": 2.0, "lowSlots": 5.0, "midSlots": 2.0, "highSlots": 5.0, "turretSlots": 4.0,
                  "launcherSlots": 0,
                  "powerOutput": 85.25, "cpuOutput": 175.0, "rigSize": 1.0, "effectiveTurrets": 6.67,
                  "effectiveLaunchers": 0.0,
                  "effectiveDroneBandwidth": 0.0,
                  "resonance": {"hull": {"exp": 0.469, "kin": 0.469, "therm": 0.469, "em": 0.469},
                                "armor": {"exp": 0.156584, "kin": 0.293595, "therm": 0.33317,
                                          "em": 0.39146},
                                "shield": {"exp": 0.11875, "kin": 0.285, "therm": 0.76, "em": 0.95}},
                  "typeID": 11393, "groupID": 324, "shipSize": "Frigate", "droneControlRange": 60000.0,
                  "mass": 1666400.0,
                  "shieldrechargetime": 468750.0, "shipinertia": 2.7864, "energyWarfareResistance": 0.75,
                  "unpropedSpeed": 343.75,
                  "unpropedSig": 35.0, "usingMWD": 1, "mwdPropSpeed": 2296.992206, "projections": [], "repairs": [],
                  "modTypeIDs": [[3033, 12559], [3033, 12559], [3033, 12559], [3033, 12559], 3488, 35658, 47255, 5849,
                                 20347, 18797,
                                 1306, 31484, 31358],
                  "moduleNames": ["High Slots:", "Small Focused Beam Laser II:  Aurora S",
                                  "Small Focused Beam Laser II:  Aurora S",
                                  "Small Focused Beam Laser II:  Aurora S", "Small Focused Beam Laser II:  Aurora S",
                                  "Empty Slot",
                                  "", "Med Slots:", "Small Cap Battery II", "5MN Quad LiF Restrained Microwarpdrive",
                                  "",
                                  "Low Slots:", "EFFA Compact Assault Damage Control", "Extruded Compact Heat Sink",
                                  "200mm Steel Plates II", "Coreli A-Type Thermal Coating", "Multispectrum Coating II",
                                  "",
                                  "Rig Slots:", "Small Energy Locus Coordinator II",
                                  "Small Ancillary Current Router I"],
                  "cargoItemIDs": [12559, 23071, 23085, 23079, 28668, 28999, 29001, 28680, 5445],
                  "pyfaVersion": "v2.33.0",
                  "efsExportVersion": 0.04})

    # ships = [ship.Ship({"name": "Retribution: TEST Armor AFs 19/05/2020", "ehp": {"shield": 747.486694, "armor": 7741.684444, "hull": 2715.884861}, "droneDPS": 0, "droneVolley": 0, "hp": {"shield": 395.0, "armor": 2273.75, "hull": 1273.75}, "maxTargets": 5, "maxSpeed": 2296.992206, "weaponVolley": 645.5295, "totalVolley": 645.5295, "maxTargetRange": 50000.0, "scanStrength": 14.4, "weaponDPS": 264.18232, "alignTime": 6.436921, "signatureRadius": 113.75, "weapons": [{"dps": 264.18232, "capUse": 5.540209, "falloff": 3125.0, "type": "Turret", "name": "Small Focused Beam Laser II, Gleam S", "optimal": 7425.0, "numCharges": 1, "numShots": 1000, "reloadTime": 0.01, "cycleTime": 2443.5, "volley": 645.5295, "tracking": 140.625, "maxVelocity": 0, "explosionDelay": 0, "damageReductionFactor": 0, "explosionRadius": 0, "explosionVelocity": 0, "aoeFieldRange": 0, "damageMultiplierBonusMax": 0.5, "damageMultiplierBonusPerCycle": 0, "dps_spread": {"em": 132.09116, "therm": 132.09116, "kin": 0.0, "exp": 0.0}}], "scanRes": 812.5, "capUsed": 8.915209, "capRecharge": 12.778667, "capacitorCapacity": 718.8, "rechargeRate": 140625.0, "rigSlots": 2.0, "lowSlots": 5.0, "midSlots": 2.0, "highSlots": 5.0, "turretSlots": 4.0, "launcherSlots": 0, "powerOutput": 85.25, "cpuOutput": 175.0, "rigSize": 1.0, "effectiveTurrets": 6.67, "effectiveLaunchers": 0.0, "effectiveDroneBandwidth": 0.0, "resonance": {"hull": {"exp": 0.469, "kin": 0.469, "therm": 0.469, "em": 0.469}, "armor": {"exp": 0.156584, "kin": 0.293595, "therm": 0.33317, "em": 0.39146}, "shield": {"exp": 0.11875, "kin": 0.285, "therm": 0.76, "em": 0.95}}, "typeID": 11393, "groupID": 324, "shipSize": "Frigate", "droneControlRange": 60000.0, "mass": 1666400.0, "shieldrechargetime": 468750.0, "shipinertia": 2.7864, "energyWarfareResistance": 0.75, "unpropedSpeed": 343.75, "unpropedSig": 35.0, "usingMWD": 1, "mwdPropSpeed": 2296.992206, "projections": [], "repairs": [], "modTypeIDs": [[3033, 12557], [3033, 12557], [3033, 12557], [3033, 12557], 3488, 35658, 47255, 5849, 20347, 18797, 1306, 31484, 31358], "moduleNames": ["High Slots:", "Small Focused Beam Laser II:  Gleam S", "Small Focused Beam Laser II:  Gleam S", "Small Focused Beam Laser II:  Gleam S", "Small Focused Beam Laser II:  Gleam S", "Empty Slot", "", "Med Slots:", "Small Cap Battery II", "5MN Quad LiF Restrained Microwarpdrive", "", "Low Slots:", "EFFA Compact Assault Damage Control", "Extruded Compact Heat Sink", "200mm Steel Plates II", "Coreli A-Type Thermal Coating", "Multispectrum Coating II", "", "Rig Slots:", "Small Energy Locus Coordinator II", "Small Ancillary Current Router I"], "cargoItemIDs": [12559, 23071, 23085, 23079, 28668, 28999, 29001, 28680, 5445], "pyfaVersion": "v2.33.0", "efsExportVersion": 0.04}),
    #          ship.Ship({"name": "Retribution: TEST Armor AFs 19/05/2020", "ehp": {"shield": 747.486694, "armor": 7741.684444, "hull": 2715.884861}, "droneDPS": 0, "droneVolley": 0, "hp": {"shield": 395.0, "armor": 2273.75, "hull": 1273.75}, "maxTargets": 5, "maxSpeed": 2296.992206, "weaponVolley": 368.874, "totalVolley": 368.874, "maxTargetRange": 50000.0, "scanStrength": 14.4, "weaponDPS": 150.961326, "alignTime": 6.436921, "signatureRadius": 113.75, "weapons": [{"dps": 150.961326, "capUse": 5.540209, "falloff": 3125.0, "type": "Turret", "name": "Small Focused Beam Laser II, Aurora S", "optimal": 53460.0, "numCharges": 1, "numShots": 1000, "reloadTime": 0.01, "cycleTime": 2443.5, "volley": 368.874, "tracking": 28.125, "maxVelocity": 0, "explosionDelay": 0, "damageReductionFactor": 0, "explosionRadius": 0, "explosionVelocity": 0, "aoeFieldRange": 0, "damageMultiplierBonusMax": 0.5, "damageMultiplierBonusPerCycle": 0, "dps_spread": {"em": 94.350829, "therm": 56.610497, "kin": 0.0, "exp": 0.0}}], "scanRes": 812.5, "capUsed": 8.915209, "capRecharge": 12.778667, "capacitorCapacity": 718.8, "rechargeRate": 140625.0, "rigSlots": 2.0, "lowSlots": 5.0, "midSlots": 2.0, "highSlots": 5.0, "turretSlots": 4.0, "launcherSlots": 0, "powerOutput": 85.25, "cpuOutput": 175.0, "rigSize": 1.0, "effectiveTurrets": 6.67, "effectiveLaunchers": 0.0, "effectiveDroneBandwidth": 0.0, "resonance": {"hull": {"exp": 0.469, "kin": 0.469, "therm": 0.469, "em": 0.469}, "armor": {"exp": 0.156584, "kin": 0.293595, "therm": 0.33317, "em": 0.39146}, "shield": {"exp": 0.11875, "kin": 0.285, "therm": 0.76, "em": 0.95}}, "typeID": 11393, "groupID": 324, "shipSize": "Frigate", "droneControlRange": 60000.0, "mass": 1666400.0, "shieldrechargetime": 468750.0, "shipinertia": 2.7864, "energyWarfareResistance": 0.75, "unpropedSpeed": 343.75, "unpropedSig": 35.0, "usingMWD": 1, "mwdPropSpeed": 2296.992206, "projections": [], "repairs": [], "modTypeIDs": [[3033, 12559], [3033, 12559], [3033, 12559], [3033, 12559], 3488, 35658, 47255, 5849, 20347, 18797, 1306, 31484, 31358], "moduleNames": ["High Slots:", "Small Focused Beam Laser II:  Aurora S", "Small Focused Beam Laser II:  Aurora S", "Small Focused Beam Laser II:  Aurora S", "Small Focused Beam Laser II:  Aurora S", "Empty Slot", "", "Med Slots:", "Small Cap Battery II", "5MN Quad LiF Restrained Microwarpdrive", "", "Low Slots:", "EFFA Compact Assault Damage Control", "Extruded Compact Heat Sink", "200mm Steel Plates II", "Coreli A-Type Thermal Coating", "Multispectrum Coating II", "", "Rig Slots:", "Small Energy Locus Coordinator II", "Small Ancillary Current Router I"], "cargoItemIDs": [12559, 23071, 23085, 23079, 28668, 28999, 29001, 28680, 5445], "pyfaVersion": "v2.33.0", "efsExportVersion": 0.04})]
    still_putting_in_ammo_types = 1

    import sys
    import test_fits
    # while still_putting_in_ammo_types != 0:
    #     ships.append(ship.Ship(ast.literal_eval(input("Input JSON EFS of ship from Sajuuk's Fork of Pyfa!"))))
    #     still_putting_in_ammo_types = int(input("More ammo? (0 = no, 1 = yes"))
    ships = None
    exec("ships = test_fits.{}".format(sys.argv[1]))

    for aship in range(0,len(ships)):
        ships[aship] = ship.Ship(ships[aship])

    fig = plt.figure()
    for ship in ships:

        for weapon in ship.weapon:
            display_graphs_helpers.plot_weapon_ecm_repper_profile(weapon, plt, fig)
    plt.rcParams["figure.figsize"] = [16,9]
    plt.title("{} at Char Setup: {}".format(sys.argv[1],sys.argv[2]))
    plt.show()