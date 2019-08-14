#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2019 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2019-07-16
# @version $Id$

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, referencePosition = netedit.setupAndStart(neteditTestRoot, ['--gui-testing-debug-gl'])

# go to demand mode
netedit.supermodeDemand()

# go to route mode
netedit.routeMode()

# create route using three edges
netedit.leftClick(referencePosition, 274, 414)
netedit.leftClick(referencePosition, 570, 250)
netedit.leftClick(referencePosition, 280, 60)

# press enter to create route
netedit.typeEnter()

# go to vehicle mode
netedit.vehicleMode()

# create vehicle
netedit.leftClick(referencePosition, 274, 414)

# go to inspect mode
netedit.inspectMode()

# inspect vehicle
netedit.leftClick(referencePosition, 91, 413)

# change departLane with an invalid value
netedit.modifyAttribute(5, "", True)

# change departLane with an invalid value
netedit.modifyAttribute(5, "dummyDepart", True)

# change departLane with an invalid value
netedit.modifyAttribute(5, "500", True)

# change departLane with an invalid value
netedit.modifyAttribute(5, "-10", True)

# change departLane with a valid value
netedit.modifyAttribute(5, "random", True)

# change departLane with a valid value
netedit.modifyAttribute(5, "free", True)

# change departLane with a valid value
netedit.modifyAttribute(5, "allowed", True)

# change departLane with a valid value
netedit.modifyAttribute(5, "best", True)

# change departLane with a valid value
netedit.modifyAttribute(5, "first", True)

# change departLane with a valid value
netedit.modifyAttribute(5, "0", True)

# Check undo redo
netedit.undo(referencePosition, 8)
netedit.redo(referencePosition, 8)

# click over reference (to avoid problem with undo-redo)
netedit.leftClick(referencePosition, 0, 0)

# save routes
netedit.saveRoutes()

# save network
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess)
