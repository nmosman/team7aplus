
# LCD display on Raspberry pi
- We are using the luma library to display text and menus.
- Refer to: https://github.com/rm-hull/luma.examples

## Usage info
Example in `main_menu.py`.

Initialize a Menu object from `menu.py` with some starting menu options:
```python
menu_options = {
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "cursor": 2,
        }
m = Menu(menu_options)
```


Then to display/update the screen: either call `m.run()` or `m.run(updated_options)`.

To update the menu:
```python
menu_options = {
            "options": ["UPDATED OPTION", "Option 2", "ANOTHER UPDATE", "Option 4"],
            "cursor": 0,
        }
m.run(menu_options)
```


## Limitations
We likely won't need more than 6 options, so there is no point in implementing scrolling. 

Do not add more than 6 options. 

It won't work.

Seriously.


## Running on personal computer
- Install `luma.oled` (using virtualenv or conda is suggested): `pip install luma.oled`
- Install `luma.emulator` (using virtualenv or conda is suggested): `pip install luma.emulator`
- For the demo: from the current directory run `python main_menu.py --display=pygame`