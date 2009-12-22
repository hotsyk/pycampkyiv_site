# -*- coding: utf-8 -*-

from south.db import db
from django.db import models
from pycamp.core.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Presentation'
        db.create_table('core_presentation', (
            ('id', orm['core.Presentation:id']),
            ('time_start', orm['core.Presentation:time_start']),
            ('time_end', orm['core.Presentation:time_end']),
            ('file', orm['core.Presentation:file']),
        ))
        db.send_create_signal('core', ['Presentation'])
        
        # Adding model 'PresentationField'
        db.create_table('core_presentationfield', (
            ('id', orm['core.PresentationField:id']),
            ('presentation', orm['core.PresentationField:presentation']),
            ('lang', orm['core.PresentationField:lang']),
            ('property', orm['core.PresentationField:property']),
            ('value', orm['core.PresentationField:value']),
        ))
        db.send_create_signal('core', ['PresentationField'])
        
        # Adding model 'Speaker'
        db.create_table('core_speaker', (
            ('id', orm['core.Speaker:id']),
            ('user', orm['core.Speaker:user']),
            ('email', orm['core.Speaker:email']),
            ('site', orm['core.Speaker:site']),
        ))
        db.send_create_signal('core', ['Speaker'])
        
        # Adding model 'SpeakerField'
        db.create_table('core_speakerfield', (
            ('id', orm['core.SpeakerField:id']),
            ('speaker', orm['core.SpeakerField:speaker']),
            ('lang', orm['core.SpeakerField:lang']),
            ('property', orm['core.SpeakerField:property']),
            ('value', orm['core.SpeakerField:value']),
        ))
        db.send_create_signal('core', ['SpeakerField'])
        
        # Adding model 'HeaderBlock'
        db.create_table('core_headerblock', (
            ('id', orm['core.HeaderBlock:id']),
            ('lang', orm['core.HeaderBlock:lang']),
            ('text', orm['core.HeaderBlock:text']),
        ))
        db.send_create_signal('core', ['HeaderBlock'])
        
        # Adding ManyToManyField 'Presentation.speakers'
        db.create_table('core_presentation_speakers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('presentation', models.ForeignKey(orm.Presentation, null=False)),
            ('speaker', models.ForeignKey(orm.Speaker, null=False))
        ))
        
        # Creating unique_together for [speaker, lang, property] on SpeakerField.
        db.create_unique('core_speakerfield', ['speaker_id', 'lang', 'property'])
        
    
    
    def backwards(self, orm):
        
        # Deleting unique_together for [speaker, lang, property] on SpeakerField.
        db.delete_unique('core_speakerfield', ['speaker_id', 'lang', 'property'])
        
        # Deleting model 'Presentation'
        db.delete_table('core_presentation')
        
        # Deleting model 'PresentationField'
        db.delete_table('core_presentationfield')
        
        # Deleting model 'Speaker'
        db.delete_table('core_speaker')
        
        # Deleting model 'SpeakerField'
        db.delete_table('core_speakerfield')
        
        # Deleting model 'HeaderBlock'
        db.delete_table('core_headerblock')
        
        # Dropping ManyToManyField 'Presentation.speakers'
        db.delete_table('core_presentation_speakers')
        
    
    
    models = {
        'auth.group': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.headerblock': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.SmallIntegerField', [], {'unique': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'core.presentation': {
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'speakers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Speaker']"}),
            'time_end': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'time_start': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'core.presentationfield': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.SmallIntegerField', [], {}),
            'presentation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Presentation']"}),
            'property': ('django.db.models.fields.SmallIntegerField', [], {}),
            'value': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'core.speaker': {
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'core.speakerfield': {
            'Meta': {'unique_together': "(('speaker', 'lang', 'property'),)"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.SmallIntegerField', [], {}),
            'property': ('django.db.models.fields.SmallIntegerField', [], {}),
            'speaker': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Speaker']"}),
            'value': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['core']
