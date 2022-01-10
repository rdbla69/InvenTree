""" Unit tests for action caller sample"""

from django.test import TestCase

from plugin import plugin_registry


class SampleApiCallerPluginTests(TestCase):
    """ Tests for SampleApiCallerPluginTests """

    def test_return(self):
        """check if the external api call works"""
        # The plugin should be defined
        self.assertIn('sample-api-caller', plugin_registry.plugins)
        plg = plugin_registry.plugins['sample-api-caller']
        self.assertTrue(plg)

        # do an api call
        result = plg.get_external_url()
        self.assertTrue(result)
        self.assertIn('data', result,)
