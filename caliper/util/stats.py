# -*- coding: utf-8 -*-
# Caliper-python package, util/stats module
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
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.standard_library import install_aliases
install_aliases()

from math import sqrt


class Statistic(object):
    _count_string = '[Count: {0}]'
    _stats_string = '[Count : {0}], [Min : {1}], [Max : {2}], [Average : {3}], [Std. Dev. : {4}]'

    def __init__(self):
        self._sum = 0.0
        self._count = 0
        self._last = 0.0

        # standard deviation variables based on
        # http://www.johndcook.com/standard_deviation.html
        self._oldM = 0.0
        self._newM = 0.0
        self._oldS = 0.0
        self._newS = 0.0

        self._min = 0.0
        self._max = 0.0

    def __str__(self):
        if self._min == 1.0 and self._max == 1.0:
            return self._count_string.format(self._count)
        else:
            return self._stats_string.format(self._count, self._min, self._max, self.average,
                                             self.standard_deviation)

    def clear(self):
        self._sum = 0.0
        self._count = 0
        self._last = 0.0
        self._oldM = 0.0
        self._newM = 0.0
        self._oldS = 0.0
        self._newS = 0.0
        self._min = 0.0
        self._max = 0.0

    def update(self, val):
        if not self._count:
            self._count += 1
            self._min = self._max = self._oldM = self._newM = val
            self.oldS = 0.0
        else:
            self._count += 1
            self._newM = self._oldM + ((val - self._oldM) / self._count)
            self._newS = self._oldS + ((val - self._oldM) * (val * self._newM))
            self._oldM = self._newM
            self._oldS = self._newS

        self._min = min(val, self._min)
        self._max = max(val, self._max)
        self._sum += val
        self._last = val

    @property
    def sum(self):
        return self._sum

    @property
    def count(self):
        return self._count

    @property
    def average(self):
        if self._count == 0:
            return 0.0
        else:
            return (self._sum / self._count)

    @property
    def variance(self):
        if self._count < 1:
            return 1.0
        else:
            return (self._newS / (self._count - 1))

    @property
    def standard_deviation(self):
        return sqrt(self.variance)

    @property
    def min(self):
        return self._min

    @property
    def max(self):
        return self._max

    @property
    def last(self):
        return self._last


class BaseStatistics(object):
    _keys = {'SUCCESSFUL': 'Successful', 'FAILED': 'Failed'}

    def __init__(self):
        self._map = {}
        for k in self._keys:
            self._map.update({self._keys[k]: Statistic()})

    def __str__(self):
        r_top = '\n-------- Caliper Python Statistics --------\n'
        r_bod = ''
        r_bot = '-------------------------------------------\n'
        for k in self._keys:
            r_bod += '{0} : {1}\n'.format(self._keys[k], self._map[self._keys[k]].__str__())
        return '{0}{1}{2}'.format(r_top, r_bod, r_bot)

    def clear(self):
        for k in self._keys:
            self._map[self._keys[k]].clear()

    @property
    def successful(self):
        return self._map[self._keys['SUCCESSFUL']]

    def update_successful(self, val):
        self._map[self._keys['SUCCESSFUL']].update(val)

    @property
    def failed(self):
        return self._map[self._keys['FAILED']]

    def update_failed(self, val):
        self._map[self._keys['FAILED']].update(val)


class SimpleStatistics(BaseStatistics):
    _keys = {'SENT': 'Sent', 'SUCCESSFUL': 'Successful', 'FAILED': 'Failed'}

    def __init__(self):
        BaseStatistics.__init__(self)

    @property
    def sent(self):
        return self._map[self._keys['SENT']]

    def update_sent(self, val):
        self._map[self._keys['SENT']].update(val)


class Statistics(BaseStatistics):
    _keys = {
        'MEASURE': 'Measure',
        'DESCRIBE': 'Describe',
        'SUCCESSFUL': 'Successful',
        'FAILED': 'Failed'
    }

    def __init__(self):
        BaseStatistics.__init__(self)

    @property
    def describes(self):
        return self._map[self._keys['DESCRIBE']]

    def update_describes(self, val):
        self._map[self._keys['DESCRIBE']].update(val)

    @property
    def measures(self):
        return self._map[self._keys['MEASURE']]

    def update_measures(self, val):
        self._map[self._keys['MEASURE']].update(val)
