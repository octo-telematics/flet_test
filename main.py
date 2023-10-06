
import flet as ft
from PzTimer import *
import unittest


class TestClass(unittest.TestCase):
	def test_prova1(self):
		self.assertEqual(1, 1)

	def test_prova2(self):
		self.assertEqual(2, 2)


def main(page: ft.page):
	page.title = 'Flet TestApp'
	page.vertical_alignment = ft.MainAxisAlignment.CENTER
	# page.horizontal_alignment = ft.MainAxisAlignment.CENTER

	number = ft.TextField(value='0', text_align="center", width=100)
	text1 = ft.Text(value='Hello, world!', color='white')
	text2 = ft.Text(value='Ciao, Paolo!', color='white')
	text3 = ft.Text(value='Ciao, Paoletto!', color='white')
	text4 = ft.Text(value='Ciao, Paolone!', color='white')

	page.add(
		ft.Column(
			[
				number,
				text1,
				text2,
				text3,
				text4
			],
			alignment=ft.MainAxisAlignment.CENTER
		)
	)

	def timer_event():
		number.value = str(int(number.value)+1)
		page.controls[0].update()

	PzTimer(1, timer_event).start()


if __name__ == "__main__":
	ft.app(target=main) # , port=8550, view=ft.AppView.WEB_BROWSER)
