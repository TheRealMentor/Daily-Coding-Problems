def get_itinerary(flights, curr_itinerary):
    if not flights:
        return curr_itinerary
    
    last_stop = curr_itinerary[-1]

    for i, (origin, destination) in enumerate(flights):
        flight_minus_curr = flights[:i] + flights[(i+1):]
        curr_itinerary.append(destination)
        if origin == last_stop:
            return get_itinerary(flight_minus_curr, curr_itinerary)
        curr_itinerary.pop()
    
    return None

flights = [('HNL', 'AKL'), ('YUL', 'ORD'), ('ORD', 'SFO'), ('SFO', 'HNL')]
print(get_itinerary(flights, ['YUL']))
