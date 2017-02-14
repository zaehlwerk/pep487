# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 by Gregor Giesen
#
# This file is part of PEP487.
#
# PEP487 is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# PEP487 is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PEP487. If not, see <http://www.gnu.org/licenses/>.

from pep487 import PEP487Object


class TestCompat:

    def test_pep487(self):
        class TestProperty:

            def __set_name__(self, owner, name):
                self.owner = owner
                self.name = name

        class Test1(PEP487Object):
            foo = TestProperty()
            bar = set()

            def __init_subclass__(cls):
                cls.bar.add(cls)

        assert Test1.foo.owner is Test1
        assert Test1.foo.name is "foo"
        assert len(Test1.bar) == 0

        class SubTest1(Test1):
            pass

        assert SubTest1 in Test1.bar
