contacts1 = {
    "Anu":"8596745698",
    "Teena":"7896562389"
}
contacts2 = {
          "john":"7896854123",
           "priya":"5698638745"
}
print("contacts1:",contacts1)
print("contacts2:",contacts2)

merged_contacts = contacts1.copy()
merged_contacts.update(contacts2)

print("merged contacts:")
print(merged_contacts)