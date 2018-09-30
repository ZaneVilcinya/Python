class Vehicles:
    def __init__(self, brand, model, km_done, service_date):
        self.brand = brand
        self.model = model
        self.km_done = km_done
        self.service_date = service_date

        def add_km(self, new_km):
            self.km_done += new_km

        def update_service_date(self, new_date):
            self.service_date = new_date

    def list_all_vehicles(vehicles):
        if not vehicles:
            print(
                "We are sorry, but there are no vehicles in the system yet. Please select b) to add the first vehicle.")
        else:
            for index, vehicle in enumerate(vehicles):
                print("%s) %s %s with %s km driven. Last service date: %s") \
                % (index + 1, vehicle.brand, vehicle.model, vehicle.km_done, vehicle.service_date)

    def create_vehicle_object(brand, model, km_done_str, service_date, vehicles):
        try:
            km_done_str = km_done_str.replace(",", ".")
            km_done = float(km_done_str)

            new_vehicle = Vehicle(brand=brand, model=model, km_done=km_done, service_date=service_date)

            vehicles.append(new_vehicle)

            return True
        except ValueError:
            return False

    def add_new_vehicle(vehicles):
        brand = input("Please specify the brand of the vehicle: ")
        model = input("Please specify the model of the vehicle: ")
        km_done_str = input("Please specify how many kilometres the vehicle has driven so far: ")
        service_date = input("Please specify the last known service date: ")

        result = create_vehicle_object(brand, model, km_done_str, service_date, vehicles)

        if result:
            print("Thank you, your vehicle %s %s has been added to the system!") % (brand, model)
        else:
            print("Please specify kilometres.")

    def choose_vehicle(vehicles):
        print("Please choose the number of the vehicle you would like to edit.")
        print(" ")
        list_all_vehicles(vehicles)
        print(" ")
        selection = input("Which vehicle number would you like to access? ")
        return vehicles[int(selection) - 1]

    def add_new_kilometres(vehicles):
        sel_vehicle = choose_vehicle(vehicles)

        print("You have selected vehicle %s %s with %s kilometres.") \
        % (sel_vehicle.brand, sel_vehicle.model, sel_vehicle.km_done)
        print(" ")
        new_kilometres_str = input("How many kilometres would you like to add? ")
        print(" ")

        try:
            new_km_str = new_km_str.replace(",", ".")
            new_km = float(new_km_str)

            sel_vehicle.add_km(new_km)
            print("The updated number of kilometres for %s %s is now %s.") \
            % (sel_vehicle.brand, sel_vehicle.model, sel_vehicle.km_done)
        except ValueError:
            print("Please enter the number of kilometres you would like to add.")

    def change_service_date(vehicles):
        sel_vehicle = choose_vehicle(vehicles)

        print("You have selected the vehicle %s %s with the service date %s.") \
        % (sel_vehicle.brand, sel_vehicle.model, sel_vehicle_service_date)
        print(" ")
        new_service_date = input("Please specify the new service date for the vehicle. ")
        print(" ")
        sel_vehicle.update_service_date(new_date=new_service_date)
        print("The service date has been updated!")

    def save_to_disk(vehicles):
        with open("vehicles.txt", "w+") as veh_file:
            for vehicle in vehicles:
                veh_file.write("%s,%s,%s,%s\n" % (vehicle.brand, vehicle.model, vehicle.km_done, vehicle.service_date))

    def main():
        print("Welcome to the vehicle management program!")

        vehicles = []

        with open("vehicles.txt", "r") as v_file:
            for line in v_file:
                try:
                    brand, model, km_done_str, service_date = line.split(",")
                    create_vehicle_object(brand, model, km_done_str, service_date, vehicles)
                except ValueError:
                    continue

        while True:
            print(" ")
            print("Please select one of the following options: ")
            print("a) View all vehicles.")
            print("b) Add a new vehicle.")
            print("c) Edit mileage.")
            print("d) Edit service date.")
            print("e) Quit.")
            print(" ")

            choice = input("Which option do you select? ")
            print(" ")

            if choice.lower() == "a":
                list_all_vehicles(vehicles)
            elif choice.lower() == "b":
                add_new_vehicle(vehicles)
            elif choice.lower() == "c":
                add_new_kilometres(vehicles)
            elif choice.lower() == "d":
                change_service_date(vehicles)
            elif choice.lower() == "e":
                print("Thank you for using the Vehicle Manager.")
                save_to_disk(vehicles)
                break
            else:
                print("We did not quite get you. Please type in the letter a, b, c, or d.")

    if __name__ == "__main__":
        main()
