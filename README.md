# Python-Troll
This is a modular tool for trolling you friends. 

You can easily modify it and add new functionalities or deactivate some.

## _Add new functionality_
Add a new function like that
```python
def my_troll_function(preferences):
	while True:
		do_whatever_you_want()
		time.sleep(preferences["sleep_time"])
```
Then you only need to add this function to the `abilities` dictionary like this:
```python
abilities = {
    'write_to_autostart': (write_to_autostart, {"active":True}),
    'rotate_screen': (rotate_screen, {"active":True, "interval":[1,2]}),
    '*name_of_your_troll*': (my_troll_function, {"active":True, "other_preferences":"and_their_values","sleep_time":5})
}
```
`{"active":True, "other_preferences":"and_their_values","sleep_time":5}` will be passed as preferences to your new function.

All abilities listed here will automaticaly be launched in an own thread on startup if ther attribute `active` is set to `True`

## Compile to exe
You can compile your finished script to an .exe file.

Firstly install pyinstaller:
`pip install pyinstaller`

Then compile using:
`pyinstaller --noconfirm --onefile --windowed --uac-admin --clean --name "TheNameForTheTrollProcess" "troll.py" `

### Implemented features

- write itself to autostart folder and registry
- rotate screen in an given interval to a random rotation


