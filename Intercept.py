"""
    @Created on 18 Dec 2020
    @Author: Geoff Willis
    @Email: gwillis18@yahoo.com
    @Updated On:
    @Updated On:
    @template: Wrapper class for Intercpt attributes/fields

"""


class Intercept:
    def __init__(self, pris, rfs, pds, scans, modeType, 
    lat=0.0, lon=0.0, scan_type="", elnot="", domain=""):
        self.scan_type = scan_type
        self.elnot = elnot
        self.pris  = pris
        self.rfs   = rfs
        self.pds   = pds
        self.scans = scans
        self.lattitude = float(lat)
        self.longitude = float(lon)
        self.domain = domain
        self.intercept_map = self.__dict__
        #self.intercept_map = dict([('ELNOT': self.elnot), ('PRIS': self.pris), ('RFS': self.rfs)])


    #def build_string:
        #out_string = "{ ELNOT: ".join(elnot)
        
    def __repr__(self):
        class_name = type(self).__name__
        return '{}, {!r}, {!r}, {!r}, {!r},{}'.format(class_name, pris, rfs, pds, scans, scan_type, elnot )

