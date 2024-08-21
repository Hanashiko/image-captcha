from captcha.image import ImageCaptcha
from io import BytesIO
from PIL import Image

def main() -> None:
	text: str = "HANASHIKO"

	captcha: ImageCaptcha = ImageCaptcha(width=400,
										height=200,
										fonts=['./fonts/Anton.ttf',
												'./fonts/BodoniModaSC-Italic.ttf',
												'./fonts/BodoniModaSC.ttf',
												'./fonts/DMSerifText-Italic.ttf',
												'./fonts/DMSerifText.ttf',
												'./fonts/EduVICWANTBeginner.ttf',
												'./fonts/Jersey10.ttf',
												'./fonts/Matemasie.ttf',
												'./fonts/NewAmsterdam.ttf',
												'./fonts/QwitcherGrypen-Bold.ttf',
												'./fonts/QwitcherGrypen.ttf'],
										font_sizes=(40, 70, 100))

	# captcha.write(text, 'captcha.png')

	data: BytesIO = captcha.generate(text)
	image: Image = Image.open(data)
	image.show('Sample captcha')

if __name__ == "__main__":
	main()