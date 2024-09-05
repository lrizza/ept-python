#
# LAS/LAZ module
#

import laspy


class LAZ(object):
    def __init__(self, bytes, decompression_selection):
        self.las = laspy.read(bytes, decompression_selection)
