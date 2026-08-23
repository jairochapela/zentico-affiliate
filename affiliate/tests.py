from django.test import TestCase

from .models import AffiliateLink


class AffiliateViewsTests(TestCase):
	def setUp(self):
		self.active_link = AffiliateLink.objects.create(
			name='Curso de analítica',
			slug='curso-analitica',
			advertiser='Zentico Academy',
			target_url='https://example.com/curso',
		)
		self.inactive_link = AffiliateLink.objects.create(
			name='Guía antigua',
			slug='guia-antigua',
			advertiser='Zentico Academy',
			target_url='https://example.com/guia',
			active=False,
		)

	def test_home_returns_active_links(self):
		response = self.client.get('/')

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, self.active_link.name)
		self.assertNotContains(response, self.inactive_link.name)

	def test_missing_link_returns_not_found(self):
		response = self.client.get('/go/no-existe/')

		self.assertEqual(response.status_code, 404)

	def test_active_link_redirects_and_increments_clicks(self):
		response = self.client.get('/go/curso-analitica/')

		self.assertRedirects(response, self.active_link.target_url, fetch_redirect_response=False)
		self.active_link.refresh_from_db()
		self.assertEqual(self.active_link.clicks, 1)

	def test_inactive_link_returns_not_found(self):
		response = self.client.get('/go/guia-antigua/')

		self.assertEqual(response.status_code, 404)
		self.inactive_link.refresh_from_db()
		self.assertEqual(self.inactive_link.clicks, 0)
