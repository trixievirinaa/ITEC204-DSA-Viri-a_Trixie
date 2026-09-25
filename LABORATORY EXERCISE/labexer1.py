tickets = [
    ["INC1392939", "BOT-Inventory", "Failed to generate the daily report"],
    ["INC1392940", "BOT-Email", "Failed to send the scheduled notification"],
    ["INC1392941", "BOT-DataSync", "Encountered an error during data transfer"],
    ["INC1392942", "BOT-Invoice", "Failed to process an invoice"],
    ["INC1392943", "BOT-Report", "Failed to generate the weekly report"],
    ["INC1392944", "BOT-FileTransfer", "Failed to upload the required file"],
    ["INC1392945", "BOT-DataEntry", "Encountered an error while entering records"],
    ["INC1392946", "BOT-Backup", "Failed to complete the scheduled backup"],
    ["INC1392947", "BOT-Validation", "Failed to validate the submitted records"],
    ["INC1392948", "BOT-Notification", "Failed to send the system alert"]
]


def add_ticket():
    incident_id = input("Enter Incident ID: ")
    bot = input("Enter Bot: ")
    description = input("Enter Short Description: ")

    tickets.append([incident_id, bot, description])
    print("Ticket added successfully!")


def display_tickets():
    if len(tickets) == 0:
        print("No active incident tickets.")
    else:
        print("\n--- ACTIVE INCIDENT TICKETS ---")

        for ticket in tickets:
            print("Incident ID:", ticket[0])
            print("Bot:", ticket[1])
            print("Description:", ticket[2])
            print("-----------------------------")


def search_ticket():
    incident_id = input("Enter Incident ID to search: ")

    found = False

    for ticket in tickets:
        if ticket[0] == incident_id:
            print("\nTicket Found!")
            print("Incident ID:", ticket[0])
            print("Bot:", ticket[1])
            print("Description:", ticket[2])
            found = True
            break

    if not found:
        print("Ticket not found.")


def remove_ticket():
    incident_id = input("Enter Incident ID to remove: ")

    for ticket in tickets:
        if ticket[0] == incident_id:
            tickets.remove(ticket)
            print("Ticket removed successfully!")
            return

    print("Ticket not found.")


def count_tickets():
    print("Total active incident tickets:", len(tickets))


# Main Menu
while True:
    print("\n===================================")
    print(" IT AUTOMATION INCIDENT TICKET MANAGER")
    print("===================================")
    print("1. Add a new incident ticket")
    print("2. Display all active incident tickets")
    print("3. Search for a ticket")
    print("4. Remove a resolved ticket")
    print("5. Count active incident tickets")
    print("6. Exit")
    print()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_ticket()

    elif choice == "2":
        display_tickets()

    elif choice == "3":
        search_ticket()

    elif choice == "4":
        remove_ticket()

    elif choice == "5":
        count_tickets()

    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Please try again.")