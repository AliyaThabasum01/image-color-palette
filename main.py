from palette import get_palette

print("🎨 Image Color Palette")
print("=" * 40)

image_path = input("Enter image path: ").strip()

try:
    colors = get_palette(image_path)

    print("\n🎨 Dominant Colors")
    print("=" * 40)

    for i, color in enumerate(colors, 1):
        print(
            f"{i}. RGB{color['rgb']}  "
            f"HEX {color['hex']}"
        )

except FileNotFoundError:
    print("❌ Image not found.")
except Exception as error:
    print(f"❌ Error: {error}")
