import sys 
sys.path.append("packages/apiazzesi/reverse")
import reverse
import mysql.connector

def test_reverse():
    res = reverse.reverse({"input": "pippo"})
    assert res["output"] == "oppip"
