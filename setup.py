from setuptools import setup

setup(
    name='paged_html_theme',
    entry_points = {
        'sphinx.html_themes': [
            'paged_html_theme = paged_html_theme',
        ]
    },
)