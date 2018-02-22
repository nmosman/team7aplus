from time import sleep
from demo_opts import get_device
from menu import Menu

def main():
    m = Menu({"options":["None"],"cursor":0})

    for i in range(20):
        menu_options = {
            "options": ["First num: "+str(i), "Something b", "Other C", "Also D"],
            "cursor": i%4,
        }

        try:
            device = get_device()
            m.run(device, updated_options=menu_options)
        except KeyboardInterrupt:
            pass
        sleep(1)



if __name__ == "__main__":
    main()