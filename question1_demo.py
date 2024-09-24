from city_infrastructure_management import Vehicle

def main():
    car = Vehicle("WS93D1", "Hatchback", "Alan Shepherd")

    car.update_owner("Rory Gilmore")

    print(f"The vehicle's information is now: Registration Number: {car.registration_number}, Vehicle Type: {car.type}, Owner: {car.owner} ")


if __name__ == "__main__":
    main()