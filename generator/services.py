from PIL import Image

def generate_creative(background_path, logo_path=None, panel_path=None, output_path="output.png"):

    #open background

    bg = Image.open(background_path).convert("RGBA")

    #if logo exists

    if logo_path:
        logo = Image.open(logo_path).convert("RGBA")

        #Reasize logo (auto scale)

        logo.thumbnail((bg.width // 4, bg.height // 4))

    #Position (top_, logo)

        x = bg.width - logo.width - 20
        y = 20

    # Paste logo

        bg.paste(logo, (x, y), logo)


#Panel (BOTTOM)
    if panel_path:
    
        panel = Image.open(panel_path).convert("RGBA")

        panel.thumbnail((bg.width, bg.height // 4))

        x = 0
        y = bg.height - panel.height

        bg.paste(panel, (x, y), panel)

    bg.save(output_path)
    return output_path


    #Save final image

    bg.save(output_path)

    return output_path