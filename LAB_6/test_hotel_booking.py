import pytest
from hotel_booking import booking_cost, cancellation_refund, room_upgrade

# --- Booking Cost Tests ---
def test_standard_two_nights():
    assert booking_cost(room="standard", nights=2, guests=2, is_peak_season=False) == 4000

def test_booking_cost_invalid_room():
    with pytest.raises(ValueError, match="unknown room"):
        booking_cost(room="tent", nights=2, guests=2, is_peak_season=False)

def test_booking_cost_invalid_nights():
    with pytest.raises(ValueError, match="invalid nights"):
        booking_cost(room="standard", nights=0, guests=2, is_peak_season=False)

def test_booking_cost_peak_season():
    assert booking_cost(room="standard", nights=1, guests=1, is_peak_season=True) == 2500

def test_booking_cost_extra_guests():
    assert booking_cost(room="deluxe", nights=2, guests=4, is_peak_season=False) == 9000

def test_booking_cost_long_stay_discount():
    assert booking_cost(room="standard", nights=7, guests=2, is_peak_season=False) == 12600


# --- Cancellation Refund Tests ---
def test_full_refund():
    assert cancellation_refund(amount=1000, days_before=10, is_member=False) == 1000

def test_cancellation_refund_half():
    assert cancellation_refund(amount=1000, days_before=3, is_member=False) == 500

def test_cancellation_refund_none():
    assert cancellation_refund(amount=1000, days_before=1, is_member=False) == 0

def test_cancellation_refund_member_bonus():
    assert cancellation_refund(amount=1000, days_before=3, is_member=True) == 750


# --- Room Upgrade Tests ---
def test_room_upgrade_no_rooms_free():
    assert room_upgrade(room="standard", is_member=True, rooms_free=0) == "standard"

def test_room_upgrade_standard_member():
    assert room_upgrade(room="standard", is_member=True, rooms_free=1) == "deluxe"

def test_room_upgrade_deluxe_member():
    assert room_upgrade(room="deluxe", is_member=True, rooms_free=1) == "suite"

def test_room_upgrade_non_member():
    assert room_upgrade(room="standard", is_member=False, rooms_free=1) == "standard"

def test_room_upgrade_suite_member():
    assert room_upgrade(room="suite", is_member=True, rooms_free=1) == "suite"