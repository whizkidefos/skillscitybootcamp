from room import Room

kitchen = Room("Kitchen", "A dank and dirty room buzzing with flies.")
kitchen.set_description("A dank and dirty room buzzing with flies.")


ballroom = Room("Ballroom", "A vast room with shiny wooden floors; huge candlesticks guard the entrance.")
ballroom.set_description("A vast room with shiny wooden floors; huge candlesticks guard the entrance.")


dining_hall = Room("Dining Hall", "A room with a large table and chairs.")
dining_hall.set_description("A room with a large table and chairs.")


kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")


dining_hall.get_details()