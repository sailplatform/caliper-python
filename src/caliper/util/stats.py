# -*- coding: utf-8 -*-
# Caliper-python package, util/stats module
#
# Copyright (c) 2014 IMS Global Learning Consortium, Inc. All Rights Reserved.
# Trademark Information- http://www.imsglobal.org/copyright.html

# IMS Global Caliper Analytics™ APIs are publicly licensed as Open Source
# Software via GNU General Public License version 3.0 GPL v3. This license
# contains terms incompatible with use in closed-source software including a
# copyleft provision.

# IMS Global also makes available an Alternative License based on the GNU Lesser
# General Public License. LGPL v3 Licensees (via the Alternative License) are
# required to be IMS Global members. Membership in IMS is a commitment by a
# supplier to the IMS community for ongoing support for achieving "plug and play"
# integration.  IMS Membership dues pay for ongoing maintenance for the
# Alternative License to be applicable to updates to the Caliper Analytics
# APIs. The rationale for this dual-license approach and membership component is
# to help assure a requisite level of ongoing development, project management,
# and support for the software.

# Licensees of IMS Global Caliper Analytics APIs are strongly encouraged to
# become active contributors to the Caliper Analytics project and other projects
# within IMS Global. Prospective licensees should understand that their initial
# base contribution and ongoing membership fees are insufficient to fully fund
# the ongoing development and maintenance of Caliper APIs and that voluntary
# contributions are the primary "fuel" ensuring any open source project's
# viability. Contributions can include development, bug fixing, bug reporting,
# performance analysis, and other aspects of the overall development process.

# Contributor status at the "github" level will be individual-based. Contributors
# will need to sign an IMS Global Contributor License Agreement (CLA) that grants
# IMS Global a license to contributions.

# If you are interested in licensing the IMS Global Caliper Analytics APIs please
# email licenses@imsglobal.org

from math import sqrt

class Statistic(object):
    
    def __init__(self):
        self._sum = 0.0
        self._count = 0
        self._last = 0.0

        ## standard deviation variables based on
        ## http://www.johndcook.com/standard_deviation.html
        self._oldM = 0.0
        self._newM = 0.0
        self._oldS = 0.0
        self._newS = 0.0

        self._min = 0.0
        self._max = 0.0

    def __str__(self):
        if self._min == 1.0 and self._max == 1.0:
            return '[Count: {0}]'.format(self._count)
        else:
            return '[Count : {0}], [Min : {1}], [Max : {2}], [Average : {3}], [Std. Dev. : {4}]'.format(
                self._count,
                self._min,
                self._max,
                self.average,
                self.standard_deviation
                )

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

    def update(self,val):
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


class Statistics(object):
    _keys = {
        'MEASURE' : 'Measure',
        'DESCRIBE' : 'Describe',
        'SUCCESSFUL' : 'Successful',
        'FAILED': 'Failed'
        }

    def __init__(self):
        self._map = {}
        for k in self._keys:
            self._map.update({self._keys[k]:Statistic()})

    def __str__(self):
        r_top = '\n-------- Caliper Python Statistics --------\n'
        r_bod = ''
        r_bot =   '-------------------------------------------\n'
        for k in self._keys:
            r_bod += '{0} : {1}\n'.format(
                self._keys[k],
                self._map[self._keys[k]].__str__()
                )
        return '{0}{1}{2}'.format(r_top,r_bod,r_bot)

    def clear(self):
        for k in self._keys:
            self._map[self._keys[k]].clear()

    @property
    def describes(self):
        return self._map[self._keys['DESCRIBE']]

    def update_describes(self,val):
        self._map[self._keys['DESCRIBE']].update(val)

    @property
    def measures(self):
        return self._map[self._keys['MEASURE']]

    def update_measures(self,val):
        self._map[self._keys['MEASURE']].update(val)

    @property
    def successful(self):
        return self._map[self._keys['SUCCESSFUL']]

    def update_successful(self,val):
        self._map[self._keys['SUCCESSFUL']].update(val)
            
    @property
    def failed(self):
        return self._map[self._keys['FAILED']]

    def update_failed(self,val):
        self._map[self._keys['FAILED']].update(val)
