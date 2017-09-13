#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Validates Apple's in-app purchase receipt.

Uses itunesiap package to validate receipts.
Said receipts must be in a file
passed as an argument.
"""

import itunesiap
import optparse
import os.path

__author__ = "Adrià Prat"
__copyright__ = "Copyright 2017, Adrià Prat"
__credits__ = "Adrià Prat"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Adrià Prat"
__email__ = "adria@adriaprat.com"
__status__ = "Development"

def validate():
    # Setup parser
    p = optparse.OptionParser(
        description=' Validate iTunes in-app purchase receipt',
        prog='validate.py',
        version='validate 0.1',
        usage='%prog receipt.txt'
    )
    options, arguments = p.parse_args()
    if len(arguments) == 1 and os.path.exists(arguments[0]):
        f = open(arguments[0])
        try:
            # base64-encoded data from file argument
            response = itunesiap.verify(f.read())
            print response.receipt.last_in_app.product_id
        except itunesiap.exc.InvalidReceipt as e:
            print 'invalid receipt: ' + e.description
    else:
        p.print_help()

if __name__=="__main__":    #code to execute if called from command-line
	validate()
