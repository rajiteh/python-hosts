import pytest
import socket
import sys
from os import path
sys.path.insert(0, path.abspath(path.join(path.dirname( __file__ ), '..', 'hosts')))
from utils import is_ipv4, is_ipv6


def test_ipv4_validation_success():
    """
    Test function returns True if valid IPv4 address is specified
    """
    assert is_ipv4('8.8.8.8')


def test_ipv4_validation_failure():
    """
    Test function returns False if invalid IPv4 address is specified
    """
    #with pytest.raises(socket.error):
    assert is_ipv4('256.8.8.8') == False

def test_ipv6_validation_success():
    """
    Test function returns True if valid IPv4 address is specified
    """
    assert is_ipv6('2001:db8::ff00:42:8329')


def test_ipv6_validation_failure():
    """
    Test function returns False if invalid IPv4 address is specified
    """
    #with pytest.raises(socket.error):
    assert is_ipv6('2001::0234:C1ab::A0:aabc:003F') == False