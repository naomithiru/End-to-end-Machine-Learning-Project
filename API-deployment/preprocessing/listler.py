global subtype
subtype = ['APARTMENT', 'APARTMENT_BLOCK', 'BUNGALOW', 'COUNTRY_COTTAGE', 'DUPLEX', 'EXCEPTIONAL_PROPERTY',
           'FARMHOUSE', 'FLAT_STUDIO', 'GROUND_FLOOR', 'HOUSE', 'KOT', 'LOFT', 'MANOR_HOUSE', 'MANSION',
           'MIXED_USE_BUILDING', 'OTHER_PROPERTY', 'PENTHOUSE', 'SERVICE_FLAT', 'TOWN_HOUSE', 'TRIPLEX', 'VILLA', ]

f3 = ['source', 'house_is', 'property_subtype', 'price', 'postcode', 'area',
      'rooms_number', 'equipped_kitchen_has', 'garden', 'garden_area',
      'terrace', 'terrace_area', 'furnished', 'swimming_pool_has',
      'land_surface', 'basement', 'building_state_agg', 'open_fire',
      'longitude', 'latitude']

sample_json_input = {
    "data": {
        "property-type": "APARTMENT",
        "zip-code": 1000,
        "area": "10",
        "rooms-number": 1,
        "property_subtype": "APARTMENT_BLOCK",
        "land-area": "djfg",
        "garden": 1,
        "garden-area": "djfg",
        "equipped-kitchen": 1,
        "full-address": "djfg",
        "swimmingpool": 1,
        "furnished": 1,
        "open-fire": 1,
        "terrace": 1,
        "terrace-area": "djfg",
        "facades-number": "djfg",
        "building-state": "GOOD"
    }
}
json_input = {'data': {'area': 10, 'property-type': 'APARTMENT', 'rooms-number': 1, 'zip-code': 1000, 'land-area': 10,
                       'garden': 1, 'garden-area': 10, 'equipped-kitchen': 1, 'full-address': 'djfg', 'swimmingpool': 1,
                       'furnished': 1, 'open-fire': 1, 'terrace': 1, 'terrace-area': 10, 'facades-number': 4,
                       'latitude': 0, 'longitude': 0, 'col1_col1_APARTMENT_BLOCK': 0, 'col1_col1_BUNGALOW': 0, 'col1_col1_COUNTRY_COTTAGE': 0,
                       'col1_col1_DUPLEX': 0, 'col1_col1_EXCEPTIONAL_PROPERTY': 0, 'col1_col1_FARMHOUSE': 0, 'col1_col1_FLAT_STUDIO': 0, 'col1_col1_GROUND_FLOOR': 0,
                       'col1_col1_HOUSE': 0, 'col1_col1_KOT': 0, 'col1_col1_LOFT': 0, 'col1_col1_MANOR_HOUSE': 0, 'col1_col1_MANSION': 0,
                       'col1_col1_MIXED_USE_BUILDING': 0, 'col1_col1_OTHER_PROPERTY': 0, 'col1_col1_PENTHOUSE': 0, 'col1_col1_SERVICE_FLAT': 0, 'col1_col1_TOWN_HOUSE': 0,
                       'col1_col1_TRIPLEX': 0, 'col1_col1_VILLA': 0, 'col2_col2_AS_NEW': 0, 'col2_col2_GOOD': 0, 'col2_col2_JUST_RENOVATED': 0,
                       'col2_col2_TO_RENOVATE': 0, 'col2_col2_TO_RESTORE': 0}}

a = ['area ', 'rooms-number ', 'zip-code ', 'land-area ', 'garden ', 'garden-area ', 'equipped-kitchen ', 'swimmingpool ', 'furnished ', 'open-fire ', 'terrace ', 'terrace-area ', 'latitude ', 'longitude ', 'col1_APARTMENT ', 'col1_APARTMENT_BLOCK ', 'col1_BUNGALOW ', 'col1_COUNTRY_COTTAGE ', 'col1_DUPLEX ', 'col1_EXCEPTIONAL_PROPERTY ', 'col1_FARMHOUSE ',
     'col1_FLAT_STUDIO ', 'col1_GROUND_FLOOR ', 'col1_HOUSE ', 'col1_KOT ', 'col1_LOFT ', 'col1_MANOR_HOUSE ', 'col1_MANSION ', 'col1_MIXED_USE_BUILDING ', 'col1_OTHER_PROPERTY ', 'col1_PENTHOUSE ', 'col1_SERVICE_FLAT ', 'col1_TOWN_HOUSE ', 'col1_TRIPLEX ', 'col1_VILLA ', 'col2_AS_NEW ', 'col2_GOOD ', 'col2_JUST_RENOVATED ', 'col2_TO_RENOVATE ', 'col2_TO_RESTORE ']

