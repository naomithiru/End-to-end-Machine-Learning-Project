# Definition of Json schema

from preprocessing.listler import postcodes

global json_schema
json_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Belgian real estate property",
    "description": "Features of a Belgian real estate property",
    "type": "object",
    "required": ["data"],
    "properties": {
        "data": {
            "title": "Input data",
            "type": "object",
            "required": ["area", "property-type", "rooms-number", "zip-code"],
            "properties": {
                "area": {"title": "Area", "type": "integer", "exclusiveMinimum": 0},
                "property-type": {
                    "title": "Type of property",
                    "type": "string",
                    "enum": ["APARTMENT", "HOUSE", "OTHERS"],
                },
                "rooms-number": {
                    "title": "Number of rooms",
                    "type": "integer",
                    "minimum": 1,
                },
                "zip-code": {"title": "Belgian zip-code", "enum": postcodes},
                "land-area": {"type": "integer", "default": 0},
                "garden": {"type": "boolean", "default": False},
                "garden-area": {"type": "integer"},
                "equipped-kitchen": {"type": "boolean", "default": False},
                "swimmingpool": {"type": "boolean", "default": False},
                "furnished": {"type": "boolean", "default": False},
                "open-fire": {"type": "boolean", "default": False},
                "terrace": {"type": "boolean", "default": False},
                "terrace-area": {"type": "integer"},
                "facades-number": {"type": "integer"},
                "building-state": {
                    "type": "string",
                    "default": "GOOD",
                    "enum": [
                        "NEW",
                        "GOOD",
                        "TO RENOVATE",
                        "JUST RENOVATED",
                        "TO REBUILD",
                    ],
                },
                "full-address": {
                    "type": "string",
                    "description": " - Template is 'HouseNumber,StreetName,Municipality,PostCode' and use , comma as seperator other formats are invalid for the address info",
                    "example": "10,Cantersteen,Bruxelles,1000",
                },
                "property-subtype": {
                    "type": "string",
                    "description": "This is an EXTRA FEATURE to increase accuracy of the prediction.",
                    "default": "APARTMENT",
                    "enum": ['APARTMENT', 'APARTMENT_BLOCK', 'BUNGALOW', 'COUNTRY_COTTAGE', 'DUPLEX', 'EXCEPTIONAL_PROPERTY',
                             'FARMHOUSE', 'FLAT_STUDIO', 'GROUND_FLOOR', 'HOUSE', 'KOT', 'LOFT', 'MANOR_HOUSE', 'MANSION',
                             'MIXED_USE_BUILDING', 'OTHER_PROPERTY', 'PENTHOUSE', 'SERVICE_FLAT', 'TOWN_HOUSE', 'TRIPLEX', 'VILLA', ]},
            },
        },
    },
}

if __name__ == "__main__":
    print(json_schema)
