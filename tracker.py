import streamlit as st

def add_expense(expenses, category, amount):
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

def view_expenses(expenses):
    total = 0
    st.write("Expenses:")
    for category, amount in expenses.items():
        st.write(f"{category}: ${amount}")
        total += amount
    st.write(f"Total: ${total}")

def main():
    expenses = {}
    st.title("Expense Tracker")
    while True:
        choice = st.sidebar.selectbox("Menu", ["Add Expense", "View Expenses", "Exit"])

        if choice == "Add Expense":
            category = st.text_input("Enter expense category:")
            amount = st.number_input("Enter expense amount:", step=0.01)
            if st.button("Add Expense"):
                add_expense(expenses, category, amount)
                st.success("Expense added successfully!")

        elif choice == "View Expenses":
            view_expenses(expenses)

        elif choice == "Exit":
            st.warning("Exiting...")
            break

if __name__ == "__main__":
    main()