f = ['postcode', 'area', 'rooms_number', 'equipped_kitchen_has', 'garden', 'garden_area', 'terrace', 'terrace_area', 'furnished',
     'swimming_pool_has', 'land_surface', 'open_fire', 'longitude', 'latitude', 'col1_APARTMENT', 'col1_APARTMENT_BLOCK',
     'col1_BUNGALOW', 'col1_COUNTRY_COTTAGE', 'col1_DUPLEX', 'col1_EXCEPTIONAL_PROPERTY', 'col1_FARMHOUSE', 'col1_FLAT_STUDIO',
     'col1_GROUND_FLOOR', 'col1_HOUSE', 'col1_KOT', 'col1_LOFT', 'col1_MANOR_HOUSE', 'col1_MANSION', 'col1_MIXED_USE_BUILDING',
     'col1_OTHER_PROPERTY', 'col1_PENTHOUSE', 'col1_SERVICE_FLAT', 'col1_TOWN_HOUSE', 'col1_TRIPLEX', 'col1_VILLA', 'col2_AS_NEW',
     'col2_GOOD', 'col2_JUST_RENOVATED', 'col2_TO_RENOVATE',
     'col2_TO_RESTORE']

template = {
    "data": {
        "area": int,
        "property-type": ["APARTMENT", "HOUSE", "OTHERS"],
        "rooms-number": int,
        "zip-code": int,
        "land-area": [int],  # Optional
        "garden": [bool],  # Optional
        "garden-area": [int],  # Optional
        "equipped-kitchen": [bool],  # Optional
        "full-address": [str],  # Optional
        "swimmingpool": [bool],  # Optional
        "furnished": [bool],  # Optional
        "open-fire": [bool],  # Optional
        "terrace": [bool],  # Optional
        "terrace-area": [int],  # Optional
        "facades-number": [int],  # Optional
        # Optional
        "building-state": ["NEW", "GOOD", "TO RENOVATE", "JUST RENOVATED", "TO REBUILD"]
    }
}
global postcodes
postcodes = [1840, 2600, 1082, 4000, 7140, 6031, 1000, 1300, 1050, 1030, 1090, 8370, 9100, 5620, 2610, 5530, 4020, 4671, 2140, 6001, 1600, 6769, 6120, 2390, 2000, 5570, 9500, 7900, 6940, 2870, 7000, 6030, 9310, 4040, 1020, 1070, 1332, 5020, 6060, 9600, 9660, 9680, 2960, 7390, 4400, 1980, 6000, 4470, 4800, 7100, 4600, 1650, 6200, 1500, 4367, 2300, 3270, 2018, 4890, 3200, 1730, 7110, 2100, 5000, 6010, 1080, 2060, 9000, 1060, 1170, 6044, 7850, 6971, 4100, 6032, 4610, 3970, 1083, 2400, 7160, 9200, 2500, 1785, 4430, 6953, 7740, 2490, 4300, 6041, 5500, 3530, 7090, 9250, 9940, 4031, 6960, 8700, 1780, 4630, 7080, 7041, 2070, 3500, 3540, 8520, 6591, 6760, 2480, 4683, 4920, 4170, 8450, 7700, 3980, 7020, 2440, 1410, 1652, 2660, 6740, 4540, 4910, 1745, 4500, 4030, 3001, 6110, 8300, 6560, 8760, 2200, 3945, 9230, 9700, 9320, 1861, 6830, 6840, 1320, 7380, 6140, 7711, 7500, 1310, 1150, 7370, 2640, 3470, 9300, 1180, 3600, 2270, 6800, 5651, 6020, 4690, 6900, 2150, 6600, 6061, 2275, 2900, 4980, 2340, 4141, 2830, 3740, 7180, 6590, 4460, 6880, 6724, 1430, 2460, 9260, 5100, 1654, 1120, 8560, 1400, 4480, 4670, 4851, 4032, 2970, 7130, 7330, 8750, 2560, 2280, 5150, 6180, 1190, 3290, 9130, 4680, 6762, 1420, 9620, 6040, 7170, 3798, 4900, 3840, 4820, 9960, 3800, 2930, 1470, 7620, 4317, 4602, 8840, 9950, 6181, 2980, 5060, 1930, 3520, 1700, 1703, 7870, 1932, 7300, 8430, 5330, 6870, 9050, 8434, 6767, 2240, 3130, 8500, 4260, 9255, 1853, 3620, 7350, 2550, 1760, 1457, 4761, 3700, 3512, 4101, 1081, 7012, 7070, 8820, 8420, 8210, 9070, 8200, 3630, 3300, 4171, 6990, 7340, 4190, 9810, 3320, 5377, 7940, 4731, 1640, 1040, 9030, 6534, 4420, 4130, 4530, 5310, 3010, 9900, 2940, 4140, 9041, 6043, 6182, 6717, 1480, 1731, 1800, 3053, 9930, 8400, 2310, 8880, 3450, 1140, 3650, 1702, 5590, 5361, 9120, 2170, 8800, 8380, 2430, 7022, 8610, 7800, 9140, 9880, 2650, 9400, 3560, 3770, 1755, 8377, 2620, 2020, 2845, 9220, 9160, 4102, 4560, 6850, 5550, 7950, 1495, 1160, 9402, 1370, 9470, 5640, 2520, 2800, 5030, 4970, 3660, 3910, 4960, 8690, 7972, 8510, 7782, 2860, 8000, 1200, 3201, 8630, 3212, 2110, 3830, 4180, 4720, 1301, 4790, 4870, 9150, 4257, 2570, 5544, 5004, 3550, 8660, 5300, 9630, 3870, 8930, 9080, 5003, 8810, 3941, 7600, 2470, 7860, 9060, 9290, 8580, 5370, 5542, 8900, 2920, 2880, 4280, 6690, 1450, 5002, 6670, 8640, 4821, 6791, 5190, 3000, 9690, 3070, 9340, 4801, 7780, 4750, 1210, 3920, 1440, 4700, 3380, 7034, 2220, 3190, 2320, 8791, 5580, 3990, 1390, 1820, 3900, 8680, 4860, 8670, 9550, 9190, 8310, 3202, 2630, 1360, 6111, 9450, 3400, 6730, 4845, 2850, 4557, 3440, 6660, 3360, 5650, 1350, 6890, 3971, 8780, 8530, 3401, 8792, 3090, 1950, 1630, 3621, 5555, 1933, 4621, 8920, 9280, 4051, 7021, 6810, 7387, 3930, 6141, 9040, 4121, 4840, 6250, 4728, 4701, 9472, 3040, 3680, 4880, 5022, 7011, 3950, 7603, 6460, 6183, 6673, 7501, 9681, 9240, 4780, 4650,
             4730, 1460, 2030, 4830, 2590, 4877, 8020, 6220, 2540, 5630, 1547, 3960, 1701, 2840, 6720, 7971, 8620, 2431, 5670, 6500, 5350, 3583, 4760, 2160, 1348, 6980, 1851, 7712, 5001, 9770, 5540, 9570, 5360, 6700, 4950, 4802, 2230, 3220, 7880, 5140, 5560, 9980, 1910, 6530, 3404, 7382, 3670, 4654, 9420, 9170, 9881, 3850, 7540, 6280, 2250, 4681, 6820, 8830, 7033, 6997, 7730, 2380, 3891, 7024, 9506, 3020, 1435, 7622, 4340, 4217, 9910, 8340, 7520, 7502, 9051, 1340, 6150, 8710, 1380, 8740, 5561, 3640, 9800, 6224, 8870, 5537, 1490, 8540, 8970, 1570, 3210, 3110, 2360, 9790, 7060, 6240, 3590, 5660, 7810, 3012, 9571, 4550, 5600, 3370, 6834, 3570, 2260, 6238, 7141, 7623, 3580, 5070, 9990, 7050, 9308, 7760, 8600, 8953, 8501, 2180, 7040, 6567, 8790, 2950, 6533, 8460, 5021, 7134, 1970, 8770, 2235, 7890, 2580, 5621, 5574, 3940, 4120, 7504, 7331, 4837, 1653, 4570, 6922, 1357, 9750, 4590, 4987, 5340, 7640, 2450, 4218, 8956, 8421, 3730, 1830, 7618, 6461, 7822, 4983, 5520, 7830, 9991, 6887, 8730, 4360, 7903, 8570, 3080, 4053, 4351, 1852, 4357, 8573, 2530, 4052, 3271, 4520, 7181, 2050, 8211, 1880, 3390, 6812, 4577, 1330, 4450, 6792, 1325, 9270, 8793, 4042, 4537, 5351, 7912, 7910, 1770, 3120, 8890, 6230, 1850, 7970, 9830, 3460, 6637, 1560, 6210, 4607, 4608, 4350, 8490, 7801, 5354, 1502, 5523, 1860, 5101, 1790, 4050, 8850, 9820, 7190, 9850, 2890, 6440, 6950, 6761, 7334, 4287, 4261, 9840, 1620, 2381, 7951, 4163, 5170, 6750, 4041, 3890, 8720, 9870, 4432, 2491, 4210, 6211, 3118, 9931, 1331, 1428, 9920, 6687, 8650, 8470, 3111, 2910, 4160, 7812, 6630, 6831, 2330, 1501, 6223, 2811, 2547, 7608, 9860, 8860, 7861, 7864, 6927, 7804, 6742, 6790, 1750, 6747, 6680, 8301, 1982, 9992, 5080, 1981, 5032, 9968, 6780, 7063, 8950, 1367, 6723, 1342, 3391, 3140, 2350, 1421, 3350, 5575, 1341, 7602, 5081, 8531, 3018, 7866, 3060, 7911, 7522, 8480, 3454, 8511, 7301, 1740, 6860, 4620, 9031, 7062, 2820, 7750, 3321, 9404, 6941, 3720, 4631, 8972, 7604, 3545, 4162, 6970, 6821, 6640, 7120, 7131, 2990, 1601, 4252, 9981, 4651, 9185, 4990, 1315, 2370, 6596, 8433, 9032, 5680, 8851, 7973, 9520, 8572, 9772, 7904, 8552, 9890, 3511, 4347, 1602, 7742, 4633, 6929, 1670, 6838, 3384, 2382, 6688, 9090, 9052, 8550, 7031, 1540, 3294, 5024, 4342, 2861, 5543, 6511, 5380, 7862, 1473, 1401, 7321, 6042, 7332, 1130, 8755, 7320, 1541, 7783, 6983, 7333, 7532, 9831, 9111, 1742, 2321, 4624, 8691, 6920, 9961, 7530, 6221, 1474, 9988, 1651, 7943, 8554, 5522, 6470, 5501, 7901, 9406, 6987, 7641, 8553, 5031, 7133, 8647, 2040, 1472, 2222, 7322, 3272, 6661, 3128, 3078, 3050, 2221, 4710, 4263, 9473, 8587, 1476, 3581, 3582, 8940, 9112, 9667, 4632, 8431, 3221, 3473, 2223, 8951, 8954, 3071, 6540, 3665, 9180, 7521, 2243, 5541, 2812, 3150, 4219, 4122, 4250, 2627, 8432, 9451, 4850, 1831, 4653, 5363, 9661, 9970, 3472, 5374, 6671, 7784, 2242, 8904, 6464, 6856, 4431, 5336, 6832, 2290]
