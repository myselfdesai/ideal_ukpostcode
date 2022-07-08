# Usage

To use ideal_ukpostcode in a project:

### validate a postcode

it gives boolean result True or False
```
import ideal_ukpostcode
ideal_ukpostcode.validate("EC1A 1BB")
```

### format a postcode

format(area, district, sector, unit)
```
import ideal_ukpostcode
ideal_ukpostcode.format("EC","1A","1","BB")
```