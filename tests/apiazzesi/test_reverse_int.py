import os, requests as req
def test_reverse_int():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/apiazzesi/reverse?input=pippo"
    res = req.get(url).json()
    assert res.get("output") == "oppip"
