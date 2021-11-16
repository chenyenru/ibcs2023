import context as c


def menu1(ctx):
    prompt = "Albert Wang asks you if you like Mingdao. You don't know what he's up to."
    options = []
    options.append(c.create_menu_item(1, "Ask him what he's up to", ask))
    options.append(c.create_menu_item(
        1, "Express your 'love' for Mingdao", tell))
    options.append(c.create_menu_item(
        1, "Tell him everything you hate about Mingdao", ask))
    options.append(c.create_menu_item(
        1, "Activate your mystery card, with consequence", mystery))

    menu = c.create_menu(prompt, options)
    return c.draw_menu(ctx, menu)


def ask(ctx):
    prompt = """He's never seen such a genuine student in Mingdao. 
    However, he foresees that you would not fit into the human resources category Mingdao create.
    Thus, you're attacked by SDG4, quality education.
    10 years serving in Mingdao.
    """
    options = []
    options.append(c.create_menu_item(1, "Curse him and do it", None))
    options.append(c.create_menu_item(1, "Hug him and do it", None))
    options.append(c.create_menu_item(
        1, "Tell him you really love Mingdao and do it", None))
    options.append(c.create_menu_item(
        1, "Go find his son and perhaps you'll be saved", None))

    menu = c.create_menu(prompt, options)
    return c.draw_menu(ctx, menu)


def tell(ctx):
    prompt = """He sees through your insincerity and decides to attack you with SDG4, quality education. 
    Clearly, you're sentenced of 6 more years in Mingdao."""
    options = []
    options.append(c.create_menu_item(1, "Curse him and do it", None))
    options.append(c.create_menu_item(1, "Hug him and do it", None))
    options.append(c.create_menu_item(
        1, "Tell him you really love Mingdao and do it", None))
    options.append(c.create_menu_item(
        1, "Go find his son and perhaps you'll be saved", None))

    menu = c.create_menu(prompt, options)
    return c.draw_menu(ctx, menu)


def mystery(ctx):
    prompt = "You ran away. You're safe"
    options = []
    options.append(c.create_menu_item(1, "Return", menu1))
    options.append(c.create_menu_item(1, "Enjoy your life", None))
    options.append(c.create_menu_item(
        1, "Get kicked out and start a startup", None))
    options.append(c.create_menu_item(
        1, "Go to college without a high school diploma. good luck", None))

    menu = c.create_menu(prompt, options)
    return c.draw_menu(ctx, menu)


def main():
    ctx = c.init()
    cb = menu1(ctx)
    while cb != None:  # will exit the program
        cb = cb(ctx)


if __name__ == "__main__":
    main()
