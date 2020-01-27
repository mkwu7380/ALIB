from ib.ext.Contract import Contract
from ib.ext.Order import Order
from ib.opt import Connection, message


def error_handler(msg):
    """Handles the capturing of error messages"""
    print "Server Error: %s" % msg


def reply_handler(msg):
    """Handles of server replies"""
    print "Server Response: %s. %s" % (msg.typeName. msg)


def create_contract(symbol, sec_type, exch, prim_exch, curr)

"""Create a Contract object defining what will be purchased, at which exchange and in which currency.

    symbol - The ticker symbol for the Contract
    sec_type - The security type for the Contract ('STK' is 'stock')
    exch - The exchange to carry out the Contract on
    prim_exch - The primary exchange to carry out the Contract on
    curr - The currency in which to purchase the Contract"""
