import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot responses
pairs = [
    [r"(?i).*hello.*|.*hi.*|.*hey.*", ["Hello! Welcome to our hotel. How can I assist you?", "Hi there! Looking for information about our hotel?", "Hey! How may I help you with your hotel inquiries?"]],
    [r"(?i).*rooms available.*|.*room types.*|.*accommodation options.*", ["We offer single, double, deluxe, and suite rooms with modern amenities.", "Our hotel provides a variety of rooms, including standard, luxury, and family suites.", "You can choose from single, double, executive, and penthouse suites."]],
    [r"(?i).*room rates.*|.*price of rooms.*|.*cost per night.*", ["Room rates depend on the type and season. Standard rooms start from $100 per night.", "Prices vary based on availability and season. Visit our website for the latest rates.", "Our hotel offers competitive pricing. Contact us for special discounts."]],
    [r"(?i).*amenities.*|.*facilities.*|.*services provided.*", ["We offer free Wi-Fi, a swimming pool, spa, gym, and 24/7 room service.", "Our facilities include a business center, fine dining restaurant, and airport shuttle service.", "Enjoy our rooftop lounge, in-room dining, and exclusive spa treatments."]],
    [r"(?i).*check-in time.*|.*when can i check in.*", ["Check-in time starts from 2:00 PM. Early check-in is available upon request.", "You can check in from 2:00 PM onwards. Please inform us if you need early check-in.", "Standard check-in is from 2 PM. Let us know if you have special timing needs."]],
    [r"(?i).*check-out time.*|.*when to check out.*", ["Check-out time is 12:00 PM. Late check-out may be available upon request.", "You must check out by 12:00 PM. Contact reception for late check-out options.", "Check-out is at noon. Let us know if you need to extend your stay."]],
    [r"(?i).*booking.*|.*reservation.*|.*how to book.*", ["You can book a room online through our website or call our reception for reservations.", "Visit our website or contact our front desk to make a reservation.", "To book a room, go to our booking page or call our reservation hotline."]],
    [r"(?i).*cancellation policy.*|.*refund policy.*", ["Our cancellation policy allows free cancellations up to 24 hours before check-in.", "If you cancel within 24 hours of check-in, a cancellation fee may apply.", "Full refunds are available for cancellations made at least 1 day in advance."]],
    [r"(?i).*location.*|.*where is the hotel.*|.*hotel address.*", ["Our hotel is located in the city center, near major attractions.", "You can find us at 123 Main Street, Downtown.", "Visit our website for detailed location and directions."]],
    [r"(?i).*restaurant.*|.*dining options.*|.*food services.*", ["We have a multi-cuisine restaurant, a coffee shop, and in-room dining service.", "Enjoy fine dining at our hotel restaurant or grab a quick snack at our café.", "Our hotel offers buffet breakfast, à la carte dining, and 24/7 room service."]],
    [r"(?i).*airport shuttle.*|.*transportation.*|.*pick-up service.*", ["Yes, we offer airport pick-up and drop-off services. Contact us to schedule a ride.", "Our hotel provides shuttle services to and from the airport.", "You can request an airport transfer while booking your stay."]],
    [r"(?i).*parking.*|.*car parking.*|.*is parking available.*", ["Yes, we offer free parking for all guests staying at our hotel.", "We have secure parking facilities available for guests.", "Our hotel provides both valet and self-parking options."]],
    [r"(?i).*pet policy.*|.*are pets allowed.*|.*bring my pet.*", ["Yes, our hotel is pet-friendly. Please inform us in advance if you’re bringing a pet.", "Pets are allowed in designated rooms. Additional charges may apply.", "We welcome pets, but certain restrictions apply. Contact us for details."]],
    [r"(?i).*bye.*|.*goodbye.*|.*see you later.*", ["Goodbye! Have a great stay at our hotel.", "See you later! Let us know if you need more assistance.", "Alright, take care! We hope to welcome you soon."]]
]

chatbot = Chat(pairs, reflections)

def chat():
    print("Hello! I am your hotel assistant. How can I help you today?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye! Have a great day!")
            break
        
        response = chatbot.respond(user_input)
        if not response:
            response = "I'm sorry, I don't know how to respond to that."
        
        print(f"Bot: {response}")

if __name__ == '__main__':
    chat()
