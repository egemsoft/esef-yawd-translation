# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('name', models.CharField(max_length=7, serialize=False, verbose_name='Name', primary_key=True, choices=[(b'af', b'Afrikaans'), (b'sq', b'Albanian'), (b'ar', b'Arabic'), (b'es-ar', b'Argentinian Spanish'), (b'ast', b'Asturian'), (b'en-au', b'Australian English'), (b'az', b'Azerbaijani'), (b'eu', b'Basque'), (b'be', b'Belarusian'), (b'bn', b'Bengali'), (b'bs', b'Bosnian'), (b'pt-br', b'Brazilian Portuguese'), (b'br', b'Breton'), (b'en-gb', b'British English'), (b'bg', b'Bulgarian'), (b'my', b'Burmese'), (b'ca', b'Catalan'), (b'hr', b'Croatian'), (b'cs', b'Czech'), (b'da', b'Danish'), (b'nl', b'Dutch'), (b'en', b'English'), (b'eo', b'Esperanto'), (b'et', b'Estonian'), (b'fi', b'Finnish'), (b'fr', b'French'), (b'fy', b'Frisian'), (b'gl', b'Galician'), (b'ka', b'Georgian'), (b'de', b'German'), (b'el', b'Greek'), (b'he', b'Hebrew'), (b'hi', b'Hindi'), (b'hu', b'Hungarian'), (b'is', b'Icelandic'), (b'io', b'Ido'), (b'id', b'Indonesian'), (b'ia', b'Interlingua'), (b'ga', b'Irish'), (b'it', b'Italian'), (b'ja', b'Japanese'), (b'kn', b'Kannada'), (b'kk', b'Kazakh'), (b'km', b'Khmer'), (b'ko', b'Korean'), (b'lv', b'Latvian'), (b'lt', b'Lithuanian'), (b'lb', b'Luxembourgish'), (b'mk', b'Macedonian'), (b'ml', b'Malayalam'), (b'mr', b'Marathi'), (b'es-mx', b'Mexican Spanish'), (b'mn', b'Mongolian'), (b'ne', b'Nepali'), (b'es-ni', b'Nicaraguan Spanish'), (b'nb', b'Norwegian Bokmal'), (b'nn', b'Norwegian Nynorsk'), (b'os', b'Ossetic'), (b'fa', b'Persian'), (b'pl', b'Polish'), (b'pt', b'Portuguese'), (b'pa', b'Punjabi'), (b'ro', b'Romanian'), (b'ru', b'Russian'), (b'sr', b'Serbian'), (b'sr-latn', b'Serbian Latin'), (b'zh-cn', b'Simplified Chinese'), (b'zh-hans', b'Simplified Chinese'), (b'sk', b'Slovak'), (b'sl', b'Slovenian'), (b'es', b'Spanish'), (b'sw', b'Swahili'), (b'sv', b'Swedish'), (b'ta', b'Tamil'), (b'tt', b'Tatar'), (b'te', b'Telugu'), (b'th', b'Thai'), (b'zh-hant', b'Traditional Chinese'), (b'zh-tw', b'Traditional Chinese'), (b'tr', b'Turkish'), (b'udm', b'Udmurt'), (b'uk', b'Ukrainian'), (b'ur', b'Urdu'), (b'es-ve', b'Venezuelan Spanish'), (b'vi', b'Vietnamese'), (b'cy', b'Welsh')])),
                ('image', models.CharField(max_length=50)),
                ('default', models.BooleanField(default=False, verbose_name='Default')),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
            ],
            options={
                'ordering': ['order', 'name'],
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
                'permissions': (('view_translations', 'Can see translation messages for a language'), ('edit_translations', "Can edit the language's translation messages")),
            },
        ),
    ]
