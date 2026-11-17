from pyscript import document

# Members already in each grade
grade_9 = {"Guia Suarez", "Casey Canlas"}
grade_10 = {"Princess Beltran", "Annika Marquez"}

# Combine the grade lists
all_members = grade_9 | grade_10


def render_members():
    output = document.querySelector("#output")
    output.innerHTML = ""

    count = document.createElement("p")
    count.id = "member-count"
    count.textContent = f"{len(all_members)} current members"
    output.appendChild(count)

    member_list = document.createElement("ul")
    member_list.id = "member-list"
    output.appendChild(member_list)
    list(map(add_to_list, sorted(all_members)))


def add_to_list(name):
    item = document.createElement("li")
    item.textContent = name
    document.querySelector("#member-list").appendChild(item)


def add_member(event):
    first_input = document.querySelector("#first-name")
    last_input = document.querySelector("#last-name")
    first = first_input.value.strip().title()
    last = last_input.value.strip().title()

    name = f"{first} {last}".strip()
    all_members.update(filter(None, [name]))
    render_members()

    first_input.value = ""
    last_input.value = ""
    first_input.focus()


render_members()
