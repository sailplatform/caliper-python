# -*- coding: utf-8 -*-
# Caliper-python package, Schema.org external defs module
#
# This file is part of the IMS Caliper Analytics(tm) and is licensed to IMS
# Global Learning Consortium, Inc. (http://www.imsglobal.org) under one or more
# contributor license agreements. See the NOTICE file distributed with this
# work for additional information.
#
# IMS Caliper is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, version 3 of the License.
#
# IMS Caliper is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see http://www.gnu.org/licenses/.
#
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.standard_library import install_aliases
install_aliases()
from builtins import *


## Schema.org entities
class Thing(object):
    pass


class CreativeWork(Thing):
    pass


class MediaObject(CreativeWork):
    pass


class AudioObject(MediaObject):
    pass


class ImageObject(MediaObject):
    pass


class SoftwareApplication(CreativeWork):
    pass


class VideoObject(MediaObject):
    pass


class WebPage(CreativeWork):
    pass
