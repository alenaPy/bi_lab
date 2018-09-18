"""Simulator of booking rooms in some hotel."""
from datetime import date
from datetime import timedelta


class BookingRoom():
    """Class represents booking of some room in the hotel."""

    hotel_rooms = [100, 101, 102, 103, 104, 201, 202, 203,
                   204, 205, 206, 301, 302, 303, 304, 305, 306, ]
    booked_rooms = []

    def __init__(self, room_number, renter_name, book_date, term):
        """Create an instance of class."""
        if room_number not in BookingRoom.hotel_rooms:
            # If room doesn't present in the hotel, raise error.
            print("Room %d doesn't exist in the hotel." % room_number)
        elif room_number in BookingRoom.booked_rooms:
            # If room is already booked, raise error.
            print('Room %d is already booked.' % room_number)
        else:
            self.room_number = room_number
            self.renter_name = renter_name
            split_date = book_date.split('/')
            self.book_date = date(int(split_date[2]), int(split_date[0]),
                                  int(split_date[1]))
            self.term = timedelta(days=term)
            BookingRoom.booked_rooms.append(room_number)
            print('Room %d was successfully booked.' % self.room_number)

    def __del__(self):
        """Delete an instance of class."""
        try:
            BookingRoom.booked_rooms.remove(self.room_number)
            print('Booking for room #%d is canceled.' % self.room_number)
        except AttributeError:
            # Exception is treated for cases when initialization parameters
            # were not assigned to object variables
            # (when room doesn't exist or booked).
            pass

    def display_booking(self):
        """Display information about specific booking."""
        end_date = self.book_date + self.term
        print('Room number: ' + str(self.room_number) + '\n' +
              'Renter name: ' + self.renter_name + '\n' +
              'Book date: ' + self.book_date.strftime('%m/%d/%Y') + '\n' +
              'Book end date: ' + end_date.strftime('%m/%d/%Y'))

    @staticmethod
    def available_rooms():
        """Find available rooms in the hotel."""
        available_rooms = []
        for room in BookingRoom.hotel_rooms:
            if room not in BookingRoom.booked_rooms:
                available_rooms.append(room)
        if len(available_rooms) == 0:
            print('All rooms are booked.')
        else:
            print('Available rooms are:', available_rooms)


room101 = BookingRoom(101, 'Volodya Putin', '9/18/2018', 14)
room101_1 = BookingRoom(101, 'Slavik', '9/18/2018', 14)
room102 = BookingRoom(102, 'Boris Moiseyev', '1/13/2018', 45)
room101.display_booking()
del room101
BookingRoom.available_rooms()
