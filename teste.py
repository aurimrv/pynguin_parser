# Automatically generated by Pynguin.
import pytest
import Identifier as module_0


def test_case_0():
    identifier_0 = module_0.Identifier()
    str_0 = "H9"
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "e6ic|mE"
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is False
    str_1 = "f"
    var_1 = identifier_0.validateIdentifier(str_1)
    assert var_1 is True
    var_0.validateIdentifier(var_1)