# -*- coding: UTF-8 -*-

import unittest

from args import ARGS

import oerplib
from oerplib.error import RPCError


class TestTimeout(unittest.TestCase):

    def setUp(self):
        self.oerp = oerplib.OERP(ARGS.server, ARGS.database,
                                 protocol=ARGS.protocol, port=ARGS.port)
        self.user = self.oerp.login(ARGS.user, ARGS.passwd)

    def test_reduced_timeout(self):
        # Set the timeout
        self.oerp.timeout = 0.1
        # Execute a time consuming query: handle exception
        ids = self.oerp.search('ir.module.module', [])
        self.assertRaises(
            RPCError,
            self.oerp.write, 'ir.module.module', ids, {})

    def test_increased_timeout(self):
        # Set the timeout
        self.oerp.timeout = 120
        # Execute a time consuming query: no exception
        ids = self.oerp.search('ir.module.module', [])
        self.oerp.write('ir.module.module', ids, {})

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: