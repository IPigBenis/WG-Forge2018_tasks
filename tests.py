from unittest import TestCase
from IGOR_TURCEVICH_WGFORGE2018.TASK2.task2 import analyze_text


class TestTask2(TestCase):
    def test_task1_1(self):
        text = (
            r"""
            192.168.1.1 [fsgrgreg] regerg 2.3 fdger 4.44.4 geg789 89
            192.168.1.1 [rgrgerg]ergergerrg ergerger 2.2.2.2 ggreg3.5.6.2
            3.5.6.2 fsdfsdf uhsdu fa4 438 9 438  gdfhg ew
            1.1.1.1 uerhegw gerg erug3.2.3.5
            2.4.52.5 fjghhg urgh uerg regu er3.5.6.2
            4.5.7.8 ufghr urgh uerhg/3.5.6.2
            4.5.7.8 ufghr urgh uerhg\3.5.6.2     
            """
        )

        actual = analyze_text(text, 2)
        expected = ['192.168.1.1', '4.5.7.8']
        self.assertIn(actual, expected)

    def test_task1_2(self):
        text = (
            """
            3.4.5.5 gtr 4.4.4.44.4.4 ttrhtr thgur thurt gurth gurg
            3.4.5.6. igjrt tijg rjg rk kt 3.3.3.3
            grj i rijgi jti grkt krkg kgkr 
            1.1.1.1.1 jg itrjij rije 3.4.5.6.4
            rg
            3.4.5.6 gijri i4543 .34.34.5.34 
            3.5.6.7.irjti  itjhi 1.1.1.1
            2.3..64 igjir gj ijg itjg rtgr
            3.5.6.2 igjirgierge
            3.5.6.2 igjri gjierg iergei rjgerjg ijr gjti jhrjt kgj
            """
        )

        actual = analyze_text(text, 2)
        self.assertIn(actual, ['3.5.6.2', '11.1.1.1'])



