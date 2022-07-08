#!/usr/bin/env python


import unittest
import pytest

from ideal_ukpostcode import pc_validate
from ideal_ukpostcode import pc_format
from ideal_ukpostcode.exceptions import *

class TestIdeal_ukpostcode(unittest.TestCase):
    """Tests for `ideal_ukpostcode` package."""

    def test_validate(self):
        self.assertTrue(pc_validate.validate("EC1A 1BB"))
        self.assertTrue(pc_validate.validate("W1A 0AX"))
        self.assertTrue(pc_validate.validate("M1 1AE"))
        self.assertTrue(pc_validate.validate("CR2 6XH"))
        self.assertTrue(pc_validate.validate("DN55 1PT"))

        self.assertFalse(pc_validate.validate(""))
        self.assertFalse(pc_validate.validate("1C1A 1BB"))
        self.assertFalse(pc_validate.validate("SADAKMxa da"))
        self.assertFalse(pc_validate.validate("E122A 1BB"))
        self.assertFalse(pc_validate.validate("EC1A 100"))
    
    def test_validate_areacode(self):
        self.assertTrue(pc_format.validate_areacode("EC"))
        self.assertTrue(pc_format.validate_areacode("A"))
        
        self.assertFalse(pc_format.validate_areacode(""))
        self.assertFalse(pc_format.validate_areacode("212"))
        self.assertFalse(pc_format.validate_areacode("a"))
    
    def test_validate_districtcode(self):
        self.assertTrue(pc_format.validate_districtcode("3"))
        self.assertTrue(pc_format.validate_districtcode("21"))
        self.assertTrue(pc_format.validate_districtcode("3A"))

        self.assertFalse(pc_format.validate_districtcode("AB"))
        self.assertFalse(pc_format.validate_districtcode("B2"))
        self.assertFalse(pc_format.validate_districtcode(""))

    def test_validate_sectorcode(self):
        self.assertTrue(pc_format.validate_sectorcode("2"))
        self.assertTrue(pc_format.validate_sectorcode("0"))
        self.assertTrue(pc_format.validate_sectorcode("9"))

        self.assertFalse(pc_format.validate_sectorcode("-1"))
        self.assertFalse(pc_format.validate_sectorcode(""))
        self.assertFalse(pc_format.validate_sectorcode("10"))

    def test_validate_unitcode(self):
        self.assertTrue(pc_format.validate_unitcode("HF"))
        self.assertTrue(pc_format.validate_unitcode("TB"))
        
        self.assertFalse(pc_format.validate_unitcode("ab"))
        self.assertFalse(pc_format.validate_unitcode("1"))
        self.assertFalse(pc_format.validate_unitcode(""))
    
    def test_format(self):
        with pytest.raises(InvalidArea):
            pc_format.format("1C","1A","1","BB")
        
        with pytest.raises(InvalidArea):
            pc_format.format("2","1A","1","BB")
        
        with pytest.raises(InvalidArea):
            pc_format.format("","2A","9","CC")
        
        with pytest.raises(InvalidDistrict):
            pc_format.format("EC","A","9","CC")
        
        with pytest.raises(InvalidDistrict):
            pc_format.format("EC","","9","CC")
        
        with pytest.raises(InvalidSector):
            pc_format.format("EC","1A","10","CC")
        
        with pytest.raises(InvalidSector):
            pc_format.format("EC","2A","","CC")
        

        with pytest.raises(InvalidUnit):
            pc_format.format("EC","2A","2","B2")

        with pytest.raises(InvalidUnit):
            pc_format.format("EC","2A","2","")