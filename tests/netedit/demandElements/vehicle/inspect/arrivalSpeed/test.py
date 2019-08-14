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

# change arrivalSpeed with an invalid value
netedit.modifyAttribute(10, "", True)

# change arrivalSpeed with an invalid value
netedit.modifyAttribute(10, "dummySpeed", True)

# change departColor with a valid value
netedit.modifyAttribute(10, "500", True)

# change arrivalSpeed with an invalid value
netedit.modifyAttribute(10, "-10", True)

# change arrivalSpeed with a valid value
netedit.modifyAttribute(10, "current", True)

# change arrivalSpeed with a valid value
netedit.modifyAttribute(10, "15.5", True)

# Check undo redo
netedit.undo(referencePosition, 5)
netedit.redo(referencePosition, 5)

# click over reference (to avoid problem with undo-redo)
netedit.leftClick(referencePosition, 0, 0)

# save routes
netedit.saveRoutes()

# save network
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess)
