import re
from typing import Union


def validate(postcode: Union[str, None]) -> bool:
    """
    Validate a UK postcode.
    
    Args:
        postcode: The postcode string to validate
        
    Returns:
        True if the postcode is valid, False otherwise
    """
    if not postcode or not isinstance(postcode, str):
        return False
    
    result = bool(
        re.match(
            r"^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$",
            postcode
        ))
    return result