cleaned_input = {'data': {'area': 0, 'rooms-number': 1, 'zip-code': 1000, 'land-area': 10, 'garden': 1, 'garden-area': 10, 'equipped-kitchen': 1, 'swimmingpool': 1, 'furnished': 1, 'open-fire': 1, 'terrace': 1, 'terrace-area': 10, 'latitude': 0, 'longitude': 0, 'col1_APARTMENT': 0, 'col1_APARTMENT_BLOCK': 1, 'col1_BUNGALOW': 0, 'col1_COUNTRY_COTTAGE': 0, 'col1_DUPLEX': 0, 'col1_EXCEPTIONAL_PROPERTY': 0,
                          'col1_FARMHOUSE': 0, 'col1_FLAT_STUDIO': 0, 'col1_GROUND_FLOOR': 0, 'col1_HOUSE': 0, 'col1_KOT': 0, 'col1_LOFT': 0, 'col1_MANOR_HOUSE': 0, 'col1_MANSION': 0, 'col1_MIXED_USE_BUILDING': 0, 'col1_OTHER_PROPERTY': 0, 'col1_PENTHOUSE': 0, 'col1_SERVICE_FLAT': 0, 'col1_TOWN_HOUSE': 0, 'col1_TRIPLEX': 0, 'col1_VILLA': 0, 'col2_AS_NEW': 0, 'col2_GOOD': 1, 'col2_JUST_RENOVATED': 0, 'col2_TO_RENOVATE': 0, 'col2_TO_RESTORE': 0}}