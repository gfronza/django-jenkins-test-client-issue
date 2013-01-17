from django.test import Client, TestCase
from django.core.urlresolvers import reverse


class TestSimple(TestCase):

    def test_basic(self):
        client = Client()

        resp = client.get('%s?q=test&type=user' % reverse('search'))
        page = resp.context['page']
        paginator = resp.context['paginator']

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(page['number'], 1)
        self.assertEqual(paginator['num_pages'], 1)
        self.assertEqual(len(page['object_list']), 2)
