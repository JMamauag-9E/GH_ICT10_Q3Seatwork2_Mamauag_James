#Use: varname = document.querySelector('input[name='#']:checked').value -> Getting data from a radio button
#Use: document.getElementById('idname')innerHTML = displaying image using pyscript (optional)
#Use: <img src='#' height = '#' width = '#'>

from pyscript import display, document


def Intramurals_2526(e):
    document.getElementById('output').innerHTML = ' '

    Sagot1 = document.querySelector('input[name="Yes_or_no1"]:checked').value
    Sagot2 = document.querySelector('input[name="Yes_or_no2"]:checked').value

    if Sagot1 and Sagot2 == "yes":
        display(f'Yes', target='output')
    elif Sagot1 == "yes":
        display(f'You must get the medical certficate first.', target='output')
    elif Sagot2 == "yes":
        display(f'You must answer the online registration first.', target='output')
    else:
        display(f'You must complete these first before you join.', target='output')

    sections = document.querySelector('input[name="sections"]:checked').value
    if "Emerald":
    elif "Ruby":
    elif "Sapphire":
    elif "Topaz":