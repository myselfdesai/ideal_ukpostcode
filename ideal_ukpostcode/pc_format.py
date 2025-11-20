import re
from typing import Union

from ideal_ukpostcode.exceptions import InvalidArea, InvalidDistrict, InvalidSector, InvalidUnit


def validate_areacode(area: Union[str, None]) -> bool:
    """
    Validate a UK postcode area.
    
    The postcode area is either one or two characters long and is alphabetical.
    
    Args:
        area: The postcode area to validate
        
    Returns:
        True if the postcode area is valid, False otherwise
    """
    if not area or not isinstance(area, str):
        return False
    result = bool(re.match(r"^[A-Z]{1,2}$", area))
    return result


def validate_districtcode(district: Union[str, None]) -> bool:
    """
    Validate a UK postcode district.
    
    The postcode district is one digit, two digits or a digit followed by a letter.
    
    Args:
        district: The postcode district to validate
        
    Returns:
        True if the postcode district is valid, False otherwise
    """
    if not district or not isinstance(district, str):
        return False
    result = bool(re.match(r"^([0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA)$", district))
    return result


def validate_sectorcode(sector: Union[str, int, None]) -> bool:
    """
    Validate a UK postcode sector.
    
    The postcode sector is made up of a single digit.
    
    Args:
        sector: The postcode sector to validate
        
    Returns:
        True if the postcode sector is valid, False otherwise
    """
    if sector is None:
        return False
    result = bool(re.match(r"^\d$", str(sector)))
    return result


def validate_unitcode(unit: Union[str, None]) -> bool:
    """
    Validate a UK postcode unit.
    
    The postcode unit is two characters.
    
    Args:
        unit: The postcode unit to validate
        
    Returns:
        True if the postcode unit is valid, False otherwise
    """
    if not unit or not isinstance(unit, str):
        return False
    result = bool(re.match(r"^[A-Z]{2}$", unit))
    return result


def format(area: Union[str, None], district: Union[str, None], 
           sector: Union[str, int, None], unit: Union[str, None]) -> str:
    """
    Format UK postcode components into a standard postcode string.
    
    Args:
        area: The postcode area (1-2 alphabetical characters)
        district: The postcode district
        sector: The postcode sector (single digit)
        unit: The postcode unit (2 alphabetical characters)
        
    Returns:
        Formatted postcode string (e.g., "EC1A 1BB")
        
    Raises:
        InvalidArea: If the area code is invalid
        InvalidDistrict: If the district code is invalid
        InvalidSector: If the sector code is invalid
        InvalidUnit: If the unit code is invalid
    """
    if not validate_areacode(str(area)):
        raise InvalidArea
    if not validate_districtcode(str(district)):
        raise InvalidDistrict
    if not validate_sectorcode(str(sector)):
        raise InvalidSector
    if not validate_unitcode(str(unit)):
        raise InvalidUnit

    outward_code = str(area) + str(district)
    inward_code = str(sector) + str(unit)

    return outward_code + " " + inward_code
