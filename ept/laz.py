#
# LAS/LAZ module
#

import laspy


class LAZ(object):
    def __init__(self, bytes, decompression_int):
        decompression_selection = (
            laspy.compression.DecompressionSelection(decompression_int)
            if decompression_int is not None
            else None
        )
        self.las = laspy.read(
            bytes,
            decompression_selection=decompression_selection,
            laz_backend=laspy.compression.LazBackend(0),
        )
