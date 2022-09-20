from re import L
from rich import print
from rich.layout import Layout

layout = Layout()

layout.split_column(
    Layout(name='top', ratio=2),
    Layout(name='bottom')

)

print(layout)
