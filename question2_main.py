# question 2 task 1 (cont)

from event_management_enhance import Event

def main():
    the_event = Event("Concert", "10-20-2024")

    print(f"The initial participant count for {the_event.name}: {the_event.get_count()}")

    the_event.add_participant()
    the_event.add_participant()
    the_event.add_participant()

    print(f"The participant count for {the_event.name} on {the_event.date}: {the_event.get_count()}")


if __name__ == "__main__":
    main()
