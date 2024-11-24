import pytest
from television import Television

def test_power():
    tv = Television()
    assert not tv.power_status
    tv.power()
    assert tv.power_status
    tv.power()
    assert not tv.power_status

def test_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    tv.channel_up()
    assert tv.channel == 2
    for _ in range(10):
        tv.channel_up()
    assert tv.channel == 2

def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert tv.channel == 9
    tv.channel_down()
    assert tv.channel == 8

def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert tv.volume == 1
    for _ in range(10):
        tv.volume_up()
    assert tv.volume == 5

def test_volume_down():
    tv = Television()
    tv.power()
    tv.volume_down()
    assert tv.volume == 0
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert tv.volume == 1

def test_mute():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    assert tv.volume == 2
    tv.mute()
    assert tv.volume == 0
    tv.mute()
    assert tv.volume == 0
    tv.volume_up()
    assert tv.volume == 1
