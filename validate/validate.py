#!/usr/bin/env python

import itunesiap
import optparse
import os.path

def validate():
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
            """ base64-encoded data """
            response = itunesiap.verify(f.read())
            print response.receipt.last_in_app.product_id 
        except itunesiap.exc.InvalidReceipt as e:
            print 'invalid receipt: ' + e.description
    else:
        p.print_help()

if __name__=="__main__":
	validate()

