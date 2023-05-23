from typing import Optional

class Record:
    def __init__(self, name: str, phone: str, surname: Optional[str] = None, birth_date: Optional[str] = None):
        self._name = name
        self._surname = surname
        self._phone = phone
        self._birth_date = birth_date

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def phone(self):
        return self._phone

    @property
    def birth_date(self):
        return self._birth_date


class Directory:
    def __init__(self):
        self._records = []
        self._emergency_numbers = {"Police": "911", "Fire": "112", "Ambulance": "999"}

    def add_record(self, record):
        self._records.append(record)

    def delete_record(self, record):
        if record in self._records and record.name not in self._emergency_numbers:
            self._records.remove(record)

    def edit_record(self, record, new_phone):
        if record in self._records and record.name not in self._emergency_numbers:
            record._phone = new_phone

    def get_records(self):
        return self._records + [Record(name, number) for name, number in self._emergency_numbers.items()]


class Interface:
    def __init__(self, directory):
        self._directory = directory

    def run(self):
        print("Welcome to the Phone Directory!")
        while True:
            print("\nPlease select an option:")
            print("1. Add a record")
            print("2. Delete a record")
            print("3. Edit a record")
            print("4. View all records")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self._add_record()
            elif choice == "2":
                self._delete_record()
            elif choice == "3":
                self._edit_record()
            elif choice == "4":
                self._view_records()
            elif choice == "5":
                print("Exiting the Phone Directory...")
                break
            else:
                print("Invalid choice. Please try again.")

    def _add_record(self):
        name = input("Enter the name: ")
        surname = input("Enter the surname (optional): ")
        phone = input("Enter the phone number: ")
        birth_date = input("Enter the birth date (optional): ")

        record = Record(name, phone, surname, birth_date)
        self._directory.add_record(record)
        print("Record added successfully.")

    def _delete_record(self):
        records = self._directory.get_records()
        if not records:
            print("No records found.")
            return

        print("Select a record to delete:")
        for i, record in enumerate(records):
            print(f"{i+1}. {record.name}")

        while True:
            choice = input("Enter the record number: ")
            if not choice.isdigit() or int(choice) < 1 or int(choice) > len(records):
                print("Invalid choice. Please try again.")
            else:
                record = records[int(choice) - 1]
                if record.name in self._directory._emergency_numbers:
                    print("Cannot delete emergency service numbers.")
                else:
                    self._directory.delete_record(record)
                    print("Record deleted successfully.")
                break

    def _edit_record(self):
        records = self._directory.get_records()
        if not records:
            print("No records found.")
            return

        print("Select a record to edit:")
        for i, record in enumerate(records):
            print(f"{i+1}. {record.name}")

        while True:
            choice = input("Enter the record number: ")
            if not choice.isdigit() or int(choice) < 1 or int(choice) > len(records):
                print("Invalid choice. Please try again.")
            else:
                record = records[int(choice) - 1]
                if record.name in self._directory._emergency_numbers:
                    print("Cannot edit emergency service numbers.")
                else:
                    new_phone = input("Enter the new phone number: ")
                    self._directory.edit_record(record, new_phone)
                    print("Record edited successfully.")
                break

    def _view_records(self):
        records = self._directory.get_records()
        if not records:
            print("No records found.")
        else:
            print("Phone Directory Records:")
            for record in records:
                print(f"Name: {record.name}")
                if record.surname:
                    print(f"Surname: {record.surname}")
                print(f"Phone: {record.phone}")
                if record.birth_date:
                    print(f"Birth Date: {record.birth_date}")
                print()


def main():
    directory = Directory()
    interface = Interface(directory)
    interface.run()


if __name__ == "__main__":
    main()
