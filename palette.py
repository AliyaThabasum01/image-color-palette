from PIL import Image


def get_palette(image_path, count=5):
    image = Image.open(image_path).convert("RGB")

    image.thumbnail((150, 150))

    colors = image.getcolors(
        maxcolors=image.width * image.height
    )

    colors.sort(reverse=True)

    result = []

    for _, rgb in colors[:count]:
        hex_value = "#{:02X}{:02X}{:02X}".format(*rgb)

        result.append({
            "rgb": rgb,
            "hex": hex_value
        })

    return result
